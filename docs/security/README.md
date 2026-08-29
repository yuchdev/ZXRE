# Security

Threat models, security review outputs, and posture documentation for ZXRE.

The `security-auditor` agent owns this directory. Every change touching auth,
secrets, external integrations, or untrusted-input ingestion triggers a security
review whose output is stored here.

## Naming convention

`threat-model-<scope>.md` for threat models, `review-<scope>-<YYYY-MM-DD>.md`
for point-in-time reviews.

## What a threat model must contain

1. **Scope** - which components and trust boundaries are in scope.
2. **Assets** - what secrets, PII, and data are handled.
3. **Threat actors** - attacker profiles considered.
4. **STRIDE analysis** - Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation.
5. **Mitigations** - existing controls and open gaps.
6. **Verdict** - CRITICAL (merge blocked) / HIGH / MEDIUM / LOW / INFO.

## Security rules (non-negotiable)

- Never log secrets; rely on this project's log-redaction mechanism (if any)
  and verify it covers new sinks.
- Never hard-code credentials. Read from settings/env.
- Treat all untrusted external input as sensitive - no unredacted raw input
  in logs, exceptions, stored reports, or API error bodies.
- Untrusted input must never reach a shell, SQL string, `eval`, or an AI
  prompt without sanitization/parameterization.

## Draft threat model - ZXRE ingestion and agent boundary

> **SME REVIEW NEEDED (AI-drafted - verify before relying on this):**
>
> Drafted from `docs/roadmap/` specifications, not from running code. As of this writing
> `src/zxre/` contains only `__init__.py`, `__main__.py` and `cli.py`, so nothing below is
> yet implemented; treat this as the shape to verify against as each milestone lands.
>
> **1. Scope.** Two trust boundaries. (a) *Ingestion*: user-supplied files and external
> tool/emulator output entering the deterministic pipeline - `src/zxre/tape/`,
> `src/zxre/basic/`, `src/zxre/snapshots/`, `src/zxre/memory/`,
> `src/zxre/adapters/skoolkit/`, `src/zxre/adapters/zesarux/`. (b) *Agent boundary*: the
> `zxre-mcp` stdio server (`src/zxre/mcp/`), its tool and resource surface, and optional
> companion debugger MCPs reached through `src/zxre/integrations/debugger/`. Out of scope:
> the emulator and SkoolKit themselves, and the LLM harness.
>
> **2. Assets.** No credentials or PII in the classic sense. What matters here is:
> third-party copyrighted ZX Spectrum software (`.tap`/`.tzx`/`.z80` inputs and every
> derivative - extracted CODE blocks, memory images, generated assembler); the integrity of
> the artifact store and its `ProvenanceRecord` chain; the correctness of confirmed project
> knowledge (evidence, hypothesis lifecycle, promotion audit log in `src/zxre/policy/`); the
> user's host filesystem and process environment, reachable via external-tool discovery,
> temp paths and MCP host-file operations; and ZEsarUX host/port plus process launch config.
>
> **3. Threat actors.** A malicious or malformed tape/snapshot file (the realistic case -
> ZXRE is pointed at arbitrary vintage binaries of unknown provenance); a hostile or buggy
> emulator/companion-MCP endpoint on the other end of a socket; and the LLM agent itself as
> a confused deputy, driving MCP tools toward paths or mutations the user did not intend.
>
> **4. STRIDE (initial).**
> - *Spoofing*: a companion debugger MCP asserting observations as if they were canonical
>   ZXRE evidence. Mitigated by the Task 06.3 rule that external observations stay
>   exploratory until imported and reproduced through ZXRE.
> - *Tampering*: artifact or provenance records mutated out-of-band, breaking
>   reproducibility. Content addressing (SHA-256) plus Task 01.2's integrity verification is
>   the intended control.
> - *Repudiation*: a confirmed semantic claim whose evidence chain no longer explains it.
>   The promotion audit log is the control; it must be append-only.
> - *Information disclosure*: copyrighted payload bytes, host paths or discovered tool
>   locations leaking into logs, exception messages, generated reports or agent context.
> - *Denial of service*: hostile length prefixes and pathological structures in TAP/TZX,
>   unbounded execution traces, and oversized MCP resource payloads. Bounded retrieval,
>   streaming JSONL and Task 06.2 Subtask 07 pagination are the intended controls.
> - *Elevation of privilege*: the highest-value target - reaching confirmed project state
>   without passing `src/zxre/policy/`, or escaping the project root via MCP host-file
>   operations or external command execution. `src/zxre/mcp/tools/policy.py` is specified to
>   enforce allowed project roots, mutation policy, bounded host-file operations and no
>   arbitrary external command execution.
>
> **5. Mitigations and open gaps.** Specified controls: argv built without shell
> interpolation and deterministic executable discovery in the SkoolKit adapter; the
> deliberately restricted `src/zxre/basic/evaluator.py`, which must never execute arbitrary
> BASIC, `PEEK`, `IN` or user input; explicit truncation and impossible-length validation in
> the tape parsers; temp-file cleanup on success *and* failure; stdout reserved for MCP
> protocol with logs to stderr. Open gaps: no implementation exists to audit yet; no
> log-redaction utility is defined anywhere in the repository; no dependency-audit or
> secret-scanning step appears in the roadmap's quality gates; and the legal handling of
> user-supplied commercial software is addressed only for test fixtures (Task 06.8 Subtask
> 01 requires a synthetic, legally clean fixture), not for user projects.
>
> **6. Verdict.** INFO - no exploitable surface exists in the current scaffold. Re-run this
> model as a real review at Milestone 0002 (first untrusted-file parsing) and again at
> Milestone 0006 (first agent-driven mutation surface).
