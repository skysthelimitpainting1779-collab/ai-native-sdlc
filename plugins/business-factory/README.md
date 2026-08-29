# Business Factory v0

Business Factory is an evidence-driven bootstrap business creation plugin.

It starts from the question **“Why would a specific real buyer give us money instead of doing nothing or choosing an alternative?”** and treats company creation as sequential search under uncertainty.

## v0 objective

Prove the operating algorithm before building a standalone Business OS:

```text
opportunity
-> buyer/problem/economics research
-> explicit hypotheses
-> cheapest valid experiments
-> war-room verdicts
-> resource reallocation
-> payment/delivery/retention evidence
-> Software Factory handoff only when earned
-> workflows/operators/automation
-> compounding learning
```

## Starting constraint

`cash_new_spend = 0` by default.

This does **not** mean low capability. Business Factory should aggressively use legitimate existing capacity:

- already-paid ChatGPT/Codex capability;
- CLI and deterministic scripts;
- existing databases and workflow engines;
- free APIs/tiers where their current terms allow the intended use;
- open-source/local tools;
- MCP/connectors/WebMCP;
- authenticated browser execution;
- computer use;
- agent email, SMS/messaging, and voice;
- human approval only where judgment, authority, or risk requires it.

## Core outputs

A run maintains an Opportunity Ledger, Purchase Thesis, Hypothesis Ledger, Experiment Ledger, Evidence Ledger, War Room Ledger, Resource Ledger, Decision Ledger, Pattern Ledger, and Software Factory handoff packets.

## Material-state war rooms

Every material promotion must pass an appropriately sized adversarial review. Review depth is based on:

`impact × uncertainty × irreversibility × downstream blast radius`

The implementer/proposer may advocate, but may not be the sole judge.

## Compounding model

Business Factory compounds four things:

1. **market knowledge** — better ICP, pain, trigger, offer, pricing, objection and channel models;
2. **distribution** — reusable prospecting, sales and referral channels;
3. **execution primitives** — code, integrations, workflows, operators and automations;
4. **factory intelligence** — validated rules about which tests, patterns, resources and business structures work under which conditions.

Failures are preserved when they reduce future search space. Wins are promoted only after replication/context checks.

## Relationship to Software Factory

Business Factory decides **what should exist, for whom, why, and what evidence warrants further investment**.

Software Factory decides **how to build the validated technical capability safely and verify that it works**.

A Business Factory handoff must identify the originating business outcome, evidence, validated workflow, acceptance tests, current execution surfaces, expected automation value, security boundary and rollback path.

## Installation status

This directory is a v0 plugin package scaffold inside `ai-native-sdlc`. It is intentionally isolated from the existing SDLC plugin so Business Factory can be extracted to its own repository/package once the plugin contract is stable.

The canonical skill entrypoint is:

`plugins/business-factory/skills/business-factory/SKILL.md`
