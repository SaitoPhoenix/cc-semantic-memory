---
name: TypeScript
aliases: []
entity_classification: technology/language
status: active
created: 2025-09-30T10:07-05:00
last_updated: 2025-09-30T10:07-05:00
source_episodes:
  - 250929_EP_1
summary: Superset of JavaScript with static typing. Primary programming language for Project Alpha, providing type safety and better IDE support.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Primary programming language
    role: main language
    source: 250929_EP_1
  - type: works_with
    entity: react
    description: Provides type safety for React components
    role: typing system
    source: 250929_EP_1
  - type: works_with
    entity: vite
    description: Supported out of the box by Vite
    role: language
    source: 250929_EP_1
---

## Facts

### Benefits
- Catches errors at compile-time instead of runtime [250929_EP_1]
- Excellent IDE autocomplete and refactoring support [250929_EP_1]
- Superset of JavaScript with static typing [250929_EP_1]

### Integration with Stack
- Part of all modern React stack recommendations [250929_EP_1]
- Works with Vite out of the box [250929_EP_1]
- Will be installed with the project [250929_EP_1]

## Constraints

- **Shadcn/ui Components: TypeScript recommended (almost required)** [250929_EP_1]
  - **Category:** Technology
  - **Status:** Active
  - **Scope:** Shadcn/ui components
  - **Reason:** Components are written in TypeScript, using JavaScript causes type errors
  - **Created:** 2025-09-29