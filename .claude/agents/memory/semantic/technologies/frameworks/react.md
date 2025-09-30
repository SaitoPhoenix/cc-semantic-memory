---
name: React
aliases: []
entity_classification: technology/framework
status: new
created: 2025-09-30T10:07-05:00
last_updated: 2025-09-30T10:07-05:00
source_episodes:
  - 250929_EP_1
summary: JavaScript library for building user interfaces. Core framework for Project Alpha and preferred by Saito.
ambiguities: []
relationships:
  - type: preferred_by
    entity: saito
    description: Saito is a fan of React
    role: preferred technology
    source: 250929_EP_1
  - type: used_by
    entity: project-alpha
    description: Core UI framework for the project
    role: primary framework
    source: 250929_EP_1
  - type: works_with
    entity: typescript
    description: Commonly used together for type safety
    role: UI framework
    source: 250929_EP_1
  - type: works_with
    entity: vite
    description: Build tool for React development
    role: framework
    source: 250929_EP_1
  - type: complements
    entity: zustand
    description: State management solution for React
    role: UI framework
    source: 250929_EP_1
  - type: complements
    entity: tanstack-query
    description: Server state management for React
    role: UI framework
    source: 250929_EP_1
---

## Facts

### Popular Stacks
- Next.js + TypeScript + Tailwind + TanStack Query is industry standard for production apps [250929_EP_1]
- Vite + React + TypeScript + Zustand + Tailwind provides fast development experience [250929_EP_1]
- Next.js + TypeScript + tRPC + Prisma + Tailwind (T3 Stack) offers full-stack type safety [250929_EP_1]

### Framework Options
- Next.js is the most popular choice for React, offering SSR, SSG, API routes, and file-based routing [250929_EP_1]
- Remix focuses on web fundamentals, nested routes, and progressive enhancement [250929_EP_1]
- Gatsby specializes in static site generation with a rich plugin ecosystem [250929_EP_1]