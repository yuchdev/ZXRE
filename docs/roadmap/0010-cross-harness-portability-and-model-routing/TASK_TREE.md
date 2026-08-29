# 0010 Task Tree

```text
0010 Cross-Harness Portability and Model Routing
├── 10.0 Harness-Neutral Workflow Contract
│   ├── 01 Define harness-neutral workflow model
│   ├── 02 Define harness capability model
│   ├── 03 Define portable decision/result schemas
│   ├── 04 Define portable context bundle
│   ├── 05 Define workflow checkpoint and handoff semantics
│   ├── 06 Implement harness adapter protocol
│   ├── 07 Add Claude adapter over existing Milestone 0006 assets
│   ├── 08 Add workflow portability conformance tests
│   └── 09 Document portable workflow contract
├── 10.1 Second Agent Harness Integration
│   ├── 01 Select and record the second reference harness
│   ├── 02 Implement second-harness adapter descriptor
│   ├── 03 Create harness-specific project instruction adapter
│   ├── 04 Configure ZXRE MCP for the second harness
│   ├── 05 Map canonical procedures and roles
│   ├── 06 Implement second-harness diagnostic capture
│   ├── 07 Run bounded investigation from existing project state
│   ├── 08 Verify canonical result equivalence
│   └── 09 Document second-harness setup and limitations
├── 10.2 Portable Skill/Procedure Packaging
│   ├── 01 Define canonical procedure schema
│   ├── 02 Create canonical procedure source tree
│   ├── 03 Implement Claude Skill renderer
│   ├── 04 Implement second-harness procedure renderer
│   ├── 05 Implement procedure portability linter
│   ├── 06 Implement procedure versioning
│   ├── 07 Add procedure equivalence tests
│   ├── 08 Migrate Milestone 0006/0008 Skills to canonical procedures
│   └── 09 Document portable procedure authoring
├── 10.3 External Debugger/MCP Adapter Metadata
│   ├── 01 Version companion integration schema
│   ├── 02 Formalize generic capability mapping
│   ├── 03 Model companion lifecycle/connection metadata
│   ├── 04 Model provenance/canonicalization metadata
│   ├── 05 Validate zesarux-mcp reference descriptor
│   ├── 06 Add non-ZEsarUX reference descriptor fixture
│   ├── 07 Expose descriptors to both harness adapters
│   ├── 08 Add schema compatibility/migration tests
│   └── 09 Document companion descriptor schema
├── 10.4 Model Capability and Cost Routing
│   ├── 01 Define model/task capability schema
│   ├── 02 Define routing request/result model
│   ├── 03 Implement configurable model registry
│   ├── 04 Implement deterministic routing policy
│   ├── 05 Implement harness-native model mapping
│   ├── 06 Implement budget accounting
│   ├── 07 Implement routing telemetry
│   ├── 08 Add fake model/provider fixtures
│   ├── 09 Add route-model MCP resource/tool
│   └── 10 Document model routing
├── 10.5 Multi-Agent Review Strategies
│   ├── 01 Define review-strategy model
│   ├── 02 Implement independent-analysis strategy
│   ├── 03 Implement reciprocal-critic strategy
│   ├── 04 Implement moderator/synthesis strategy
│   ├── 05 Implement diversity and duplicate detection
│   ├── 06 Integrate evidence/policy evaluation
│   ├── 07 Add collaboration budgets
│   ├── 08 Create multi-agent-review Skill
│   ├── 09 Add adversarial review regression scenario
│   └── 10 Document collaboration strategies
└── 10.6 Cross-Harness and Companion-Tool Regression Scenarios
    ├── 01 Define portability benchmark model
    ├── 02 Select benchmark scenarios
    ├── 03 Implement canonical project reset/clone helper
    ├── 04 Implement harness run manifest
    ├── 05 Implement canonical result comparator
    ├── 06 Collect portability metrics
    ├── 07 Add with/without companion variants
    ├── 08 Generate benchmark report
    ├── 09 Add manual/CI benchmark profiles
    └── 10 Document portability benchmark
```
