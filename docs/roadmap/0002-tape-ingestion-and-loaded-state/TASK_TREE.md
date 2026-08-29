# Milestone 0002 Task Tree

```text
0002 Tape Ingestion and Loaded Machine State
├── 02.0 Tape Inspection and Block Inventory
│   ├── 01 Define tape domain model
│   ├── 02 Implement TAP parser
│   ├── 03 Implement TZX parser core
│   ├── 04 Normalize standard Spectrum header blocks
│   ├── 05 Implement tape inventory service
│   ├── 06 Implement raw block extraction
│   ├── 07 Persist tape inventory metadata
│   └── 08 Document tape ingestion model
├── 02.1 BASIC Loader Decoding
│   ├── 01 Define BASIC loader domain model
│   ├── 02 Implement Spectrum BASIC token decoder
│   ├── 03 Extract BASIC program payloads from tape inventory
│   ├── 04 Implement loader statement recognizer
│   ├── 05 Implement restricted deterministic expression evaluator
│   ├── 06 Derive candidate loader addresses
│   ├── 07 Persist decoded loader analysis
│   └── 08 Document BASIC loader decoding
├── 02.2 Tape-to-Snapshot Execution
│   ├── 01 Define snapshot domain model
│   ├── 02 Define loader/snapshot backend interface
│   ├── 03 Implement SkoolKit tap2sna adapter
│   ├── 04 Implement snapshot creation service
│   ├── 05 Parse Z80 snapshot metadata needed by ZXRE
│   ├── 06 Validate created snapshot against platform
│   ├── 07 Record reproducible snapshot recipe
│   └── 08 Document snapshot backend architecture
├── 02.3 Snapshot Memory Inspection and Diff
│   ├── 01 Define normalized memory image model
│   ├── 02 Implement snapshot-to-memory materialization
│   ├── 03 Implement memory read APIs
│   ├── 04 Implement memory export
│   ├── 05 Implement byte-level memory diff
│   ├── 06 Implement diff serialization/reporting
│   ├── 07 Integrate memory operations into project service
│   └── 08 Document memory model and diff semantics
└── 02.4 Ingestion Validation Fixtures
    ├── 01 Define fixture policy and directory structure
    ├── 02 Create synthetic TAP fixture builder
    ├── 03 Create synthetic TZX fixture builder
    ├── 04 Create minimal BASIC loader fixture set
    ├── 05 Create deterministic machine-code payload fixtures
    ├── 06 Create snapshot fixtures without copyrighted ROM content
    ├── 07 Add external-backend integration test marker
    ├── 08 Add Milestone 0002 end-to-end acceptance test
    └── 09 Document regression/fixture maintenance
```
