---
name: Shadcn/ui
aliases:
  - shadcn
  - shadcn ui
entity_classification: technology/library
status: new
created: 2025-09-29T14:23-05:00
last_updated: 2025-09-29T14:23-05:00
source_episodes:
  - 250929_EP_1
summary: A component library that provides copy-paste React components built on Radix UI and Tailwind CSS. Selected as the design system for Project Alpha due to its flexibility and customizability.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Primary component library and design system
    role: UI component library
    source: 250929_EP_1
  - type: preferred_by
    entity: saito
    description: Chosen for its flexibility and code ownership model
    role: design system choice
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
  - type: depends_on
    entity: typescript
    description: Components are written in TypeScript
    role: component library
    source: 250929_EP_1
---

## Facts

### Architecture
- Not a traditional package - components are copied into codebase [250929_EP_1]
- Built on Radix UI + Tailwind CSS [250929_EP_1]
- Provides CLI for initialization: `npx shadcn-ui@latest init` [250929_EP_1]
- Requires configuration of components.json, path aliases, Tailwind config [250929_EP_1]

### Characteristics
- Fully customizable since you own the code [250929_EP_1]
- Not technically a component library - you copy components into your project [250929_EP_1]
- Components live in your repository [250929_EP_1]
- No built-in themes or full page templates [250929_EP_1]

## Decisions

- **Selected over alternatives for Project Alpha** [250929_EP_1]
  - **Alternatives Considered:** Tremor (too dashboard-focused), Mantine, Carbon (too corporate), Chakra UI
  - **Rationale:** Maximum flexibility for gamification customization
  - **Key Benefit:** Full control over component code

## Constraints

- **Not a Traditional Package** [250929_EP_1]
  - **Impact:** Components must be maintained and updated manually
  - **Benefit:** Full control over implementation

- **Requires Tailwind CSS** [250929_EP_1]
  - **Impact:** Cannot use with other CSS solutions
  - **Note:** Already planned for project

- **TypeScript Recommended** [250929_EP_1]
  - **Impact:** Works with JavaScript but will encounter type errors
  - **Recommendation:** Almost required for smooth experience

- **Bundle Size Considerations** [250929_EP_1]
  - **Impact:** Cannot tree-shake unused parts of copied components
  - **Note:** Still smaller than full libraries

- **Animation Limitations** [250929_EP_1]
  - **Impact:** Basic animations included, may need Framer Motion or GSAP for gamification
  - **Solution:** Can integrate additional animation libraries

## Preferences

### Use Cases
- Ideal for gamification because components can be heavily modified [250929_EP_1]
- Perfect for projects wanting creative freedom [250929_EP_1]
- Good for building custom game-like aesthetics [250929_EP_1]
- Can add custom gamification components alongside base components [250929_EP_1]

## Philosophies

### Development Philosophy
- Ownership over convenience [250929_EP_1]
- Reading component code teaches patterns [250929_EP_1]
- Debugging is straightforward with no black box mysteries [250929_EP_1]
- Every animation and interaction can be intentionally crafted [250929_EP_1]