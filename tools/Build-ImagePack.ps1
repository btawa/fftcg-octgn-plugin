[CmdletBinding()]
param(
	[Parameter(Mandatory = $true)]
	[string[]]$SetIds,
	[string]$OutputPath
)

$ErrorActionPreference = 'Stop'

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$gameDirectories = @(Get-ChildItem -LiteralPath $repositoryRoot -Directory | Where-Object {
	Test-Path -LiteralPath (Join-Path $_.FullName 'definition.xml') -PathType Leaf
})
if ($gameDirectories.Count -ne 1) {
	throw "Expected exactly one OCTGN game directory under '$repositoryRoot'; found $($gameDirectories.Count)."
}

$gameSource = $gameDirectories[0].FullName
$definitionPath = Join-Path $gameSource 'definition.xml'
[xml]$definition = Get-Content -LiteralPath $definitionPath -Raw
$gameGuid = [guid]::Empty
if (-not [guid]::TryParse($definition.game.id, [ref]$gameGuid)) {
	throw "The game ID in '$definitionPath' is not a valid UUID."
}
$gameId = $gameGuid.ToString()

$setSourceRoot = Join-Path $repositoryRoot 'sets'
if (-not (Test-Path -LiteralPath $setSourceRoot -PathType Container)) {
	throw "Set source directory not found: '$setSourceRoot'."
}

$setSources = @{}
foreach ($setDirectory in Get-ChildItem -LiteralPath $setSourceRoot -Directory) {
	$setFile = Join-Path $setDirectory.FullName 'set.xml'
	if (-not (Test-Path -LiteralPath $setFile -PathType Leaf)) {
		throw "Missing set.xml in '$($setDirectory.FullName)'."
	}

	[xml]$set = Get-Content -LiteralPath $setFile -Raw
	$setGuid = [guid]::Empty
	if (-not [guid]::TryParse($set.set.id, [ref]$setGuid)) {
		throw "Invalid set UUID '$($set.set.id)' in '$setFile'."
	}
	$setId = $setGuid.ToString()
	if ($setSources.ContainsKey($setId)) {
		throw "Duplicate set UUID '$setId' in '$($setSources[$setId])' and '$($setDirectory.FullName)'."
	}
	$setGameGuid = [guid]::Empty
	if (-not [guid]::TryParse($set.set.gameId, [ref]$setGameGuid) -or $setGameGuid.ToString() -ne $gameId) {
		throw "Set '$($set.set.GetAttribute('name'))' has a missing or mismatched game ID in '$setFile'."
	}

	$setSources[$setId] = $setDirectory.FullName
}

$selectedSets = @()
$imageFiles = @()
foreach ($requestedSetId in $SetIds) {
	$requestedGuid = [guid]::Empty
	if (-not [guid]::TryParse($requestedSetId, [ref]$requestedGuid)) {
		throw "Invalid set UUID: '$requestedSetId'."
	}
	$setId = $requestedGuid.ToString()
	if (-not $setSources.ContainsKey($setId)) {
		throw "Set UUID not found under '$setSourceRoot': $setId"
	}
	if ($selectedSets -contains $setId) {
		throw "Set UUID was specified more than once: $setId"
	}

	$setPath = $setSources[$setId]
	[xml]$set = Get-Content -LiteralPath (Join-Path $setPath 'set.xml') -Raw
	$cardIds = @{}
	foreach ($card in $set.set.cards.card) {
		$cardGuid = [guid]::Empty
		if (-not [guid]::TryParse($card.id, [ref]$cardGuid)) {
			throw "Invalid card UUID '$($card.id)' in '$setPath\set.xml'."
		}
		$cardIds[$cardGuid.ToString()] = $true
	}

	$cardsPath = Join-Path $setPath 'Cards'
	if (-not (Test-Path -LiteralPath $cardsPath -PathType Container)) {
		throw "Card image directory not found: '$cardsPath'."
	}
	$images = @(Get-ChildItem -LiteralPath $cardsPath -File |
		Where-Object { $_.Extension.ToLowerInvariant() -in @('.jpg', '.jpeg', '.png') })
	if ($images.Count -eq 0) {
		throw "No card images found for set $setId in '$cardsPath'."
	}

	foreach ($image in $images) {
		$imageGuid = [guid]::Empty
		if (-not [guid]::TryParse($image.BaseName, [ref]$imageGuid) -or -not $cardIds.ContainsKey($imageGuid.ToString())) {
			throw "Image filename does not match a card UUID in set ${setId}: $($image.Name)"
		}
		$imageFiles += [pscustomobject]@{
			Path = $image.FullName
			Entry = "$gameId/Sets/$setId/Cards/$($image.Name)"
		}
	}
	$selectedSets += $setId
}
if ($selectedSets.Count -eq 0) {
	throw 'Select at least one set UUID with -SetIds.'
}

if ([string]::IsNullOrWhiteSpace($env:TEMP)) {
	throw 'The TEMP environment variable is not set; specify -OutputPath.'
}
if ([string]::IsNullOrWhiteSpace($OutputPath)) {
	$OutputPath = Join-Path $env:TEMP ("FFTCG-images-" + [guid]::NewGuid().ToString('N') + '.o8c')
}
elseif (-not [System.IO.Path]::IsPathRooted($OutputPath)) {
	$OutputPath = Join-Path (Get-Location).Path $OutputPath
}
$OutputPath = [System.IO.Path]::GetFullPath($OutputPath)
if ([System.IO.Path]::GetExtension($OutputPath) -ne '.o8c') {
	throw "Image pack output path must use the .o8c extension: '$OutputPath'."
}
if (Test-Path -LiteralPath $OutputPath) {
	throw "Output file already exists: '$OutputPath'. Choose a different path."
}
$outputDirectory = Split-Path -Parent $OutputPath
if (-not (Test-Path -LiteralPath $outputDirectory -PathType Container)) {
	throw "Output directory not found: '$outputDirectory'."
}

$archive = $null
$completed = $false
try {
	Add-Type -AssemblyName System.IO.Compression
	Add-Type -AssemblyName System.IO.Compression.FileSystem
	$archive = [System.IO.Compression.ZipFile]::Open($OutputPath, 'Create')
	foreach ($image in $imageFiles) {
		[void][System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile(
			$archive, $image.Path, $image.Entry, 'Optimal')
	}
	$completed = $true
}
finally {
	if ($null -ne $archive) {
		$archive.Dispose()
	}
	if (-not $completed -and (Test-Path -LiteralPath $OutputPath -PathType Leaf)) {
		Remove-Item -LiteralPath $OutputPath -Force
	}
}

Write-Host "Image pack created: $OutputPath"
Write-Host "Sets: $($selectedSets.Count); images: $($imageFiles.Count)"
