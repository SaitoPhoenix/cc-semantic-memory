---
name: Vite
aliases: []
entity_classification: technology/tool
status: active
created: 2025-09-29T14:23-05:00
last_updated: 2025-09-29T14:23-05:00
source_episodes:
  - 250929_EP_1
summary: A next-generation build tool that provides fast development experience for modern web projects. Selected as the build tool for Project Alpha.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Primary build tool for the project
    role: build system
    source: 250929_EP_1
  - type: works_with
    entity: react
    description: Provides build tooling for React projects
    role: build tool
    source: 250929_EP_1
  - type: works_with
    entity: typescript
    description: Supports TypeScript out of the box
    role: build tool
    source: 250929_EP_1
---

## Facts

### Performance
- Significantly faster than Webpack/Create React App [250929_EP_1]
- Uses native ES modules for instant hot reload [250929_EP_1]
- Creates optimized production builds with Rollup [250929_EP_1]

### Developer Experience
- Provides fast iteration capability [250929_EP_1]
- Part of recommended stack for fast development experience [250929_EP_1]

## Preferences

### Use Cases
- Recommended for projects prioritizing fast development experience [250929_EP_1]
- Ideal for rapid styling experimentation when combined with Tailwind [250929_EP_1]