---
name: Shadcn/ui
aliases:
  - Shadcn
  - shadcn-ui
entity_classification: technology/library
status: new
created: 2025-09-30T10:07-05:00
last_updated: 2025-09-30T10:07-05:00
source_episodes:
  - 250929_EP_1
summary: Component library built on Radix UI and Tailwind CSS where components are copied into your codebase rather than installed as packages. Selected as the design system for Project Alpha.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Design system and component library
    role: UI components
    source: 250929_EP_1
  - type: preferred_by
    entity: saito
    description: Selected over alternatives for gamification project
    role: chosen solution
    source: 250929_EP_1
  - type: depends_on
    entity: tailwind-css
    description: Requires Tailwind CSS for styling
    role: component library
    source: 250929_EP_1
  - type: depends_on
    entity: radix-ui
    description: Built on top of Radix UI primitives
    role: styled layer
    source: 250929_EP_1
---

## Facts

### Architecture
- Not a traditional package - components are copied into codebase [250929_EP_1]
- Not technically a component library - you copy components into your project [250929_EP_1]
- Built on Radix UI + Tailwind [250929_EP_1]
- Fully customizable since you own the code [250929_EP_1]
- Works perfectly with Vite + React + TypeScript + Tailwind stack [250929_EP_1]

### Components
- Has components like Progress, Badge, Card, Avatar, Tabs [250929_EP_1]
- Great for gamification with easy modifications for animations, colors, themes [250929_EP_1]
- CLI helps with initialization: `npx shadcn-ui@latest init` [250929_EP_1]

### Documentation
- Great documentation and active community [250929_EP_1]

## Preferences

### Why Chosen for Project Alpha
- Ideal for gamification aesthetics [250929_EP_1]
- Easy to customize for game-like interactions [250929_EP_1]
- Can add custom gamification components alongside base components [250929_EP_1]
- Can integrate custom animations easily [250929_EP_1]

## Constraints

- **Not a Traditional Package** [250929_EP_1]
  - **Category:** Architecture
  - **Status:** Active
  - **Scope:** All component usage
  - **Reason:** Components must be copied and maintained in codebase
  - **Created:** 2025-09-29

- **Requires Configuration Setup** [250929_EP_1]
  - **Category:** Setup
  - **Status:** Active
  - **Scope:** Initial project setup
  - **Reason:** Need to configure components.json, path aliases, Tailwind config
  - **Created:** 2025-09-29

- **Dependency on Radix UI** [250929_EP_1]
  - **Category:** Dependencies
  - **Status:** Active
  - **Scope:** All components
  - **Reason:** Built on Radix UI primitives for accessibility
  - **Created:** 2025-09-29

- **TypeScript Recommended** [250929_EP_1]
  - **Category:** Language
  - **Status:** Active
  - **Scope:** Component implementation
  - **Reason:** Components written in TypeScript, JavaScript usage causes type errors
  - **Created:** 2025-09-29

- **Bundle Size Considerations** [250929_EP_1]
  - **Category:** Performance
  - **Status:** Active
  - **Scope:** Production builds
  - **Reason:** Cannot tree-shake unused parts of copied components
  - **Created:** 2025-09-29

- **Styling Customization Requirements** [250929_EP_1]
  - **Category:** Skills
  - **Status:** Active
  - **Scope:** Component customization
  - **Reason:** Requires Tailwind knowledge for effective customization
  - **Created:** 2025-09-29

- **Version Control Impact** [250929_EP_1]
  - **Category:** Development
  - **Status:** Active
  - **Scope:** Team collaboration
  - **Reason:** Components in repo can cause merge conflicts
  - **Created:** 2025-09-29

- **No Built-in Themes** [250929_EP_1]
  - **Category:** Features
  - **Status:** Active
  - **Scope:** Page layouts
  - **Reason:** Provides components, not full page layouts
  - **Created:** 2025-09-29

- **Animation Limitations** [250929_EP_1]
  - **Category:** Features
  - **Status:** Active
  - **Scope:** Gamification features
  - **Reason:** Basic animations only, may need Framer Motion or GSAP for advanced effects
  - **Created:** 2025-09-29