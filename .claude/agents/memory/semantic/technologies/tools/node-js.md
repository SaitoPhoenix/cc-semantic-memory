---
name: Node.js
aliases:
  - Node
entity_classification: technology/tool
status: active
created: 2025-09-30T10:07-05:00
last_updated: 2025-09-30T10:07-05:00
source_episodes:
  - 250929_EP_1
summary: JavaScript runtime that enables running JavaScript outside the browser. Required for Project Alpha's build tools and development environment.
ambiguities: []
relationships:
  - type: enables
    entity: npm
    description: Includes npm by default
    role: runtime
    source: 250929_EP_1
  - type: enables
    entity: vite
    description: Required to run Vite build tool
    role: runtime environment
    source: 250929_EP_1
---

## Facts

### Purpose
- JavaScript runtime that lets you run JS outside the browser [250929_EP_1]
- Required to run build tools, development servers, and package managers [250929_EP_1]
- LTS versions (even numbers: 18, 20, 22) are most stable [250929_EP_1]

### Recommendations
- v18+ recommended for Project Alpha [250929_EP_1]
- Includes npm by default [250929_EP_1]

## Requirements

- **Requirement: Node.js installation for Project Alpha** [250929_EP_1]
  - **Category:** Development Environment
  - **Priority:** Critical
  - **Status:** Open
  - **Details:** Must have Node.js v18+ installed to run build tools and development server
  - **Created:** 2025-09-29