[CmdletBinding()]
param(
	[string]$BuilderPath,
	[switch]$ValidateOnly,
	[switch]$Install,
	[switch]$StageOnly
)

$ErrorActionPreference = 'Stop'

if ($ValidateOnly -and $Install) {
	throw 'Choose either -ValidateOnly or -Install, not both.'
}
if ($StageOnly -and ($ValidateOnly -or $Install)) {
	throw '-StageOnly cannot be combined with -ValidateOnly or -Install.'
}

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
$gameId = [guid]::Empty
if (-not [guid]::TryParse($definition.game.id, [ref]$gameId)) {
	throw "The game ID in '$definitionPath' is not a valid UUID."
}
$gameId = $gameId.ToString()

$setSourceRoot = Join-Path $repositoryRoot 'sets'
if (-not (Test-Path -LiteralPath $setSourceRoot -PathType Container)) {
	throw "Set source directory not found: '$setSourceRoot'."
}
$setDirectories = @(Get-ChildItem -LiteralPath $setSourceRoot -Directory)
if ($setDirectories.Count -eq 0) {
	throw "No set source directories found under '$setSourceRoot'."
}

$setIds = @{}
$setSources = @()
foreach ($setDirectory in $setDirectories) {
	$setFile = Join-Path $setDirectory.FullName 'set.xml'
	if (-not (Test-Path -LiteralPath $setFile -PathType Leaf)) {
		throw "Missing set.xml in '$($setDirectory.FullName)'."
	}

	[xml]$set = Get-Content -LiteralPath $setFile -Raw
	$setId = [guid]::Empty
	if (-not [guid]::TryParse($set.set.id, [ref]$setId)) {
		throw "Invalid set UUID '$($set.set.id)' in '$setFile'."
	}
	$setId = $setId.ToString()

	$setGameId = [guid]::Empty
	if (-not [guid]::TryParse($set.set.gameId, [ref]$setGameId) -or $setGameId.ToString() -ne $gameId) {
		throw "Set '$($set.set.GetAttribute('name'))' has a missing or mismatched game ID in '$setFile'."
	}
	if ($setIds.ContainsKey($setId)) {
		throw "Duplicate set UUID '$setId' in '$($setIds[$setId])' and '$($setDirectory.FullName)'."
	}

	$setIds[$setId] = $setDirectory.FullName
	$setSources += [pscustomobject]@{
		Id = $setId
		Name = $set.set.GetAttribute('name')
		Path = $setDirectory.FullName
	}
}

if ([string]::IsNullOrWhiteSpace($env:TEMP)) {
	throw 'The TEMP environment variable is not set; cannot create a build staging directory.'
}
$stagePath = Join-Path $env:TEMP ("FFTCG-OCTGN-" + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $stagePath | Out-Null

try {
	foreach ($item in Get-ChildItem -LiteralPath $gameSource -Force) {
		if ($item.Name -ne 'Sets') {
			Copy-Item -LiteralPath $item.FullName -Destination $stagePath -Recurse -Force
		}
	}

	$stagedSetsPath = Join-Path $stagePath 'Sets'
	New-Item -ItemType Directory -Path $stagedSetsPath | Out-Null
	foreach ($setSource in $setSources) {
		$stagedSetPath = Join-Path $stagedSetsPath $setSource.Id
		New-Item -ItemType Directory -Path $stagedSetPath | Out-Null
		foreach ($item in Get-ChildItem -LiteralPath $setSource.Path -Force) {
			if ($item.Name -ne 'Cards') {
				Copy-Item -LiteralPath $item.FullName -Destination $stagedSetPath -Recurse
			}
		}
		$stagedCardsPath = Join-Path $stagedSetPath 'Cards'
		New-Item -ItemType Directory -Path $stagedCardsPath | Out-Null
	}

	Write-Host "Staged $($setSources.Count) sets for game $gameId at:"
	Write-Host $stagePath
	foreach ($setSource in ($setSources | Sort-Object Name)) {
		Write-Host ("  {0} -> Sets\{1}" -f $setSource.Name, $setSource.Id)
	}

	if ($StageOnly) {
		Write-Host 'Staging only; the OCTGN builder was not run.'
		return
	}

	if ([string]::IsNullOrWhiteSpace($BuilderPath)) {
		if ([string]::IsNullOrWhiteSpace($env:LOCALAPPDATA)) {
			throw 'Set -BuilderPath to o8build.exe; LOCALAPPDATA is not set.'
		}
		$BuilderPath = Join-Path $env:LOCALAPPDATA 'Programs\OCTGN\o8build.exe'
	}
	if (-not (Test-Path -LiteralPath $BuilderPath -PathType Leaf)) {
		throw "OCTGN builder not found at '$BuilderPath'. The staged game is preserved at '$stagePath'. Specify -BuilderPath."
	}

	$builderArguments = @('-d', $stagePath)
	if ($ValidateOnly) {
		$builderArguments += '-v'
	}
	elseif ($Install) {
		$builderArguments += '-i'
	}

	Write-Host "Running o8build.exe $($builderArguments -join ' ')"
	& $BuilderPath @builderArguments
	if ($LASTEXITCODE -ne 0) {
		throw "o8build.exe exited with code $LASTEXITCODE. The staged game is preserved at '$stagePath'."
	}

	$packages = @(Get-ChildItem -LiteralPath $stagePath -Filter '*.nupkg' -File -Recurse)
	if ($packages.Count -gt 0) {
		Write-Host 'Built package(s):'
		$packages | ForEach-Object { Write-Host $_.FullName }
	}
	else {
		Write-Host "Build completed. Inspect the output and artifacts under '$stagePath'."
	}
}
catch {
	if (Test-Path -LiteralPath $stagePath -PathType Container) {
		Write-Host "Staging directory preserved at: $stagePath"
	}
	throw
}
