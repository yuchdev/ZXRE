# Task 10.1 - Second Agent Harness Integration

## Story

Integrate one additional MCP-capable coding/agent harness and reproduce a bounded ZXRE investigation
on the same project state. Codex is the preferred reference if its current integration surface
supports the required MCP/project instructions; otherwise use Copilot or another available harness
and record the selection rationale.  The implementation must verify current harness configuration
syntax at implementation time rather than inventing stale config keys.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Select and record the second reference harness | [01-select-and-record-the-second-reference-harness.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.1-second-agent-harness-integration/01-select-and-record-the-second-reference-harness.md) | ⬜ Not started |
| 02 | Implement second-harness adapter descriptor | [02-implement-second-harness-adapter-descriptor.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.1-second-agent-harness-integration/02-implement-second-harness-adapter-descriptor.md) | ⬜ Not started |
| 03 | Create harness-specific project instruction adapter | [03-create-harness-specific-project-instruction-adapter.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.1-second-agent-harness-integration/03-create-harness-specific-project-instruction-adapter.md) | ⬜ Not started |
| 04 | Configure ZXRE MCP for the second harness | [04-configure-zxre-mcp-for-the-second-harness.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.1-second-agent-harness-integration/04-configure-zxre-mcp-for-the-second-harness.md) | ⬜ Not started |
| 05 | Map canonical procedures and roles | [05-map-canonical-procedures-and-roles.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.1-second-agent-harness-integration/05-map-canonical-procedures-and-roles.md) | ⬜ Not started |
| 06 | Implement second-harness diagnostic capture | [06-implement-second-harness-diagnostic-capture.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.1-second-agent-harness-integration/06-implement-second-harness-diagnostic-capture.md) | ⬜ Not started |
| 07 | Run bounded investigation from existing project state | [07-run-bounded-investigation-from-existing-project-state.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.1-second-agent-harness-integration/07-run-bounded-investigation-from-existing-project-state.md) | ⬜ Not started |
| 08 | Verify canonical result equivalence | [08-verify-canonical-result-equivalence.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.1-second-agent-harness-integration/08-verify-canonical-result-equivalence.md) | ⬜ Not started |
| 09 | Document second-harness setup and limitations | [09-document-second-harness-setup-and-limitations.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.1-second-agent-harness-integration/09-document-second-harness-setup-and-limitations.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is clear.
- Read the milestone [plan.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/plan.md), this README and the selected
  subtask before implementation.
- Generalize only from concrete requirements demonstrated by supported harnesses/platforms.
- Preserve explicit capability discovery and graceful degradation where implementations differ.
- Canonical correctness is measured from ZXRE project state and deterministic verification, not
  harness prose or external-tool convenience.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task output is proven against the concrete
implementations selected by the milestone rather than hypothetical future integrations.
