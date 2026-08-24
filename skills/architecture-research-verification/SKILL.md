---
name: architecture-research-verification
description: Rigorous protocol for architecture research, subsystem invariant discovery, blast radius modeling via Graphify, and formal specification verification via Context7 and evaluation harnesses.
---

# Architecture Research & Verification Protocol

This skill enforces a mathematically rigorous, evidence-based research and verification process before any structural or cross-module changes are approved.

---

## 🔬 1. The 4-Pillar Research Mandate

### Pillar A: Codebase Topology & Invariants (Graphify)
1. **Query Subsystems**: Run `query_graph` or `graphify query` to extract all nodes involved in the target feature/bug.
2. **Blast Radius Analysis**: Run `shortest_path` and `get_pr_impact` to identify upstream callers and downstream dependents.
3. **God-Node Audit**: Identify heavily coupled hub nodes (`god_nodes`) to ensure changes do not destabilize the core graph.
4. **Historical Memory**: Query past incident and ADR nodes to inspect prior failure modes.

### Pillar B: Authoritative External Specs (Context7)
1. **Never Assume APIs**: For any third-party framework, ORM, SDK, or cloud provider, resolve the exact library ID:
   `resolve-library-id(libraryName)`
2. **Retrieve Official Guidance**: Query targeted documentation:
   `query-docs(libraryId, specificQuery)`
3. **Verify Version Compatibility**: Ensure local dependency version matches Context7 documentation version.

### Pillar C: Dynamic Capability Resolution (skills.sh)
1. If the architecture touches a specialized domain (e.g., LiveKit, Supabase, Playwright, Vercel edge runtime), search for vetted community runbooks:
   `npx skills find <domain>`
2. Acquire the authoritative skill package:
   `npx skills add <owner/repo> -g`

### Pillar D: Formal Specification Drafting (`spec.md`)
1. Synthesize topology, official API contracts, and invariants into a comprehensive `spec.md`.
2. Include explicit Architectural Decision Records (ADRs) with trade-off matrices.
3. Define strict TypeScript/Python interfaces with zero `any` or untyped parameters.

---

## 🛡️ 2. The Verification & Quality Gate Protocol

### Gate 1: Static Invariant Verification
- Type Check: Synchronous TypeScript strict mode or mypy validation.
- Linter & Formatting: Zero lint errors before proceeding to tests.

### Gate 2: Automated Eval Harness
- Run the continuous evaluation harness:
  `python evals/run_evals.py`
- Verify test coverage against edge cases identified during the Graphify blast-radius analysis.

### Gate 3: Staging & Preview Deployment
- Deploy and verify staging environments via Vercel MCP / CLI.
- Audit console messages and network errors on the live preview.

### Gate 4: Continuous Memory Sync
- Commit verified architecture changes to the Graphify Knowledge Graph:
  `graphify --update`
