# diagrams/

Single source of truth for every Mermaid diagram in the guide (one `.mmd` file each).

| File | Used in | Type |
|------|---------|------|
| `journey.mmd` | README | flowchart TD |
| `concept-map.mmd` | ch. 01 | mindmap |
| `data-flow.mmd` | ch. 02 | flowchart LR |
| `access-path.mmd` | ch. 03 | flowchart TD |
| `table-relationships.mmd` | ch. 05 | erDiagram |
| `visit-schedule.mmd` | ch. 05 | flowchart LR |
| `phase-timeline.mmd` | ch. 06 | flowchart LR |
| `downloads.mmd` | Download chapter | flowchart TD |
| `cohort.mmd` | Cohort chapter | flowchart TD |
| `publication-workflow.mmd` | ch. 08 | flowchart TD |
| `analysis-pipeline.mmd` | ch. 09 | flowchart TD |
| `pr-lifecycle.mmd` | ch. 12 | flowchart LR |

## Workflow

1. Edit the `.mmd` file.
2. `python scripts/sync_diagrams.py` copies it into every chapter that embeds it (GitHub cannot transclude files).
3. Commit both. CI runs `sync_diagrams.py --check` and renders each file with mermaid-cli.

## House style

- At most ~15 nodes per diagram. Split otherwise.
- No `%%{init}` themes, no `click` callbacks (breaks dark mode and GitHub rendering).
- Light fills with explicit dark text (`color:#1a1a1a`) so diagrams read well in light and dark mode.
- Always add a **Text version** under the embedded diagram for accessibility and search.
- Palette: blue `#dbeafe` info, green `#d4edda` good/outputs, amber `#fff3cd` caution, red `#f8d7da` stop.
