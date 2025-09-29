---
name: Node.js
aliases: []
entity_classification: technology/tool
status: review_needed
created: 2025-09-29T17:50:00-05:00
last_updated: 2025-09-29T17:50:00-05:00
source_episodes:
  - 250929_EP_1
summary: JavaScript runtime that enables running JavaScript outside the browser. Required for running build tools, development servers, and package managers in modern web development.
ambiguities: []
relationships:
  - type: required_by
    entity: project-alpha
    description: Required for development environment and build tools
    role: runtime
    source: 250929_EP_1
  - type: contains
    entity: npm
    description: npm comes bundled with Node.js by default
    role: runtime
    source: 250929_EP_1
---

## Facts

### Characteristics
- JavaScript runtime for running JS outside the browser [250929_EP_1]
- Required to run build tools, development servers, and package managers [250929_EP_1]
- Version 18+ recommended for Project Alpha [250929_EP_1]
- LTS versions (even numbers: 18, 20, 22) are most stable [250929_EP_1]
- Includes npm by default [250929_EP_1]

## Requirements

- **Requirement: Node.js v18+ required** [250929_EP_1]
  - **Category:** Development Environment
  - **Priority:** Critical
  - **Status:** Open
  - **Details:** Node.js version 18 or higher is recommended for the project
  - **Created:** 2025-09-29