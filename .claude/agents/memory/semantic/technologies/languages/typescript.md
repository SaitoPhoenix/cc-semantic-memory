---
name: TypeScript
aliases: []
entity_classification: technology/language
status: active
created: 2025-09-29T14:23-05:00
last_updated: 2025-09-29T14:23-05:00
source_episodes:
  - 250929_EP_1
summary: A superset of JavaScript that adds static typing, providing compile-time error checking and enhanced IDE support. Core language choice for Project Alpha.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Primary programming language for the project
    role: programming language
    source: 250929_EP_1
  - type: complements
    entity: react
    description: Provides type safety for React development
    role: type system
    source: 250929_EP_1
  - type: works_with
    entity: vite
    description: Vite supports TypeScript out of the box
    role: language
    source: 250929_EP_1
  - type: enables
    entity: shadcn-ui
    description: Shadcn/ui components are written in TypeScript
    role: required language
    source: 250929_EP_1
---

## Facts

### Capabilities
- Catches errors at compile-time instead of runtime [250929_EP_1]
- Provides excellent IDE autocomplete and refactoring support [250929_EP_1]
- Installed as project dependency during setup [250929_EP_1]

### Integration
- VS Code provides best-in-class TypeScript integration [250929_EP_1]
- ESLint has plugins for TypeScript support [250929_EP_1]

## Constraints

- **Shadcn/ui Requirement** [250929_EP_1]
  - **Details:** Shadcn/ui components are written in TypeScript
  - **Impact:** While JavaScript works, will encounter type errors without TypeScript
  - **Recommendation:** TypeScript recommended, almost required for Shadcn/ui