---
name: pnpm
aliases:
  - Performant npm
entity_classification: technology/tool
status: active
created: 2025-09-29T17:50:00-05:00
last_updated: 2025-09-29T17:50:00-05:00
source_episodes:
  - 250929_EP_1
summary: A fast, disk space efficient package manager that uses hard links to share packages across projects. Alternative to npm with better performance characteristics.
ambiguities: []
relationships: []
---

## Facts

### Characteristics
- Uses hard links to save disk space (one copy of each package shared across projects) [250929_EP_1]
- Faster installs than npm [250929_EP_1]
- Stricter dependency resolution that catches hidden bugs [250929_EP_1]
- More disk-efficient than yarn [250929_EP_1]