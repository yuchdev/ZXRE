# Milestone 0006 Task Tree

```text
0006 MCP Interface and Claude-First Agent Harness
├── 06.0 ZXRE MCP Server Foundation
│   ├── 01 Select MCP SDK and define server package layout
│   ├── 02 Define MCP server configuration
│   ├── 03 Implement stdio server entry point
│   ├── 04 Implement project-context resolver
│   ├── 05 Define MCP error mapping
│   ├── 06 Define common result/serialization helpers
│   ├── 07 Add server lifecycle and graceful shutdown tests
│   └── 08 Document MCP server architecture
├── 06.1 Project-Aware Deterministic Tool Surface
│   ├── 01 Define MCP tool naming and schema conventions
│   ├── 02 Implement project and artifact tools
│   ├── 03 Implement tape and loader tools
│   ├── 04 Implement snapshot and memory tools
│   ├── 05 Implement static-analysis and reconstruction tools
│   ├── 06 Implement runtime and trace tools
│   ├── 07 Implement evidence, hypothesis, experiment and frontier tools
│   ├── 08 Add tool authorization/safety boundaries
│   ├── 09 Add MCP tool contract tests
│   └── 10 Document tool catalog
├── 06.2 MCP Resource Surface
│   ├── 01 Define resource URI scheme
│   ├── 02 Implement project summary resource
│   ├── 03 Implement memory-map and static-analysis resources
│   ├── 04 Implement knowledge/evidence/hypothesis resources
│   ├── 05 Implement trace and experiment resources
│   ├── 06 Implement runtime capability resource
│   ├── 07 Implement resource size limits and pagination
│   ├── 08 Add stale-source/version indicators
│   ├── 09 Add resource contract tests
│   └── 10 Document MCP resource catalog
├── 06.3 External-Tool Capability and Provenance Rules
│   ├── 01 Expose companion integration descriptors through ZXRE
│   ├── 02 Define canonicalization status model
│   ├── 03 Implement external observation import tool
│   ├── 04 Implement reproduce-through-ZXRE workflow helper
│   ├── 05 Define Skills-facing preference rules
│   ├── 06 Add zesarux-mcp mapping verification tests
│   ├── 07 Add generic second-companion fixture
│   └── 08 Document provenance boundary
├── 06.4 Claude Project Instructions and Guardrails
│   ├── 01 Create root CLAUDE.md
│   ├── 02 Define epistemic guardrails section
│   ├── 03 Define runtime/debugger guardrails
│   ├── 04 Define context-efficiency rules
│   ├── 05 Define verification-before-write rules
│   ├── 06 Define repository modification rules
│   ├── 07 Add Claude instruction lint/check
│   └── 08 Document Claude adapter status
├── 06.5 Core Analysis Skills
│   ├── 01 Establish Skill packaging convention
│   ├── 02 Create analyze-tape-loader Skill
│   ├── 03 Create locate-real-entry-point Skill
│   ├── 04 Create analyze-routine Skill
│   ├── 05 Create classify-code-data Skill
│   ├── 06 Create test-variable-hypothesis Skill
│   ├── 07 Create reconstruct-and-verify Skill
│   ├── 08 Create hypothesis-review Skill
│   ├── 09 Add Skill validation tests
│   └── 10 Document Skill authoring guidelines
├── 06.6 Role-Based Agents
│   ├── 01 Define canonical agent-role schema
│   ├── 02 Create Investigator role
│   ├── 03 Create Loader Analyst role
│   ├── 04 Create Static Analyst role
│   ├── 05 Create Dynamic Analyst role
│   ├── 06 Create Asset Analyst role
│   ├── 07 Create Reconstruction Agent role
│   ├── 08 Create Critic/Verifier role
│   ├── 09 Create Claude Code agent adapters
│   ├── 10 Add agent-role conformance tests
│   └── 11 Document multi-agent collaboration pattern
├── 06.7 Optional Companion MCP Configuration
│   ├── 01 Define companion-MCP examples directory
│   ├── 02 Create Claude Code dual-MCP example
│   ├── 03 Create second-harness conceptual example
│   ├── 04 Document shared-emulator lifecycle rules
│   ├── 05 Define agent usage rules for companion MCP
│   ├── 06 Add configuration validation script where practical
│   ├── 07 Add fake alternative companion example
│   └── 08 Document troubleshooting
└── 06.8 Guided End-to-End Investigation
    ├── 01 Define legal deterministic investigation fixture
    ├── 02 Define investigation goal and acceptance contract
    ├── 03 Create initial project setup script
    ├── 04 Create guided investigation procedure
    ├── 05 Run canonical evidence workflow
    ├── 06 Require critic review and promotion evaluation
    ├── 07 Verify result against fixture ground truth
    ├── 08 Add optional companion-MCP variant
    ├── 09 Record cost/context/tool-use diagnostics
    └── 10 Document Milestone 0006 demo
```
