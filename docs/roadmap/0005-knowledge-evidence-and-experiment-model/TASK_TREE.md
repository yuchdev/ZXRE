# Milestone 0005 Task Tree

```text
0005 Knowledge, Evidence and Experiment Model
├── 05.0 Knowledge Entities and Relationships
│   ├── 01 Define knowledge entity identifiers and base model
│   ├── 02 Define routine, variable and data-block entities
│   ├── 03 Define asset and concept entities
│   ├── 04 Define typed relationship model
│   ├── 05 Implement knowledge graph store
│   ├── 06 Implement entity merge/alias semantics
│   ├── 07 Integrate static-analysis facts as knowledge references
│   └── 08 Document knowledge model
├── 05.1 Evidence and Provenance
│   ├── 01 Define evidence domain model
│   ├── 02 Define immutable source references
│   ├── 03 Implement evidence store
│   ├── 04 Implement evidence creation helpers for deterministic outputs
│   ├── 05 Implement human assertion evidence
│   ├── 06 Implement external observation evidence
│   ├── 07 Define evidence serialization and integrity checks
│   └── 08 Document evidence semantics
├── 05.2 Hypothesis Lifecycle
│   ├── 01 Define hypothesis domain model
│   ├── 02 Define hypothesis lifecycle state machine
│   ├── 03 Attach supporting and contradicting evidence
│   ├── 04 Implement competing-hypothesis groups
│   ├── 05 Implement hypothesis store and queries
│   ├── 06 Implement supersession and revision history
│   ├── 07 Integrate confirmed hypotheses with knowledge entities
│   └── 08 Document hypothesis lifecycle
├── 05.3 Confidence and Promotion Policy
│   ├── 01 Define evidence grade scale
│   ├── 02 Define claim confidence summary
│   ├── 03 Define promotion rules by hypothesis kind
│   ├── 04 Implement contradiction/blocking rules
│   ├── 05 Implement promotion evaluator
│   ├── 06 Implement controlled promotion transaction
│   ├── 07 Implement policy audit log
│   └── 08 Document confidence/promotion policy
├── 05.4 Experiment Specification and Results
│   ├── 01 Define experiment domain model
│   ├── 02 Define setup and starting-state model
│   ├── 03 Define stimulus/intervention model
│   ├── 04 Define expected discriminator/assertion model
│   ├── 05 Implement experiment runner
│   ├── 06 Implement experiment result serialization
│   ├── 07 Link experiment results to evidence and hypotheses
│   ├── 08 Add deterministic fake-backend experiment tests
│   └── 09 Document experiment model
└── 05.5 Research Frontier Queries
    ├── 01 Define research-frontier model
    ├── 02 Derive open hypothesis frontier items
    ├── 03 Derive static-analysis gap items
    ├── 04 Derive runtime/evidence gap items
    ├── 05 Define deterministic priority signals
    ├── 06 Implement frontier service and filters
    ├── 07 Persist frontier snapshots or regenerate on demand
    ├── 08 Add frontier report and CLI view
    └── 09 Document research-frontier semantics
```
