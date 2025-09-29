---
name: Shadcn/ui
aliases:
  - shadcn-ui
entity_classification: technology/library
status: new
created: 2025-09-29T17:50:00-05:00
last_updated: 2025-09-29T17:50:00-05:00
source_episodes:
  - 250929_EP_1
summary: A component library that provides copy-and-paste React components built on Radix UI primitives and styled with Tailwind CSS. Selected for Project Alpha due to its customizability for gamification needs.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Provides customizable UI components for the gamification project
    role: component library
    source: 250929_EP_1
  - type: preferred_by
    entity: saito
    description: Chosen over alternatives for its customizability
    role: component library
    source: 250929_EP_1
  - type: depends_on
    entity: tailwind-css
    description: Tightly coupled to Tailwind for styling
    role: component library
    source: 250929_EP_1
  - type: depends_on
    entity: radix-ui
    description: Built on top of Radix UI primitives for accessibility
    role: component library
    source: 250929_EP_1
  - type: works_with
    entity: typescript
    description: Components are written in TypeScript
    role: component library
    source: 250929_EP_1
---

## Facts

### Architecture
- Not a traditional npm package - components are copied into codebase [250929_EP_1]
- Built on Radix UI primitives for accessibility [250929_EP_1]
- Components are maintained and updated by developers themselves [250929_EP_1]
- CLI available for easy component installation: `npx shadcn-ui@latest init` [250929_EP_1]

### Benefits for Gamification
- Fully customizable for game-like aesthetics [250929_EP_1]
- Easy to modify animations, colors, and themes [250929_EP_1]
- Developer owns the code, enabling complete creative control [250929_EP_1]
- Can integrate custom animations easily [250929_EP_1]
- Pairs perfectly with Tailwind stack [250929_EP_1]

### Available Components
- Has components useful for gamification: Progress, Badge, Card, Avatar, Tabs [250929_EP_1]
- Can be extended with custom gamification components like XP bars and achievement cards [250929_EP_1]

## Preferences

### Development Philosophy
- Chosen because it aligns with Saito's preference for owning and maintaining code [250929_EP_1]
- Provides "ownership over convenience" which enables creative freedom [250929_EP_1]
- Allows deep customization without fighting framework constraints [250929_EP_1]

## Constraints

- **Not a traditional package** [250929_EP_1]
  - **Category:** Architecture
  - **Status:** Active
  - **Scope:** Component management
  - **Reason:** Components are copied into codebase rather than installed as dependency
  - **Created:** 2025-09-29

- **Requires Tailwind CSS** [250929_EP_1]
  - **Category:** Technical Dependency
  - **Status:** Active
  - **Scope:** All components
  - **Reason:** Components are built with Tailwind utility classes
  - **Created:** 2025-09-29

- **TypeScript recommended** [250929_EP_1]
  - **Category:** Language Requirement
  - **Status:** Active
  - **Scope:** Component usage
  - **Reason:** Components written in TypeScript; JavaScript usage causes type errors
  - **Created:** 2025-09-29

- **Requires configuration setup** [250929_EP_1]
  - **Category:** Setup
  - **Status:** Active
  - **Scope:** Initial project setup
  - **Reason:** Needs components.json, path aliases, and Tailwind config
  - **Created:** 2025-09-29

- **Dependency on Radix UI** [250929_EP_1]
  - **Category:** Technical Dependency
  - **Status:** Active
  - **Scope:** All interactive components
  - **Reason:** Built on Radix UI primitives for accessibility
  - **Created:** 2025-09-29

- **Bundle size considerations** [250929_EP_1]
  - **Category:** Performance
  - **Status:** Active
  - **Scope:** Component inclusion
  - **Reason:** Can't tree-shake unused parts of copied components
  - **Created:** 2025-09-29

- **Version control implications** [250929_EP_1]
  - **Category:** Development Process
  - **Status:** Active
  - **Scope:** Component maintenance
  - **Reason:** Components live in repo, creating potential merge conflicts
  - **Created:** 2025-09-29

## Suggestions

### Comparison with Alternatives
- Recommended over Mantine for greater customization control [250929_EP_1]
- Preferred over Chakra UI for gamification due to ownership model [250929_EP_1]
- Better than Tremor for gamification (Tremor too dashboard-focused) [250929_EP_1]
- Chosen over Carbon which feels too corporate for gamification [250929_EP_1]