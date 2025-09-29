---
name: React
aliases: []
entity_classification: technology/framework
status: active
created: 2025-09-29T17:50:00-05:00
last_updated: 2025-09-29T17:50:00-05:00
source_episodes:
  - 250929_EP_1
summary: A JavaScript library for building user interfaces, particularly single-page applications. Foundation framework for Project Alpha and the basis for multiple modern web development stacks.
ambiguities: []
relationships:
  - type: preferred_by
    entity: saito
    description: Saito is a fan of React for frontend development
    role: framework
    source: 250929_EP_1
  - type: used_by
    entity: project-alpha
    description: Core frontend framework for the gamification project
    role: framework
    source: 250929_EP_1
  - type: works_with
    entity: next-js
    description: Next.js is built on top of React
    role: base framework
    source: 250929_EP_1
  - type: works_with
    entity: vite
    description: Vite provides fast build tooling for React projects
    role: framework
    source: 250929_EP_1
  - type: complements
    entity: typescript
    description: Often used together for type-safe React development
    role: framework
    source: 250929_EP_1
---

## Facts

### Ecosystem
- Forms the foundation for multiple full-stack frameworks including Next.js, Remix, and Gatsby [250929_EP_1]
- Compatible with various state management solutions like Redux Toolkit, Zustand, and Jotai [250929_EP_1]
- Works with multiple styling solutions including Tailwind CSS, Styled Components, and CSS Modules [250929_EP_1]
- Supported by numerous component libraries like Shadcn/ui, Chakra UI, and MUI [250929_EP_1]

### Popular Stack Combinations
- Next.js + TypeScript + Tailwind + TanStack Query identified as industry standard for production apps [250929_EP_1]
- Vite + React + TypeScript + Zustand + Tailwind noted for fast development experience [250929_EP_1]
- Next.js + TypeScript + tRPC + Prisma + Tailwind (T3 Stack) for full-stack type safety [250929_EP_1]