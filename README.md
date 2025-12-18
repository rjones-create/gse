GSE — Governance Spec Executor

A minimal, boring, and durable validator for governance-style JSON specifications.

GSE exists to do exactly one thing:
validate a small, explicit JSON document against a published schema, and fail loudly if it does not conform.

Nothing more.

——

What This Is

GSE is:

A tiny CLI tool
Backed by a single JSON Schema
Designed to be readable, auditable, and forgettable
Built to survive long-term maintenance without ceremony

It is intentionally conservative.

No runtime magic.
No hidden state.
No interpretation layer.
No governance claims.

——

What This Is Not

GSE is not:

A governance system
A framework
A platform
A policy engine
A source of authority

It does not decide meaning.
It does not enforce behavior.
It does not evolve on its own.

It only checks structure.

——

Design Principles

Small on purpose  
 Fewer files, fewer dependencies, fewer decisions.

Correct over clever  
 Uses the reference `jsonschema` library. No custom validation logic.

Single public contract  
The schema (schema/v1.json) and this README are authoritative.

Boring is a feature  
If this feels exciting, it is doing too much.

Legally clean  
No implied authority, no delegation, no normative claims.

——
