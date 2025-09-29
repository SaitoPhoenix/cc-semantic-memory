---
name: TypeScript
aliases: []
entity_classification: technology/language
status: review_needed
created: 2025-09-29T17:50:00-05:00
last_updated: 2025-09-29T17:50:00-05:00
source_episodes:
  - 250929_EP_1
summary: A superset of JavaScript that adds static typing, enabling better IDE support, error catching at compile-time, and improved refactoring capabilities. Core language choice for Project Alpha.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Primary programming language for type safety
    role: language
    source: 250929_EP_1
  - type: complements
    entity: react
    description: Provides type safety for React components and props
    role: language
    source: 250929_EP_1
  - type: complements
    entity: vite
    description: Vite provides excellent TypeScript support
    role: language
    source: 250929_EP_1
  - type: required_by
    entity: shadcn-ui
    description: Shadcn/ui components are written in TypeScript
    role: language
    source: 250929_EP_1
---

## Facts

### Benefits
- Catches errors at compile-time instead of runtime [250929_EP_1]
- Provides excellent IDE autocomplete and refactoring support [250929_EP_1]
- Industry standard for modern React applications [250929_EP_1]

### Integration
- Part of all recommended modern React stacks [250929_EP_1]
- Almost required for Shadcn/ui (components written in TypeScript) [250929_EP_1]
- Works with JavaScript but fighting type errors is common [250929_EP_1]

## Constraints

- **Shadcn/ui Requirement: TypeScript recommended (almost required)** [250929_EP_1]
  - **Category:** Technical
  - **Status:** Active
  - **Scope:** Shadcn/ui component usage
  - **Reason:** Components are written in TypeScript; using JavaScript results in type errors
  - **Created:** 2025-09-29