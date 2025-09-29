---
name: TanStack Query
aliases:
  - React Query
entity_classification: technology/library
status: new
created: 2025-09-29T14:23-05:00
last_updated: 2025-09-29T14:23-05:00
source_episodes:
  - 250929_EP_1
summary: A powerful data fetching and server state management library for React applications. Selected for handling server state and caching in Project Alpha.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Handles server state management and data fetching
    role: data fetching library
    source: 250929_EP_1
  - type: complements
    entity: zustand
    description: TanStack Query handles server state while Zustand handles client state
    role: server state manager
    source: 250929_EP_1
  - type: works_with
    entity: react
    description: Server state management solution for React
    role: data fetching
    source: 250929_EP_1
---

## Facts

### Capabilities
- Provides automatic background refetching [250929_EP_1]
- Handles cache management [250929_EP_1]
- Manages loading and error states [250929_EP_1]
- Supports optimistic updates [250929_EP_1]
- Has built-in DevTools [250929_EP_1]

### Use Cases
- Perfect for fetching data from APIs [250929_EP_1]
- Handles mutations [250929_EP_1]
- Manages server state synchronization [250929_EP_1]
- Handles "what the data is doing" in applications [250929_EP_1]

## Patterns

### Architecture Pattern
- Clean separation from client state (handled by Zustand) [250929_EP_1]
- Prevents antipattern of putting server data in client state stores [250929_EP_1]
- Works well with Zustand without overlap - each handles distinct concerns [250929_EP_1]