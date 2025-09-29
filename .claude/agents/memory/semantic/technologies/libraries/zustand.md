---
name: Zustand
aliases: []
entity_classification: technology/library
status: active
created: 2025-09-29T17:50:00-05:00
last_updated: 2025-09-29T17:50:00-05:00
source_episodes:
  - 250929_EP_1
summary: A lightweight state management solution for React with minimal boilerplate. Selected for Project Alpha to handle client-side state like UI state, user preferences, and local app state.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Handles client-side state management
    role: state management
    source: 250929_EP_1
  - type: complements
    entity: tanstack-query
    description: Zustand handles client state while TanStack Query handles server state
    role: state management
    source: 250929_EP_1
  - type: works_with
    entity: react
    description: State management solution designed for React
    role: library
    source: 250929_EP_1
---

## Facts

### Characteristics
- Lightweight and simple state management solution [250929_EP_1]
- Minimal boilerplate compared to Redux [250929_EP_1]
- Smaller bundle size than Redux [250929_EP_1]

### Use Cases
- Handles client state: UI state, user preferences, local app state [250929_EP_1]
- Good for theme toggles, modal states, form wizards, shopping carts [250929_EP_1]
- Manages "what the user is doing" while TanStack Query manages "what the data is doing" [250929_EP_1]

## Patterns

### State Separation
- Clean separation of concerns: client state in Zustand, server state in TanStack Query [250929_EP_1]
- Avoids antipattern of putting server data in Zustand [250929_EP_1]
- Each tool handles a distinct concern without overlap [250929_EP_1]