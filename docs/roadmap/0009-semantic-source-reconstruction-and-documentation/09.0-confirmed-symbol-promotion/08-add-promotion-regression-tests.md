# Task 09.0 - Confirmed-Symbol Promotion / Subtask 08 - Add promotion regression tests

## Objective

Create integration tests proving unconfirmed proposals cannot enter semantic overlay, confirmed ones
can, mechanical labels remain intact and promotion provenance survives reopen.

## Constraints

- Keep implementation within Milestone 0009 scope.
- The mechanically faithful Milestone 0003 reconstruction remains immutable ground truth.
- Semantic names/comments/modules may use only policy-approved confirmed knowledge unless explicitly
  labeled provisional in documentation; unconfirmed hypotheses must never silently enter confirmed source.
- Every semantic source artifact must retain mapping/provenance back to address ranges, lossless source
  and evidence/policy state.
- Default semantic rebuild acceptance is byte-exact.
- Documentation is generated from canonical stores, not agent conversation prose.
- Do not perform behavior-changing refactors, modern-language decompilation or platform ports.
- Do not package/publish copyrighted game assets as part of generated handoff unless legally permitted.
- Update tests/docs with implementation.

## Completion conditions

- Named files/APIs are implemented.
- Relevant unit/integration tests pass.
- Semantic source can be mapped back to lossless source and verified.
- Generated docs visibly distinguish confirmed, supported/provisional and unresolved state.
- `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src`, and `uv run pytest`
  remain green where applicable.
