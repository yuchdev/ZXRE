# 0011 Task Tree

```text
0011 Platform Generalization and Second Target
├── 11.0 Architecture Extraction Review
│   ├── 01 Select the constrained second target
│   ├── 02 Create architecture dependency inventory
│   ├── 03 Classify coupling findings
│   ├── 04 Audit project/artifact/knowledge layers
│   ├── 05 Audit static-analysis/reconstruction layers
│   ├── 06 Audit runtime/input/display layers
│   ├── 07 Audit Skills/agents/documentation
│   ├── 08 Create constrained refactoring RFC
│   └── 09 Add architecture leakage regression checks
├── 11.1 Machine/CPU Plugin Boundary
│   ├── 01 Refine architecture descriptor model
│   ├── 02 Move Z80 metadata into architecture plugin
│   ├── 03 Define address-space and memory-view model
│   ├── 04 Refine platform descriptor/plugin protocol
│   ├── 05 Define CPU decoder backend registration by architecture
│   ├── 06 Define source/assembler dialect selection by architecture/platform
│   ├── 07 Refine snapshot/memory materializer registry
│   ├── 08 Refine input/display plugin descriptors
│   ├── 09 Add dual-plugin fake conformance tests
│   └── 10 Document machine/CPU plugin boundary
├── 11.2 Runtime Debugger/Emulator Plugin Boundary
│   ├── 01 Re-run runtime contract against second-target requirements
│   ├── 02 Refine register/state representation
│   ├── 03 Refine memory-view/runtime access APIs
│   ├── 04 Refine breakpoint/watchpoint capability details
│   ├── 05 Refine trace/coverage capability details
│   ├── 06 Refine screenshot/input capability details
│   ├── 07 Create second-backend contract test harness
│   ├── 08 Run ZEsarUX regression after contract changes
│   └── 09 Document runtime plugin refinements
├── 11.3 Second Target Adapter
│   ├── 01 Implement MOS 6510 architecture descriptor
│   ├── 02 Implement C64 platform descriptor
│   ├── 03 Implement PRG input parser/importer
│   ├── 04 Implement minimal CBM BASIC SYS loader decoding where present
│   ├── 05 Implement 6510/6502 disassembly backend
│   ├── 06 Implement C64 reconstruction dialect/assembler adapter
│   ├── 07 Implement VICE runtime adapter
│   ├── 08 Implement C64 logical input mapping
│   ├── 09 Implement basic C64 display/screen capture path
│   ├── 10 Create legal synthetic C64 fixture
│   ├── 11 Add end-to-end C64 deterministic pipeline test
│   └── 12 Document C64 reference adapter
├── 11.4 Optional Companion MCP Proof
│   ├── 01 Search/verify suitable second-target companion at implementation time
│   ├── 02 Create C64 companion descriptor
│   ├── 03 Create minimal reference companion server if needed
│   ├── 04 Add second-harness/Claude companion configuration examples
│   ├── 05 Validate exploratory import/canonicalization
│   ├── 06 Verify procedures remain companion-neutral
│   ├── 07 Add companion absence regression test
│   └── 08 Document companion proof result
├── 11.5 Agent Procedure Portability Review
│   ├── 01 Create procedure portability matrix
│   ├── 02 Review loader/media procedures
│   ├── 03 Review routine/static-analysis procedures
│   ├── 04 Review runtime/causal procedures
│   ├── 05 Review graphics/asset procedures
│   ├── 06 Review role definitions
│   ├── 07 Implement procedure selection by platform
│   ├── 08 Add cross-platform procedure lint/tests
│   └── 09 Document procedure taxonomy
└── 11.6 Cross-Platform Reconstruction Benchmark
    ├── 01 Define cross-platform benchmark schema
    ├── 02 Prepare matched ZX and C64 synthetic fixtures
    ├── 03 Benchmark deterministic ingestion/loading
    ├── 04 Benchmark static analysis/reconstruction
    ├── 05 Benchmark runtime evidence
    ├── 06 Benchmark semantic hypothesis workflow
    ├── 07 Benchmark portable procedures/harnesses
    ├── 08 Compare architecture-specific code footprint
    ├── 09 Generate cross-platform benchmark report
    ├── 10 Add regression/CI profiles
    └── 11 Finalize generalization documentation
```
