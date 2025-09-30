---
name: Tailwind CSS
aliases:
  - Tailwind
entity_classification: technology/framework
status: active
created: 2025-09-30T10:07-05:00
last_updated: 2025-09-30T10:07-05:00
source_episodes:
  - 250929_EP_1
summary: Utility-first CSS framework. Selected for Project Alpha for rapid styling and works as foundation for Shadcn/ui components.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: CSS framework for styling
    role: styling system
    source: 250929_EP_1
  - type: enables
    entity: shadcn-ui
    description: Required foundation for Shadcn/ui components
    role: CSS foundation
    source: 250929_EP_1
---

## Facts

### Characteristics
- Utility-first CSS framework [250929_EP_1]
- Very popular in modern React stacks [250929_EP_1]
- Rapid styling experimentation capability [250929_EP_1]

### Integration
- Part of recommended stack with Vite + React + TypeScript [250929_EP_1]
- Required for Shadcn/ui components [250929_EP_1]
- Works with Headless UI from the Tailwind team [250929_EP_1]

## Constraints

- **Shadcn/ui Requirement: Must use Tailwind CSS** [250929_EP_1]
  - **Category:** Technology
  - **Status:** Active
  - **Scope:** All Shadcn/ui components
  - **Reason:** Shadcn/ui is tightly coupled to Tailwind, cannot use with other CSS solutions
  - **Created:** 2025-09-29