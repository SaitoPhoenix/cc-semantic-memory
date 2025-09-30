---
name: pnpm
aliases:
  - Performant npm
entity_classification: technology/tool
status: active
created: 2025-09-30T10:07-05:00
last_updated: 2025-09-30T10:07-05:00
source_episodes:
  - 250929_EP_1
summary: Performant package manager that uses hard links to save disk space. Faster and more efficient than npm.
ambiguities: []
relationships:
  - type: competes_with
    entity: npm
    description: Alternative to default npm
    role: competitor
    source: 250929_EP_1
  - type: competes_with
    entity: yarn
    description: Alternative package manager
    role: competitor
    source: 250929_EP_1
---

## Facts

### Performance
- Faster installs than npm [250929_EP_1]
- Uses hard links to save disk space (one copy of each package shared across projects) [250929_EP_1]
- More efficient than npm and yarn [250929_EP_1]

### Characteristics
- Stricter dependency resolution (catches hidden bugs) [250929_EP_1]
- More disk-efficient than yarn [250929_EP_1]