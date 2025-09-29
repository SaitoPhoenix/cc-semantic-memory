---
name: Tailwind CSS
aliases: []
entity_classification: technology/framework
status: active
created: 2025-09-29T14:23-05:00
last_updated: 2025-09-29T14:23-05:00
source_episodes:
  - 250929_EP_1
summary: A utility-first CSS framework that provides low-level utility classes for building custom designs. Selected as the styling solution for Project Alpha.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Primary styling framework for the project
    role: CSS framework
    source: 250929_EP_1
  - type: enables
    entity: shadcn-ui
    description: Shadcn/ui is tightly coupled to and requires Tailwind CSS
    role: required dependency
    source: 250929_EP_1
  - type: works_with
    entity: vite
    description: Supports rapid styling experimentation in Vite projects
    role: styling framework
    source: 250929_EP_1
---

## Facts

### Characteristics
- Utility-first CSS framework [250929_EP_1]
- Very popular for modern web development [250929_EP_1]
- Has VS Code extension: Tailwind CSS IntelliSense [250929_EP_1]

### Integration
- Built into Tremor components [250929_EP_1]
- Required by Shadcn/ui components [250929_EP_1]
- Used with Headless UI for custom designs [250929_EP_1]

## Constraints

- **Required by Shadcn/ui** [250929_EP_1]
  - **Details:** Shadcn/ui is tightly coupled to Tailwind
  - **Impact:** Cannot use Shadcn/ui with other CSS solutions
  - **Note:** Already planned for the project, so not a limitation

## Approaches

### Developer Experience
- Enables rapid styling experimentation [250929_EP_1]
- Requires Tailwind knowledge for customizing Shadcn/ui components [250929_EP_1]
- Learning curve exists if team not comfortable with utility classes [250929_EP_1]