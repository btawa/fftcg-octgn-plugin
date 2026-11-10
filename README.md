# Final Fantasy TCG for OCTGN

This folder contains the unpackaged OCTGN game definition, card data, and assets.

## Contents

- `definition.xml` defines the game and references its scripts, images, sounds, markers, and proxy-card templates.
- `sets/` contains card sets in human-readable folders. The `set.xml` in each folder is the source of truth for its OCTGN set UUID.
- `tools/Build.ps1` reconstructs the UUID-named `Sets/` tree in a temporary staging copy and runs the OCTGN builder.
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

For every Limit Break card, append ` (LB)` to the imported card name (for example, `Ysayle (LB)`) so it follows the Limit Break deck naming convention. Include `LimitBreak|<cost>` in `AbilitiesContainer` so the game recognizes and moves it to the LB Deck when a deck is loaded; add `AlternateName|<base card name>` (for example, `AlternateName|Ysayle`) to preserve matching with the ordinary card name.

### Mapping Rules

Treat `Abilities` as the source for deciding which `AbilitiesContainer` entries are appropriate; never copy rules text into the container. For each distinct ability, add an entry only when an existing script handler supports its trigger, timing, costs, conditions, targets, and action. Container entries are script data, not a promise that the whole printed effect resolves automatically.

Use these helper mappings when they match the printed ability:

- A deck search, or a single card selected from the Break Zone, uses `SearchForCard1`, `SearchForCard2`, or `SearchForCard3`. The format is `SearchForCardN|<menu label>|Player_<Deck or BreakZone>_<filters>`. Filters are `field,operation,value` triples joined with `AND`. For example, Vivi's “Job Black Mage or Card Name Black Mage” search is `SearchForCard1|Search your Deck for a Job Black Mage or Card Name Black Mage|Player_Deck_NameOrJob,Is,Black Mage`; `NameOrJob` matches either the card name or a job. A Break Zone target can add filters such as `Type,Is,ForwardANDCP,LessThanOrEqualTo,2`. The helper shows matching cards to the player; it does not add, play, or otherwise resolve them.
- Looking at or revealing the top N cards of your deck uses `RevealCards1` or `RevealCards2`, with the format `RevealCardsN|Quantity|<count>|<filters>`. Use `N/A` when no cards need highlighting, for example `RevealCards1|Quantity|2|N/A`. A reveal helper exposes the cards and can highlight matches; adding them to hand, playing them, or moving the rest is still manual unless another handler explicitly implements that action.
- A named Special action uses `SpecialAbility1`, `SpecialAbility2`, or `SpecialAbility3` in the same order as the actions in `SpecialAbilities`. Keep the action name and activation cost consistent. This exposes the clickable action but does not resolve its effect.

One printed ability may need multiple entries: use separate numbered search helpers for distinct alternatives when each has a different filter. Conversely, leave unsupported effects in `Abilities` without a guessed container entry. Delimit multiple entries with `][`. For other entry types, follow the existing handler's expected syntax and add them only when its behavior matches the card.

The legacy EX Burst marker/flag mismatches and missing clickable Special entries identified in the set files have been corrected. Continue checking these relationships when adding or editing cards, and avoid copying older data patterns without verifying them.

## Build

Keep set sources in readable folders under `sets/` (for example, `sets/20-dawn-of-heroes/`). OCTGN still receives the UUID-based `Sets/<UUID>/` layout, generated from each source `set.xml` at build time; do not edit or create a checked-in `Sets/` tree.

Run the build script from the repository root:

```powershell
.\tools\Build.ps1
```

The script validates that set IDs are valid and unique, and that each set belongs to this game. It copies the game files and reconstructs the UUID-named set tree under a unique temporary directory. It includes the Debug set's `Cards/` contents (default card and proxy images) in the game package; images in its source `Cards/Proxies/` folder are placed directly in the staged `Cards/` folder because OCTGN does not allow a `Proxies/` subfolder there. Other sets' card images are omitted so they remain in the separately built image pack. Empty `Cards/` directories are created in staging for OCTGN compatibility. It then invokes `o8build.exe`. The default builder path is `%LOCALAPPDATA%\Programs\OCTGN\o8build.exe`; override it with `-BuilderPath 'C:\path\to\o8build.exe'` if needed.

Use `-ValidateOnly` to validate without building, `-Install` to install the built package into OCTGN's local feed, or `-StageOnly` to create the compatible staging tree without invoking the builder. The staging directory is preserved so you can inspect it and find the generated package; its path is printed by the script.

The `.nupkg` is the builder's feed package; it is not an `.o8g` file. Do not rename the package to `.o8g`.

## Build An Image Pack

Run the following in PowerShell from the repository root to create an `.o8c` archive containing base card images from one or more sets. Use the UUID from each set's `set.xml`; for example, the UUID below selects Opus 30. The source images are not moved or modified, and the archive is written to your temporary directory by default.

```powershell
.\tools\Build-ImagePack.ps1 -SetIds @('a7c829e2-247e-4d85-9c2e-8ff3dfd84d37')
```

Pass additional set UUIDs to include more sets in the same archive. Set names and UUIDs are printed by the regular build script. You can choose an output filename with `-OutputPath`.

```powershell
.\tools\Build-ImagePack.ps1 -SetIds @('a7c829e2-247e-4d85-9c2e-8ff3dfd84d37', 'f02477c1-a755-4f69-9a6c-0f96dd0999b5') -OutputPath "$env:TEMP\FFTCG-images.o8c"
```

The archive contains only `<game UUID>/Sets/<set UUID>/Cards/<card UUID>.<extension>`, with no manifest or enclosing staging folder. This example handles base images only, not alternate faces or `Crops/`. Install the matching game package first, then use OCTGN's **Install Image Packs** action to select the `.o8c`.

For separate releases, exclude optional collectible artwork from the game-build staging copy before running `o8build`, which otherwise includes it recursively. Keep referenced resources (card backs, default fronts, proxy templates, icons, sounds, boards) and essential synthetic HUD/playmat images in the game package. Do not distribute raw downloads or generated proxy caches in either package. Keep release archives outside the plugin root and preserve game, set, and card UUIDs between code and image releases.
