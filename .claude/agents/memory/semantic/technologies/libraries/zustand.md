---
name: Zustand
aliases: []
entity_classification: technology/library
status: active
created: 2025-09-29T14:23-05:00
last_updated: 2025-09-29T14:23-05:00
source_episodes:
  - 250929_EP_1
summary: A lightweight state management library for React applications. Selected for managing client state in Project Alpha.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Handles client state management
    role: state management
    source: 250929_EP_1
  - type: complements
    entity: tanstack-query
    description: Zustand handles client state while TanStack Query handles server state
    role: client state manager
    source: 250929_EP_1
  - type: works_with
    entity: react
    description: State management solution for React
    role: state manager
    source: 250929_EP_1
---

## Facts

### Characteristics
- Lightweight and simple state management solution [250929_EP_1]
- Minimal boilerplate compared to Redux [250929_EP_1]
- Smaller bundle size compared to Redux [250929_EP_1]

### Use Cases
- Ideal for UI state management [250929_EP_1]
- Good for user preferences [250929_EP_1]
- Handles local app state [250929_EP_1]
- Examples: theme toggles, modal states, form wizards, shopping carts [250929_EP_1]
- For gamification: simple state for game mechanics [250929_EP_1]

## Patterns

### Best Practices
- Should handle "what the user is doing" while TanStack Query handles "what the data is doing" [250929_EP_1]
- Avoid putting server data in Zustand (common antipattern) [250929_EP_1]
- Clean separation of concerns with TanStack Query [250929_EP_1]