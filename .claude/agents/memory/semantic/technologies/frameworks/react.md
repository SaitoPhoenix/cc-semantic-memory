---
name: React
aliases: []
entity_classification: technology/framework
status: new
created: 2025-09-29T14:23-05:00
last_updated: 2025-09-29T14:23-05:00
source_episodes:
  - 250929_EP_1
summary: A JavaScript library for building user interfaces, particularly popular for web applications. Core technology for Project Alpha.
ambiguities: []
relationships:
  - type: preferred_by
    entity: saito
    description: Saito is a fan of React
    role: preferred framework
    source: 250929_EP_1
  - type: used_by
    entity: project-alpha
    description: Core UI framework for the project
    role: frontend framework
    source: 250929_EP_1
  - type: works_with
    entity: next-js
    description: Next.js is built on top of React
    role: base framework
    source: 250929_EP_1
  - type: works_with
    entity: vite
    description: Vite provides build tooling for React projects
    role: framework
    source: 250929_EP_1
  - type: complements
    entity: typescript
    description: Often used together for type-safe React development
    role: UI library
    source: 250929_EP_1
---

## Facts

### Ecosystem
- Has multiple popular full-stack frameworks including Next.js, Remix, and Gatsby [250929_EP_1]
- Supports various state management solutions like Redux Toolkit, Zustand, and Jotai [250929_EP_1]
- Works with multiple styling approaches including Tailwind CSS, Styled Components, and CSS Modules [250929_EP_1]

### Popular Stacks
- Next.js + TypeScript + Tailwind + TanStack Query described as industry standard [250929_EP_1]
- Vite + React + TypeScript + Zustand + Tailwind noted for fast development experience [250929_EP_1]
- T3 Stack (Next.js + TypeScript + tRPC + Prisma + Tailwind) for full-stack type safety [250929_EP_1]