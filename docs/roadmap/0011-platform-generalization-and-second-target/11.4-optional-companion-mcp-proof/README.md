# Task 11.4 - Optional Companion MCP Proof

## Story

Prove that optional low-level debugger MCP integration is generic. If a suitable VICE/C64 MCP exists
and is maintainable at implementation time, describe/integrate it through the companion schema. If
not, use a tiny reference/mock companion server or descriptor to prove the architecture without
inventing a production dependency.  ZXRE's C64 workflow must remain complete without the companion.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Search/verify suitable second-target companion at implementation time | [01-search-verify-suitable-second-target-companion-at-implementation-time.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.4-optional-companion-mcp-proof/01-search-verify-suitable-second-target-companion-at-implementation-time.md) | ⬜ Not started |
| 02 | Create C64 companion descriptor | [02-create-c64-companion-descriptor.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.4-optional-companion-mcp-proof/02-create-c64-companion-descriptor.md) | ⬜ Not started |
| 03 | Create minimal reference companion server if needed | [03-create-minimal-reference-companion-server-if-needed.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.4-optional-companion-mcp-proof/03-create-minimal-reference-companion-server-if-needed.md) | ⬜ Not started |
| 04 | Add second-harness/Claude companion configuration examples | [04-add-second-harness-claude-companion-configuration-examples.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.4-optional-companion-mcp-proof/04-add-second-harness-claude-companion-configuration-examples.md) | ⬜ Not started |
| 05 | Validate exploratory import/canonicalization | [05-validate-exploratory-import-canonicalization.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.4-optional-companion-mcp-proof/05-validate-exploratory-import-canonicalization.md) | ⬜ Not started |
| 06 | Verify procedures remain companion-neutral | [06-verify-procedures-remain-companion-neutral.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.4-optional-companion-mcp-proof/06-verify-procedures-remain-companion-neutral.md) | ⬜ Not started |
| 07 | Add companion absence regression test | [07-add-companion-absence-regression-test.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.4-optional-companion-mcp-proof/07-add-companion-absence-regression-test.md) | ⬜ Not started |
| 08 | Document companion proof result | [08-document-companion-proof-result.md](/docs/roadmap/0011-platform-generalization-and-second-target/11.4-optional-companion-mcp-proof/08-document-companion-proof-result.md) | ⬜ Not started |

## Execution guidance

- Execute subtasks in listed order unless safe parallel work is clear.
- Read the milestone [plan.md](/docs/roadmap/0011-platform-generalization-and-second-target/plan.md), this README and the selected
  subtask before implementation.
- Generalize only from concrete requirements demonstrated by supported harnesses/platforms.
- Preserve explicit capability discovery and graceful degradation where implementations differ.
- Canonical correctness is measured from ZXRE project state and deterministic verification, not
  harness prose or external-tool convenience.

## Task completion criteria

All subtasks are complete, tests/docs are present, and the task output is proven against the concrete
implementations selected by the milestone rather than hypothetical future integrations.
