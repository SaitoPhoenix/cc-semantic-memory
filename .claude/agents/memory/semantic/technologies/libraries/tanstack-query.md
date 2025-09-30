---
name: TanStack Query
aliases:
  - React Query
entity_classification: technology/library
status: new
created: 2025-09-30T10:07-05:00
last_updated: 2025-09-30T10:07-05:00
source_episodes:
  - 250929_EP_1
summary: Server state management library for React. Handles API data fetching, caching, and synchronization for Project Alpha.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Server state management solution
    role: data fetcher
    source: 250929_EP_1
  - type: complements
    entity: react
    description: Server state management for React
    role: data layer
    source: 250929_EP_1
  - type: complements
    entity: zustand
    description: Handles server state while Zustand handles client state
    role: server state manager
    source: 250929_EP_1
---

## Facts

### Features
- Server state management and caching [250929_EP_1]
- Automatic background refetching [250929_EP_1]
- Cache management [250929_EP_1]
- Built-in loading/error states [250929_EP_1]
- Also known as React Query [250929_EP_1]

### Use Cases
- Perfect for fetching data, mutations, optimistic updates [250929_EP_1]
- Handles API data, caching, synchronization [250929_EP_1]
- Smooth data handling for Project Alpha [250929_EP_1]

## Patterns

### State Separation
- TanStack Query for "what the data is doing" [250929_EP_1]
- Works alongside Zustand which handles "what the user is doing" [250929_EP_1]
- Clean separation of concerns between server and client state [250929_EP_1]

### Example Pattern
- Example query pattern: `useQuery` with `queryKey` and `queryFn` [250929_EP_1]

## Suggestions

### Development Tools
- TanStack Query DevTools built into the library [250929_EP_1]