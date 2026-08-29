# Milestone 0004 Task Tree

```text
0004 Emulator Automation and Runtime Evidence
├── 04.0 Emulator Capability Contract
│   ├── 01 Define runtime capability taxonomy
│   ├── 02 Define runtime session and machine-state models
│   ├── 03 Define emulator/debugger backend protocol
│   ├── 04 Define runtime configuration model
│   ├── 05 Define runtime service facade
│   ├── 06 Add fake deterministic runtime backend for tests
│   ├── 07 Define runtime artifact/provenance conventions
│   └── 08 Document runtime capability contract
├── 04.1 Reference Emulator Adapter
│   ├── 01 Create ZEsarUX adapter package and configuration
│   ├── 02 Implement ZRCP transport client
│   ├── 03 Implement ZRCP command layer
│   ├── 04 Implement optional ZEsarUX process launcher
│   ├── 05 Map ZEsarUX features to runtime capabilities
│   ├── 06 Implement EmulatorBackend adapter
│   ├── 07 Add live ZEsarUX integration test marker
│   └── 08 Document reference adapter
├── 04.2 Breakpoints, Watchpoints and Execution Control
│   ├── 01 Define breakpoint/watchpoint models
│   ├── 02 Implement breakpoint registry/lifecycle
│   ├── 03 Implement ZEsarUX breakpoint mapping
│   ├── 04 Define execution-control request/result models
│   ├── 05 Implement step/step-over semantics
│   ├── 06 Implement bounded run/pause behavior
│   ├── 07 Add breakpoint/watchpoint acceptance tests
│   └── 08 Document execution-control semantics
├── 04.3 Execution, Memory and Coverage Tracing
│   ├── 01 Define trace domain model
│   ├── 02 Implement execution-history capture
│   ├── 03 Implement code-coverage capture
│   ├── 04 Implement memory/I/O transaction-log ingestion
│   ├── 05 Implement trace capture service
│   ├── 06 Serialize traces efficiently
│   ├── 07 Add trace query helpers
│   └── 08 Document trace formats and guarantees
├── 04.4 Reproducible Input Scripting
│   ├── 01 Define input event/scenario model
│   ├── 02 Define ZX Spectrum logical key map
│   ├── 03 Implement input scenario serialization
│   ├── 04 Implement input execution service
│   ├── 05 Implement ZEsarUX key mapping
│   ├── 06 Add deterministic BASIC input scenario fixture
│   ├── 07 Add scenario replay regression tests
│   └── 08 Document input scripting
├── 04.5 Screen and Machine-State Capture
│   ├── 01 Define runtime capture model
│   ├── 02 Implement screen capture service
│   ├── 03 Implement register-state capture
│   ├── 04 Implement RAM/range capture
│   ├── 05 Implement saved-snapshot capture
│   ├── 06 Implement synchronized capture bundle service
│   ├── 07 Add capture consistency tests
│   └── 08 Document capture semantics
├── 04.6 Trace-Assisted Code/Data Refinement
│   ├── 01 Define refinement proposal model
│   ├── 02 Map execution coverage to candidate code bytes
│   ├── 03 Detect control-map conflicts
│   ├── 04 Apply approved refinement proposals
│   ├── 05 Regenerate disassembly/static flow after refinement
│   ├── 06 Add regression scenario
│   ├── 07 Add refinement report
│   └── 08 Document runtime refinement policy
└── 04.7 Optional External Debugger/MCP Bridge
    ├── 01 Define companion debugger descriptor model
    ├── 02 Define capability-mapping metadata
    ├── 03 Create zesarux-mcp companion descriptor
    ├── 04 Define exploratory-vs-canonical provenance policy
    ├── 05 Implement external observation import APIs
    ├── 06 Document dual-MCP development configuration
    ├── 07 Add generic companion integration documentation
    └── 08 Add integration registry tests
```
