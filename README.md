# Final Fantasy TCG for OCTGN

This folder contains the unpackaged OCTGN game definition, card data, and assets.

## Contents

- `definition.xml` defines the game and references its scripts, images, sounds, markers, and proxy-card templates.
- `Sets/` contains card sets. Each set folder has a `set.xml` and an empty `Cards/` folder.
- `Decks/` contains pre-built decks; these are useful examples and are not required by the game definition itself.
- `scripts/` contains the Python game, card, power, search, and rules logic.
- `resources/` contains card and board images, icons, and sounds.
- `proxy/` contains proxy-card templates and their definitions.

## Card Ability Data

Keep the four ability-related properties on each card consistent:

- `Abilities` is rich text for the card's ordinary printed rules text, such as keywords, triggered abilities, and static effects. Preserve OCTGN markup such as `<b>`, `<i>`, and `<s value="...">` for styling and symbols.
- `SpecialAbilities` is rich text for named, costed Special actions shown separately from the ordinary rules text. Keep the action name, Special symbol, CP symbols, and effect together, in display order.
- `AbilitiesContainer` is script data, not player-facing prose. It contains the automation entries recognized by the game scripts, separated by `][`. For each Special action exposed as a clickable card action, add the matching `SpecialAbility1`, `SpecialAbility2`, or `SpecialAbility3` entry in the same order as `SpecialAbilities`; keep its name and cost consistent with the displayed action. Do not invent entries for unsupported effects: ordinary rules text can exist without automation.
- `EXBurst` is the string `TRUE` or `FALSE` and controls whether a card triggers EX Burst handling when revealed from the Damage Zone. Set it to `TRUE` for an EX Burst card and `FALSE` otherwise. In `Abilities`, mark the printed keyword with `<s value="EXBurst">EX Burst</s>`; the flag does not depend on whether the effect is automated.

### Mapping Rules

Treat `Abilities` as the source for deciding which `AbilitiesContainer` entries are appropriate, not as a template to copy into the container. For each distinct ability, add an entry only when an existing script handler matches its trigger, timing, costs, conditions, targets, and supported action. Use the handler's expected syntax and delimit multiple entries with `][`.

The mapping is not one-to-one: one text ability may need multiple supported entries, and a text ability may have no matching handler. In the latter case, leave it in `Abilities` and omit the unsupported container entry rather than guessing. `SearchForCardN` and `RevealCardsN` expose helper actions; `SpecialAbilityN` exposes the Special name and activation cost but does not resolve its effect. Keep Special text in `SpecialAbilities`, with any matching `SpecialAbilityN` entry in the same order. Only add other automation entries when the scripts support the described effect.

The legacy EX Burst marker/flag mismatches and missing clickable Special entries identified in the set files have been corrected. Continue checking these relationships when adding or editing cards, and avoid copying older data patterns without verifying them.

## Build

OCTGN's `o8build.exe` validates and builds the game package. From PowerShell, run this from the repository root to build from a temporary staging copy:

```powershell
$source = Join-Path (Get-Location).Path '285a8cdb-1d02-4edd-a9de-1ade9d5a4f43'
$build = Join-Path $env:TEMP ("FFTCG-OCTGN-" + [guid]::NewGuid())
New-Item -ItemType Directory -Path $build | Out-Null
Get-ChildItem -LiteralPath $source | Copy-Item -Destination $build -Recurse
Write-Host "Building in $build"
& "$env:LOCALAPPDATA\Programs\OCTGN\o8build.exe" -d $build
```

The builder validates the staged game and writes a versioned `.nupkg` package into the staging folder shown in the output. Add `-v` to validate without building, `-i` to install the built package into OCTGN's local feed, or `-?` to display the command-line options.

The `.nupkg` is the builder's feed package; it is not an `.o8g` file. Do not rename the package to `.o8g`.

## Build An Image Pack

Run the following in PowerShell from the repository root. It copies the selected sets' base card images from the game folder into a temporary staging tree and creates an `.o8c` ZIP archive in your temporary directory. The originals are not moved or modified. Edit `$setIds` to include additional sets; the default is Opus 30.

```powershell
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$source = Join-Path (Get-Location).Path '285a8cdb-1d02-4edd-a9de-1ade9d5a4f43'
$definition = [xml](Get-Content -LiteralPath (Join-Path $source 'definition.xml') -Raw)
$gameId = [guid]::Parse($definition.game.id).ToString()
$setIds = @('a7c829e2-247e-4d85-9c2e-8ff3dfd84d37')
$buildId = [guid]::NewGuid().ToString()
$stage = Join-Path $env:TEMP "FFTCG-images-$buildId"
$output = Join-Path $env:TEMP "FFTCG-images-$buildId.o8c"
$archive = $null
try {
	New-Item -ItemType Directory -Path $stage | Out-Null
	foreach ($setId in $setIds) {
		$setId = [guid]::Parse($setId).ToString()
		$setPath = Join-Path $source "Sets/$setId"
		$set = [xml](Get-Content -LiteralPath (Join-Path $setPath 'set.xml') -Raw)
		if ($set.set.id -ne $setId -or $set.set.gameId -ne $gameId) {
			throw "Set/game UUID mismatch: $setId"
		}
		$cardIds = @($set.set.cards.card | ForEach-Object { $_.id })
		$images = @(Get-ChildItem -LiteralPath (Join-Path $setPath 'Cards') -File |
			Where-Object { $_.Extension.ToLowerInvariant() -in @('.jpg', '.jpeg', '.png') })
		if ($images.Count -eq 0) { throw "No card images found: $setId" }
		$target = Join-Path $stage "$gameId/Sets/$setId/Cards"
		New-Item -ItemType Directory -Path $target | Out-Null
		foreach ($image in $images) {
			if ($image.BaseName -notin $cardIds) {
				throw "Image filename does not match a card UUID: $($image.Name)"
			}
			Copy-Item -LiteralPath $image.FullName -Destination $target
		}
	}
	$archive = [System.IO.Compression.ZipFile]::Open($output, 'Create')
	foreach ($image in Get-ChildItem -LiteralPath $stage -File -Recurse) {
		$entry = $image.FullName.Substring($stage.Length + 1).Replace('\', '/')
		[void][System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile(
			$archive, $image.FullName, $entry, 'Optimal')
	}
} finally {
	if ($null -ne $archive) { $archive.Dispose() }
	if (Test-Path -LiteralPath $stage) { Remove-Item -LiteralPath $stage -Recurse -Force }
}
Write-Host "Image pack: $output"
```

The archive contains only `<game UUID>/Sets/<set UUID>/Cards/<card UUID>.<extension>`, with no manifest or enclosing staging folder. This example handles base images only, not alternate faces or `Crops/`. Install the matching game package first, then use OCTGN's **Install Image Packs** action to select the `.o8c`.

For separate releases, exclude optional collectible artwork from the game-build staging copy before running `o8build`, which otherwise includes it recursively. Keep referenced resources (card backs, default fronts, proxy templates, icons, sounds, boards) and essential synthetic HUD/playmat images in the game package. Do not distribute raw downloads or generated proxy caches in either package. Keep release archives outside the plugin root and preserve game, set, and card UUIDs between code and image releases.
