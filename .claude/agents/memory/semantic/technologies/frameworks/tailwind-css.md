---
name: Tailwind CSS
aliases: []
entity_classification: technology/framework
status: review_needed
created: 2025-09-29T17:50:00-05:00
last_updated: 2025-09-29T17:50:00-05:00
source_episodes:
  - 250929_EP_1
summary: A utility-first CSS framework that enables rapid styling through utility classes. Selected as the styling solution for Project Alpha and required for Shadcn/ui components.
ambiguities: []
relationships:
  - type: used_by
    entity: project-alpha
    description: Primary styling framework for the project
    role: CSS framework
    source: 250929_EP_1
  - type: required_by
    entity: shadcn-ui
    description: Shadcn/ui is tightly coupled to Tailwind CSS
    role: CSS framework
    source: 250929_EP_1
  - type: works_with
    entity: vite
    description: Can be configured with Vite for fast development
    role: styling
    source: 250929_EP_1
---

## Facts

### Characteristics
- Utility-first CSS framework [250929_EP_1]
- Very popular choice for modern React applications [250929_EP_1]
- Enables rapid styling experimentation [250929_EP_1]
- Part of all recommended modern React stacks [250929_EP_1]

### Project Requirements
- Required for Shadcn/ui components (tightly coupled) [250929_EP_1]
- Cannot use other CSS solutions with Shadcn/ui [250929_EP_1]
- Needs configuration for theme colors and CSS variables [250929_EP_1]

## Constraints

- **Shadcn/ui Dependency: Tailwind CSS required** [250929_EP_1]
  - **Category:** Technical
  - **Status:** Active
  - **Scope:** All Shadcn/ui components
  - **Reason:** Shadcn/ui is tightly coupled to Tailwind and cannot work with other CSS solutions
  - **Created:** 2025-09-29

## Requirements

- **Requirement: Vibrant color palette for gamification** [250929_EP_1]
  - **Category:** Design
  - **Priority:** High
  - **Status:** Open
  - **Details:** Must configure Tailwind with vibrant colors suitable for gamification
  - **Created:** 2025-09-29