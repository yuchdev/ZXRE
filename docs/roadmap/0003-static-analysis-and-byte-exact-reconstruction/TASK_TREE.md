# Milestone 0003 Task Tree

```text
0003 Static Analysis and Byte-Exact Reconstruction
├── 03.0 Disassembly Backend Integration
│   ├── 01 Define disassembly domain model
│   ├── 02 Define disassembler backend contract
│   ├── 03 Implement built-in Z80 decoder or selected library adapter
│   ├── 04 Implement optional SkoolKit disassembly adapter
│   ├── 05 Implement disassembly service
│   ├── 06 Persist structured disassembly
│   ├── 07 Add backend equivalence regression tests
│   └── 08 Document disassembly architecture
├── 03.1 Code/Data Control Map
│   ├── 01 Define control-map domain model
│   ├── 02 Implement control-map validation and interval operations
│   ├── 03 Generate initial control map from explicit loader/snapshot facts
│   ├── 04 Import/export SkoolKit control files optionally
│   ├── 05 Persist control map
│   ├── 06 Integrate control map with disassembly service
│   ├── 07 Add manual classification service APIs
│   └── 08 Document control-map semantics
├── 03.2 References and Control-Flow Facts
│   ├── 01 Define reference/control-flow domain model
│   ├── 02 Classify Z80 control-flow instructions
│   ├── 03 Extract direct address references
│   ├── 04 Build conservative basic blocks
│   ├── 05 Build routine candidates
│   ├── 06 Persist static reference graph
│   ├── 07 Implement static-analysis query service
│   └── 08 Document static-flow guarantees
├── 03.3 Lossless Assembler Source Generation
│   ├── 01 Define reconstruction/source model
│   ├── 02 Define assembler dialect abstraction
│   ├── 03 Generate deterministic labels for direct targets
│   ├── 04 Render CODE regions
│   ├── 05 Render non-code regions
│   ├── 06 Generate source units and linker/order plan
│   ├── 07 Store generated source as project artifacts
│   └── 08 Document lossless source policy
├── 03.4 Byte-Exact Verification
│   ├── 01 Define assembler backend contract
│   ├── 02 Implement reference assembler adapter
│   ├── 03 Define verification model
│   ├── 04 Implement binary-to-memory mapping for rebuilt output
│   ├── 05 Implement byte-exact comparator
│   ├── 06 Implement reconstruction verification service
│   ├── 07 Add deliberate encoding-ambiguity regression cases
│   ├── 08 Add milestone-level exact rebuild integration test
│   └── 09 Document verification invariant
└── 03.5 Static Analysis Reports
    ├── 01 Define report summary model
    ├── 02 Implement coverage statistics
    ├── 03 Implement static-analysis textual report
    ├── 04 Implement machine-readable report
    ├── 05 Register reports as generated artifacts
    ├── 06 Add report consistency tests
    ├── 07 Add Milestone 0003 inspection command extensions
    └── 08 Update documentation and milestone status
```
