---
allowed-tools: Bash, Read
description: Load context for a new agent session by analyzing codebase structure, documentation and README
---

# Prime

Run commands and read files to get a high level understanding of the project.

## Workflow
1. *Run:* `date -Im`
2. *Run:* `eza --tree --only-dirs --all --ignore-glob=".git|__*|node_modules|dist|build|.vscode|.idea|.venv|target|coverage|.cursor"`
3. *Run:* `git status`
4. *Run:* `git diff HEAD origin/main`
5. *Run:* `git branch --show-current`
6. *Read:* Review the files listed under `Read` to understand the project's purpose and functionality
7. *Report:* Provide a summary of your understanding of the project

### Read
- .claude/specs/project/product-specs.md

## Report

- Provide a summary of your understanding of the project
- Include key directories, describing their purpose
- Inform the user of the current state of the git repository