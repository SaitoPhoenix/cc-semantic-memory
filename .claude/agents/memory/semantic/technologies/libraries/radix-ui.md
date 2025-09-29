---
name: Radix UI
aliases: []
entity_classification: technology/library
status: new
created: 2025-09-29T17:50:00-05:00
last_updated: 2025-09-29T17:50:00-05:00
source_episodes:
  - 250929_EP_1
summary: A collection of low-level, unstyled, accessible UI primitive components. Forms the foundation for Shadcn/ui components, providing accessibility features.
ambiguities: []
relationships:
  - type: used_by
    entity: shadcn-ui
    description: Shadcn/ui is built on top of Radix UI primitives
    role: foundation library
    source: 250929_EP_1
---

## Facts

### Role in Project
- Provides accessibility features for Shadcn/ui components [250929_EP_1]
- Acts as the primitive foundation that Shadcn/ui builds upon [250929_EP_1]
- Generally stable architecture [250929_EP_1]
- Learning Radix UI primitives improves accessible component design skills [250929_EP_1]

## Constraints

- **Shadcn/ui dependency** [250929_EP_1]
  - **Category:** Technical Dependency
  - **Status:** Active
  - **Scope:** All Shadcn/ui interactive components
  - **Reason:** Shadcn/ui requires Radix UI for accessibility primitives
  - **Created:** 2025-09-29