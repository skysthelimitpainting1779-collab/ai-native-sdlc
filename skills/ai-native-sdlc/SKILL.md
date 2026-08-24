---
name: ai-native-sdlc
description: Operational playbook and autonomous execution engine for the AI-Native Software Development Lifecycle (SDLC). Takes any raw project idea, user prompt, or goal and executes an autonomous, artifact-driven continuous loop that conducts deep research, builds surgical code, and verifies 100% of invariants across the entire stack.
---

# The AI-Native SDLC Autonomous Goal & Verification Engine

This skill empowers Antigravity to take **any raw project idea, feature request, or architectural goal** and execute an unbroken, autonomous verification loop that leaves zero technical debt or unverified assumptions.

---

## 🎯 Goal Ingestion to 360° Verification Loop

```mermaid
graph TD
    subgraph Autonomous_Execution ["End-to-End Goal & Verification Loop"]
        Goal["💡 RAW PROJECT IDEA / GOAL"] --> Ingest["1. GOAL INGESTION & DECOMPOSITION<br/>• Clarify Intent & Non-Goals<br/>• Discover Subsystems in Graphify<br/>• Auto-Acquire Skills via skills.sh"]
        
        Ingest --> Research["2. DEEP RESEARCH & CONTRACT DESIGN<br/>• Context7 Live API Contracts<br/>• Graphify Blast Radius & God Nodes<br/>• Strict Schema & ADR Generation"]
        
        Research --> Build["3. ATOMIC SURGICAL IMPLEMENTATION<br/>• Implementation Plan Approval Gate<br/>• Strict TypeScript / Python Types<br/>• Zero Silent Failures"]
        
        Build --> Verify["4. 360° VERIFICATION HARNESS<br/>• Static Typing & Linter Checks<br/>• Unit, Integration & Regression Tests<br/>• Live Vercel Staging Deploy & Preview Evals<br/>• Graphify Invariant Diff Audit"]
        
        Verify -->|❌ Any Verification Failure| AutoHeal["🔄 AUTO-HEALING REMEDIATION<br/>• Feed error trace back into Build"] --> Build
        
        Verify -->|✅ 100% Verification Passed| Deliver["5. STAKEHOLDER DELIVERY & REVIEW<br/>• walkthrough.md Evidence Package<br/>• GitHub PR & Automated Review<br/>• Human Sign-Off"]
        
        Deliver --> Memory["6. KNOWLEDGE COMMIT & TELEMETRY<br/>• graphify --update (Commit Invariants)<br/>• npx skills update -g<br/>• Telemetry Feedback Loop"]
        
        Memory --> NextGoal["🚀 Next Feature / Anomaly Seed"]
    end
```

---

## 🔍 The 360° Verification Matrix

Before any project idea, feature, or refactor is considered complete, it MUST pass all 5 verification gates:

| Verification Layer | Tool / Engine | Pass Criteria |
| :--- | :--- | :--- |
| **1. Type & Contract Safety** | Strict Compiler / Mypy | Zero `any`, zero untyped params, strict null checks pass. |
| **2. Codebase Invariant Integrity** | Graphify Knowledge Graph | `shortest_path` and `get_pr_impact` confirm zero broken dependencies or unhandled regressions. |
| **3. External API Conformance** | Context7 Live Docs | All external library/API usage conforms 100% to verified official documentation. |
| **4. Functional & Regression Testing**| Pytest / Jest / Playwright | All test suites pass; newly created test cases cover all edge cases identified in `intent.md`. |
| **5. Live Runtime Staging** | Vercel MCP / Preview URL | Clean preview build with zero runtime console errors and verified visual endpoints. |

---

## 🔁 Stage-by-Stage Operational Runbook

### Stage 1: Goal Ingestion & Intent Definition (`intent.md`)
- **Action**: Take the user's raw prompt/goal and formalize it into `intent.md`.
- **Knowledge Lookups**:
  - Run `query_graph` or `graphify query` to locate existing modules and historical incident nodes.
  - Run `npx skills find <domain>` to dynamically download required ecosystem skills.
  - Define clear **In-Scope** vs. **Explicit Non-Goals** to protect against scope creep.

### Stage 2: Architecture Research & Specification (`spec.md`)
- **Action**: Launch `sdlc-researcher` or execute `architecture-research-verification`.
- **Authoritative Specs**:
  - Resolve official library IDs with Context7 (`resolve-library-id` -> `query-docs`).
  - Draft `spec.md` with explicit data models and Architectural Decision Records (ADRs).

### Stage 3: Surgical Phased Implementation (`implementation_plan.md`)
- **Action**: Formulate `implementation_plan.md` breaking changes into atomic steps.
- **Execution**: Apply surgical edits with strict typing, zero-debt refactoring, and fail-fast exception handling.

### Stage 4: 360° Continuous Verification Loop
- **Action**: Run the complete automated test suite and evaluate against `evals/sdlc_eval_suite.json`.
- **Preview Deploy**: Trigger Vercel staging deployment and audit runtime performance.
- **Auto-Healing**: If any check fails, feed the error trace immediately back into Stage 3 to resolve the issue autonomously.

### Stage 5: Delivery & PR Review (`walkthrough.md`)
- **Action**: Package all changes, test outputs, diffs, and preview links into `walkthrough.md`.
- **Pull Request**: Open or update the GitHub Pull Request via GitHub MCP (`create_pull_request`).

### Stage 6: Persistent Memory & Intent Regeneration
- **Action**: Run `scripts/sync-graphify.ps1` (`graphify --update`) to commit new architectural invariants into `graphify-out/graph.json`.
- **Continuous Evolution**: Auto-draft subsequent `intent.md` artifacts as runtime telemetry or new goals emerge.
