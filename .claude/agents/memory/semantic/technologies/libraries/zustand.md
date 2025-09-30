---
name: Zustand
aliases: []
entity_classification: technology/library
status: new
created: 2025-09-30T10:07-05:00
last_updated: 2025-09-30T10:07-05:00
source_episodes:
  - 250929_EP_1
summary: Lightweight state management library for React. Selected for Project Alpha to handle client-side state with minimal boilerplate.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Client state management solution
    role: state manager
    source: 250929_EP_1
  - type: complements
    entity: react
    description: State management for React applications
    role: state solution
    source: 250929_EP_1
  - type: complements
    entity: tanstack-query
    description: Handles client state while TanStack Query handles server state
    role: client state manager
    source: 250929_EP_1
---

## Facts

### Characteristics
- Lightweight and simple state management [250929_EP_1]
- Minimal boilerplate compared to Redux [250929_EP_1]
- Smaller bundle size than Redux [250929_EP_1]

### Use Cases
- Handles client state (UI state, user preferences, local app state) [250929_EP_1]
- Great for theme toggles, modal states, form wizards, shopping carts [250929_EP_1]
- Simple state for game mechanics in Project Alpha [250929_EP_1]

## Patterns

### State Separation
- Zustand for "what the user is doing" [250929_EP_1]
- Works alongside TanStack Query which handles "what the data is doing" [250929_EP_1]
- Avoids antipattern of putting server data in Zustand [250929_EP_1]

### Example Pattern
- Example store pattern: `useUIStore` with `sidebarOpen` state and `toggleSidebar` action [250929_EP_1]