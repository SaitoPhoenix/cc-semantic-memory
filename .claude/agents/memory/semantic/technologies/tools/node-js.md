---
name: Node.js
aliases:
  - Node
  - NodeJS
entity_classification: technology/tool
status: new
created: 2025-09-29T14:23-05:00
last_updated: 2025-09-29T14:23-05:00
source_episodes:
  - 250929_EP_1
summary: JavaScript runtime that enables running JavaScript outside the browser. Required foundation for modern web development tooling.
ambiguities: []
relationships:
  - type: enables
    entity: project-alpha
    description: Required runtime for development environment
    role: JavaScript runtime
    source: 250929_EP_1
  - type: contains
    entity: npm
    description: npm comes bundled with Node.js
    role: runtime
    source: 250929_EP_1
---

## Facts

### Purpose
- JavaScript runtime for running JS outside the browser [250929_EP_1]
- Required to run build tools, development servers, and package managers [250929_EP_1]
- Version 18+ recommended for Project Alpha [250929_EP_1]

### Versions
- LTS versions (even numbers: 18, 20, 22) are most stable [250929_EP_1]
- Includes npm by default [250929_EP_1]

## Requirements

- **Required for Project Alpha** [250929_EP_1]
  - **Version:** v18+ recommended
  - **Purpose:** Foundation for all development tooling