---
name: TanStack Query
aliases:
  - React Query
entity_classification: technology/library
status: new
created: 2025-09-29T17:50:00-05:00
last_updated: 2025-09-29T17:50:00-05:00
source_episodes:
  - 250929_EP_1
summary: A powerful data synchronization library for React that handles server state management, caching, and background refetching. Selected for Project Alpha to manage API data and server synchronization.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Manages server state and API data fetching
    role: data fetching library
    source: 250929_EP_1
  - type: complements
    entity: zustand
    description: TanStack Query handles server state while Zustand handles client state
    role: state management
    source: 250929_EP_1
  - type: works_with
    entity: react
    description: Data fetching and caching library for React
    role: library
    source: 250929_EP_1
---

## Facts

### Core Features
- Automatic background refetching [250929_EP_1]
- Cache management [250929_EP_1]
- Loading and error states handling [250929_EP_1]
- Built-in DevTools for debugging [250929_EP_1]

### Use Cases
- Perfect for fetching data, mutations, and optimistic updates [250929_EP_1]
- Handles server state (API data, caching, synchronization) [250929_EP_1]
- Manages "what the data is doing" while Zustand manages "what the user is doing" [250929_EP_1]

## Patterns

### Integration with State Management
- Works excellently alongside Zustand with clear separation of concerns [250929_EP_1]
- Prevents antipattern of storing server data in client state management [250929_EP_1]
- Each library handles distinct concerns without overlap [250929_EP_1]

## Suggestions

### Stack Integration
- Can be integrated with the Vite + React + TypeScript + Zustand + Tailwind stack [250929_EP_1]
- Part of the industry standard stack: Next.js + TypeScript + Tailwind + TanStack Query [250929_EP_1]