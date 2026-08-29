# Task 10.3 - External Debugger/MCP Adapter Metadata

## Story

Formalize optional companion debugger metadata so agent harnesses can discover that a low-level tool
exists without ZXRE depending on that tool's schema. `zesarux-mcp` remains one reference mapping,
not the definition of memory/step/breakpoint capabilities.  The metadata layer describes external
tools; it does not turn ZXRE into an MCP-to-MCP proxy.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Version companion integration schema | [01-version-companion-integration-schema.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.3-external-debugger-mcp-adapter-metadata/01-version-companion-integration-schema.md) | ⬜ Not started |
| 02 | Formalize generic capability mapping | [02-formalize-generic-capability-mapping.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.3-external-debugger-mcp-adapter-metadata/02-formalize-generic-capability-mapping.md) | ⬜ Not started |
| 03 | Model companion lifecycle/connection metadata | [03-model-companion-lifecycle-connection-metadata.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.3-external-debugger-mcp-adapter-metadata/03-model-companion-lifecycle-connection-metadata.md) | ⬜ Not started |
| 04 | Model provenance/canonicalization metadata | [04-model-provenance-canonicalization-metadata.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.3-external-debugger-mcp-adapter-metadata/04-model-provenance-canonicalization-metadata.md) | ⬜ Not started |
| 05 | Validate zesarux-mcp reference descriptor | [05-validate-zesarux-mcp-reference-descriptor.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.3-external-debugger-mcp-adapter-metadata/05-validate-zesarux-mcp-reference-descriptor.md) | ⬜ Not started |
| 06 | Add non-ZEsarUX reference descriptor fixture | [06-add-non-zesarux-reference-descriptor-fixture.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.3-external-debugger-mcp-adapter-metadata/06-add-non-zesarux-reference-descriptor-fixture.md) | ⬜ Not started |
| 07 | Expose descriptors to both harness adapters | [07-expose-descriptors-to-both-harness-adapters.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.3-external-debugger-mcp-adapter-metadata/07-expose-descriptors-to-both-harness-adapters.md) | ⬜ Not started |
| 08 | Add schema compatibility/migration tests | [08-add-schema-compatibility-migration-tests.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.3-external-debugger-mcp-adapter-metadata/08-add-schema-compatibility-migration-tests.md) | ⬜ Not started |
| 09 | Document companion descriptor schema | [09-document-companion-descriptor-schema.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.3-external-debugger-mcp-adapter-metadata/09-document-companion-descriptor-schema.md) | ⬜ Not started |

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
