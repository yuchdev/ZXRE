# Task 10.4 - Model Capability and Cost Routing

## Story

Introduce transparent model-routing policy for semantic tasks such as summarization, difficult
reasoning, visual asset analysis and critic review. Routing must be driven by task requirements,
configured model capabilities and budgets; deterministic ZXRE operations remain independent of model
provider.  The routing layer should work as recommendation/selection metadata even when the harness,
rather than ZXRE, performs the actual model invocation.

## Subtasks

| Subtask | Name | Spec | Status |
|---|---|---|---|
| 01 | Define model/task capability schema | [01-define-model-task-capability-schema.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.4-model-capability-and-cost-routing/01-define-model-task-capability-schema.md) | ⬜ Not started |
| 02 | Define routing request/result model | [02-define-routing-request-result-model.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.4-model-capability-and-cost-routing/02-define-routing-request-result-model.md) | ⬜ Not started |
| 03 | Implement configurable model registry | [03-implement-configurable-model-registry.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.4-model-capability-and-cost-routing/03-implement-configurable-model-registry.md) | ⬜ Not started |
| 04 | Implement deterministic routing policy | [04-implement-deterministic-routing-policy.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.4-model-capability-and-cost-routing/04-implement-deterministic-routing-policy.md) | ⬜ Not started |
| 05 | Implement harness-native model mapping | [05-implement-harness-native-model-mapping.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.4-model-capability-and-cost-routing/05-implement-harness-native-model-mapping.md) | ⬜ Not started |
| 06 | Implement budget accounting | [06-implement-budget-accounting.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.4-model-capability-and-cost-routing/06-implement-budget-accounting.md) | ⬜ Not started |
| 07 | Implement routing telemetry | [07-implement-routing-telemetry.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.4-model-capability-and-cost-routing/07-implement-routing-telemetry.md) | ⬜ Not started |
| 08 | Add fake model/provider fixtures | [08-add-fake-model-provider-fixtures.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.4-model-capability-and-cost-routing/08-add-fake-model-provider-fixtures.md) | ⬜ Not started |
| 09 | Add route-model MCP resource/tool | [09-add-route-model-mcp-resource-tool.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.4-model-capability-and-cost-routing/09-add-route-model-mcp-resource-tool.md) | ⬜ Not started |
| 10 | Document model routing | [10-document-model-routing.md](/docs/roadmap/0010-cross-harness-portability-and-model-routing/10.4-model-capability-and-cost-routing/10-document-model-routing.md) | ⬜ Not started |

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
