---
name: ai-native-sdlc
description: Operational playbook and execution engine for the AI-Native Software Development Lifecycle (SDLC). Integrates official Graphify knowledge-graph navigation, Context7 external documentation retrieval, and skills.sh agent-skills package management for zero-mistake, artifact-driven agentic workflows.
---

# The AI-Native SDLC Playbook Skill

This skill operationalizes the modern AI-Native Software Development Lifecycle (SDLC) paradigm, moving from linear handoffs to continuous, artifact-driven agentic loops backed by **Graphify** knowledge-graph topology, **Context7** live documentation intelligence, and **skills.sh** dynamic capability acquisition.

---

## Tool & Knowledge Discovery Hierarchy

1. **Graphify Knowledge Graph (`graphify-out/graph.json`)**:
   - Primary source of truth for codebase topology, architectural boundaries, dependency flows, and God-node impact.
   - Core tools/commands: `query_graph`, `get_node`, `shortest_path`, `graphify path`, `graphify explain`.
   - Never fall back to unindexed searches unless Graphify graph is unbuilt or non-code files are targeted.

2. **Context7 External Documentation**:
   - Primary source of truth for third-party libraries, SDKs, frameworks, and APIs.
   - Core workflow: `resolve-library-id` -> `query-docs` using exact resolved library identifier (e.g., `/org/project`).
   - Never rely on outdated training weights for third-party APIs or framework contracts.

3. **skills.sh Agent Skills Package Manager (`npx skills`)**:
   - Primary engine for dynamic agent capability acquisition, domain-specific runbooks, and ecosystem skills.
   - Core workflow:
     - Search & discover skills: `npx skills find <query>`
     - Acquire domain packages: `npx skills add <owner/repo> -g` (e.g., `vercel-labs/agent-skills`)
     - Execute single-use workflows: `npx skills use <package>@<skill>`

---

## The 6 Lifecycle Stages & Required Artifacts

### 1. Planning Stage (`intent.md`)
- **Objective**: Translate raw problem statements, user friction, telemetry, or feature requests into a structured intent document.
- **Actions**:
  - Clarify the core user problem and target outcomes.
  - Query **Graphify** to assess impacted subsystems and architectural God nodes.
  - Identify missing capabilities and acquire specialized agent skills via **skills.sh** (`npx skills find` / `npx skills add`).
  - Ingest issues via GitHub MCP (`get_issue`, `list_issues`).
  - Define explicit non-goals to prevent scope creep.

### 2. Architecture & Design Stage (`spec.md`)
- **Objective**: Establish technical specifications and design contracts before coding.
- **Actions**:
  - Resolve and query **Context7** for authoritative documentation on any third-party APIs/libraries.
  - Model data structures, schemas, and API contracts.
  - Trace relationship paths using Graphify (`shortest_path`) to document integration boundaries.
  - Formulate Architectural Decision Records (ADRs) where trade-offs exist.

### 3. Implementation / Build Stage (`implementation_plan.md`)
- **Objective**: Formulate surgical, multi-phase execution plans before touching code.
- **Actions**:
  - Break tasks down into atomic, reviewable phases.
  - Enforce strict typing and zero-silent-failure patterns.
  - Leverage installed domain skills (e.g., Vercel optimize, Playwright, DB sync) during execution.
  - Make surgical, minimal code edits respecting existing invariants.

### 4. Verification & Testing Stage (Eval & Test Suites)
- **Objective**: Continuous verification through automated harnesses and preview deployments.
- **Actions**:
  - Implement unit, integration, and regression tests alongside code changes.
  - Validate against edge cases identified during planning and Graphify PR impact checks.
  - Trigger preview builds/deployments (e.g., Vercel MCP / CLI) for staging validation.
  - Verify linting, type checks, and build steps synchronously.

### 5. Review & Delivery Stage (`walkthrough.md`)
- **Objective**: High-signal summary and review package for stakeholders.
- **Actions**:
  - Provide an automated first-pass code review (style, invariants, safety).
  - Produce a structured `walkthrough.md` detailing modified files, verification commands, and test outcomes.
  - Open or update Pull Requests via GitHub MCP (`create_pull_request`, `create_pull_request_review`).
  - Highlight security-sensitive or high-risk areas for human sign-off.

### 6. Maintenance & Feedback Loop
- **Objective**: Continuous operation and intent regeneration.
- **Actions**:
  - Ingest operational feedback and telemetry anomalies.
  - Update the Graphify index (`graphify --update`) to commit newly established patterns and failure modes.
  - Sync and update installed skills via `npx skills update -g`.
  - Convert failure modes directly into new `intent.md` seeds for the next cycle.

