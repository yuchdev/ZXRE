# Task 09.1 - Source Module Reconstruction / Subtask 05 - Implement include/source tree renderer

## Objective

Create `src/zxre/semantic_source/render_tree.py`. Produce root `.asm` plus module files/includes
according to selected assembler dialect, preserving deterministic ordering and origin directives.

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
