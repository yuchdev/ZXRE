# Task 07.3 - Graphics and Asset Analysis

## Story

Turn candidate memory/data regions into inspectable visual assets and evidence. Deterministic
renderers should extract ZX Spectrum screens, bitmap/tile/sprite/font candidates; multimodal models
may then propose semantic classifications, but visual interpretation must be stored as hypotheses
linked to the rendered source artifact and address range.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define asset-analysis model | [01-define-asset-analysis-model.md](/docs/roadmap/0007-assisted-semantic-analysis/07.3-graphics-and-asset-analysis/01-define-asset-analysis-model.md) | ⬜ Not started |
| 02 | Implement ZX Spectrum bitmap/attribute renderer | [02-implement-zx-spectrum-bitmap-attribute-renderer.md](/docs/roadmap/0007-assisted-semantic-analysis/07.3-graphics-and-asset-analysis/02-implement-zx-spectrum-bitmap-attribute-renderer.md) | ⬜ Not started |
| 03 | Implement tile-sheet renderer | [03-implement-tile-sheet-renderer.md](/docs/roadmap/0007-assisted-semantic-analysis/07.3-graphics-and-asset-analysis/03-implement-tile-sheet-renderer.md) | ⬜ Not started |
| 04 | Implement sprite-candidate renderer | [04-implement-sprite-candidate-renderer.md](/docs/roadmap/0007-assisted-semantic-analysis/07.3-graphics-and-asset-analysis/04-implement-sprite-candidate-renderer.md) | ⬜ Not started |
| 05 | Implement font/text-glyph candidate renderer | [05-implement-font-text-glyph-candidate-renderer.md](/docs/roadmap/0007-assisted-semantic-analysis/07.3-graphics-and-asset-analysis/05-implement-font-text-glyph-candidate-renderer.md) | ⬜ Not started |
| 06 | Implement asset rendering service | [06-implement-asset-rendering-service.md](/docs/roadmap/0007-assisted-semantic-analysis/07.3-graphics-and-asset-analysis/06-implement-asset-rendering-service.md) | ⬜ Not started |
| 07 | Implement multimodal semantic proposal interface | [07-implement-multimodal-semantic-proposal-interface.md](/docs/roadmap/0007-assisted-semantic-analysis/07.3-graphics-and-asset-analysis/07-implement-multimodal-semantic-proposal-interface.md) | ⬜ Not started |
| 08 | Extend Asset Analyst workflow | [08-extend-asset-analyst-workflow.md](/docs/roadmap/0007-assisted-semantic-analysis/07.3-graphics-and-asset-analysis/08-extend-asset-analyst-workflow.md) | ⬜ Not started |
| 09 | Expose asset catalog through MCP resources | [09-expose-asset-catalog-through-mcp-resources.md](/docs/roadmap/0007-assisted-semantic-analysis/07.3-graphics-and-asset-analysis/09-expose-asset-catalog-through-mcp-resources.md) | ⬜ Not started |
| 10 | Add synthetic graphics regression fixtures | [10-add-synthetic-graphics-regression-fixtures.md](/docs/roadmap/0007-assisted-semantic-analysis/07.3-graphics-and-asset-analysis/10-add-synthetic-graphics-regression-fixtures.md) | ⬜ Not started |
| 11 | Document graphics/asset workflow | [11-document-graphics-asset-workflow.md](/docs/roadmap/0007-assisted-semantic-analysis/07.3-graphics-and-asset-analysis/11-document-graphics-asset-workflow.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is clear.
- Read the milestone [plan.md](/docs/roadmap/0007-assisted-semantic-analysis/plan.md), this README and
  the selected subtask first.
- Start from deterministic/static/runtime facts and canonical evidence; let agents add interpretation as
  explicit hypotheses.
- Keep confirmed and proposed semantic state visibly distinct in services, MCP resources and reports.
- Do not pre-implement autonomous research loops or semantic source refactoring from later milestones.

## Task completion criteria

All subtasks are complete, tests/docs are present, and semantic outputs are reproducible as canonical
ZXRE hypotheses/knowledge state with evidence and uncertainty preserved.
