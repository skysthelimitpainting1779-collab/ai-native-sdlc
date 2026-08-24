---
trigger: always_on
description: AI-Native SDLC rules enforcing artifact-driven development, Graphify knowledge discovery & error memory, Context7 documentation verification, and cyclic feedback.
---

# AI-Native Software Development Lifecycle (SDLC) Directives

## Non-Negotiable Directives

### 1. Graphify Knowledge Graph & Long-Term Error Memory
- **Codebase & Architecture Topology**: Use the official Graphify Knowledge Graph (`graphify-out/graph.json` / MCP / CLI) as the primary source of truth for codebase architecture and call-flows.
- **Learn & Remember Mistakes**:
  - Before making changes to any subsystem, query Graphify (`query_graph`, `get_node`, `shortest_path`) for recorded past regressions, known architectural traps, and incident nodes.
  - When fixing bugs or establishing ADRs, ensure the failure mode, invariant, and solution are documented in markdown artifacts and updated in the graph (`graphify --update`).
  - Perform impact assessments using `get_pr_impact` / `shortest_path` to avoid repeating past mistakes across interdependent modules.

### 2. Context7 Live Documentation Mandate
- **Authoritative API Verification**: Before implementing any third-party library, framework, or SDK behavior, resolve the library ID and query official docs via Context7 (`resolve-library-id` -> `query-docs`).
- Do not trust training data for third-party APIs.

### 3. Artifact-Driven Quality Gates
- Non-trivial development cycles MUST produce or reference machine-readable and human-verifiable markdown artifacts (`intent.md`, `spec.md`, `implementation_plan.md`, `walkthrough.md`) before taking modifying actions.
- Shift architectural decisions left into the planning and specification stage.

### 4. Cyclic Feedback & Zero Silent Failures
- Ingest evaluation results, test failures, and operational logs as continuous input loops rather than post-facto firefighting.
- Never swallow errors; throw explicit exceptions and fail fast.

