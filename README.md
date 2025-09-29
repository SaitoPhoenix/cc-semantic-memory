# Claude Code Semantic Memory System

A token-efficient memory system for Claude Code that captures conversation transcripts as episodic memories and synthesizes them into structured semantic knowledge.

## Overview

This project extends Claude Code with an automated memory system that:
- **Captures** every conversation as episodic memory (JSON transcripts)
- **Synthesizes** episodic memories into semantic knowledge (structured markdown files)
- **Organizes** knowledge into an interconnected graph of entities and relationships
- **Maintains** persistent context across Claude Code sessions

## How It Works

### 1. Episodic Memory Capture

When you start a Claude Code session, a conversation watchdog automatically captures the full transcript in real-time.

**Process:**
- Session starts → `session_start` hook triggers
- Watchdog subprocess launches and monitors conversation
- All messages, tool calls, and responses are captured as JSON
- Session ends → `session_end` hook cleans up watchdog subprocess
- Complete episodic memory saved to `.claude/agents/memory/episodic/YYYY/MM/YYMMDD_EP_N.json`

**Example Episode Structure:**
```json
{
  "metadata": [...],
  "conversations_headers": ["id", "order", "parent_id", "timestamp", "speaker", "operation", "message"],
  "conversations_data": [
    ["5c55f", "1", null, 1759170294, "Saito", "response", "Hello"],
    ["cec3c", "2", "5c55f", 1759170316, "The Architect", "response", "Hello Saito! How can I help you today?"],
    ...
  ]
}
```

### 2. Semantic Memory Synthesis

After conversations complete, you can synthesize episodic memories into structured semantic knowledge.

**Process:**
1. Run `/create-memories <episode_id>` command
2. **Semantic Synthesist Agent** analyzes the episode transcript
3. Extracts entities, facts, decisions, patterns, relationships
4. Creates/updates semantic memory files organized by entity type
5. **Semantic Synthesist Reviewer** validates the output
6. Approved memories are committed to version control

**Example Entity Classifications:**
- People (`people/`)
- Projects (`projects/`)
- Technologies (`technologies/frameworks/`, `technologies/tools/`, `technologies/libraries/`)
- Agents (`agents/`)
- Companies (`companies/`)
- Concepts (`concepts/`)

**Example Semantic Memory File:**
```markdown
---
name: project-alpha
entity_classification: project
status: active
created: 2025-09-29T10:30:00Z
last_updated: 2025-09-29T10:30:00Z
source_episodes:
  - 250929_EP_1
summary: A gamification project using React and Vite
relationships:
  - type: uses
    entity: react
    description: Frontend framework for Project Alpha
    source: 250929_EP_1
---

## Facts

### Tech Stack
- Uses Vite + React + TypeScript + Tailwind CSS [250929_EP_1]
- Chose Shadcn/ui for the design system [250929_EP_1]

## Decisions

- **Design System: Shadcn/ui over Mantine** [250929_EP_1]
  - **Category:** Technology Choices
  - **Rationale:** Full customization and ownership of component code
  - **Impact:** More control over animations and gamification aesthetics
```

### 3. Relationship Typology

The system maintains a controlled vocabulary of relationship types to ensure consistency across the knowledge graph.

**Relationship Categories:**
- **Hierarchical:** manages, reports_to, is_part_of, contains
- **Associative:** collaborates_with, works_on, uses, prefers
- **Influence:** influences, depends_on, enables, guides
- **Action-based:** proposed, decided_on, completed, designed

See `.claude/agents/memory/relationship-typology.yaml` for the complete list.

## Getting Started

### Prerequisites

- Claude Code installed
- Python 3.11+
- `uv` (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd cc-semantic-memory
```

2. Start Claude Code in this directory:
```bash
claude
```

The memory system is now active! Conversation capture begins automatically.

### First Use

The repository includes example memories to demonstrate the structure:
- **Episodic:** `.claude/agents/memory/episodic/2025/09/250929_EP_1.json`
- **Semantic:** `.claude/agents/memory/semantic/` (various entity files)

**To start fresh:**
1. Delete `.claude/agents/memory/episodic/` contents
2. Delete `.claude/agents/memory/semantic/` contents
3. Keep `.claude/agents/memory/relationship-typology.yaml`

### Creating Semantic Memories

After having a conversation:

1. Note the episode ID from the session start message (e.g., `250929_EP_1`)
2. Run the create-memories command:
```
/create-memories 250929_EP_1
```

3. The system will:
   - Launch the Semantic Synthesist agent
   - Analyze the transcript and extract knowledge
   - Create/update semantic memory files
   - Launch the Reviewer agent to validate output
   - Commit approved changes to git

## Project Structure

```
.
├── .claude
│  ├── agents
│  │  ├── memory
│  │  │  ├── episodic
│  │  │  │  └── 2025
│  │  │  │     └── 09
│  │  │  │        ├── 250929_EP_1.json (example episodic memory file)
│  │  │  ├── relationship-typology.yaml
│  │  │  └── semantic (examples of semantic memory files)
│  │  ├── semantic-synthesist-reviewer.md
│  │  └── semantic-synthesist.md
│  ├── commands
│  │  ├── create-memories.md
│  ├── hooks
│  │  ├── config
│  │  │  └── hooks_config.yaml
│  │  ├── hook_entry.py
│  │  ├── pid
│  │  │  └── random_session_ids
│  │  │     └── conversation_watchdog.pid
│  │  ├── tasks
│  │  │  ├── cleanup_subprocesses
│  │  │  │  └── main.py
│  │  │  └── conversation_capture
│  │  │     ├── conversation_watchdog.py
│  │  │     └── main.py
│  │  └── utils
│  │     └── hooks_config.py
│  ├── patterns
│  │  └── memory
│  │     └── semantic-memory_pattern.md
│  ├── settings.json
├── .gitignore
├── CLAUDE.md
└── README.md
```
## Configuration

### Hooks Configuration

Edit `.claude/hooks/config/hooks_config.yaml` to customize:

**Conversation Capture:**
```yaml
session_start:
  conversation_capture:
    enabled: true
    config:
      episodic_path: ".claude/agents/memory/episodic"
      human_name: "Saito"           # Your name
      agent_name: "The Architect"   # Claude's persona name
```

**Subprocess Cleanup:**
```yaml
session_end:
  cleanup_subprocesses:
    enabled: true
```

## Semantic Memory Patterns

Semantic memories follow a standardized structure defined in `.claude/patterns/memory/semantic-memory_pattern.md`:

**YAML Frontmatter:**
- Entity metadata (name, classification, status)
- Source episode references
- Relationship mappings
- Timestamps and aliases

**Content Sections:**
- **Facts:** Objective, verifiable information
- **Decisions:** Conclusive choices with rationale
- **Actions:** Assigned tasks and commitments
- **Accomplishments:** Completed goals and milestones
- **Suggestions:** Ideas offered for consideration
- **Preferences:** Expressed partialities
- **Requirements:** Necessary conditions
- **Constraints:** Boundaries and limitations
- **Philosophies:** Guiding principles
- **Patterns:** Recurring behaviors
- **Approaches:** Conscious strategies

Each item includes source episode notation: `[<episode_id>]`

## Commands

### `/create-memories <episode_id>`

Synthesizes semantic knowledge from an episodic memory transcript.

**Arguments:**
- `<episode_id>`: The episode identifier (e.g., `250929_EP_1`)

**Process:**
1. Retrieves timestamp
2. Tasks the Semantic Synthesist agent with the episode
3. Tasks the Reviewer agent to validate output
4. Returns the final review report

## Agents

### Semantic Synthesist

**Role:** Translates episodic conversations into structured semantic knowledge

**Model:** Claude Opus (for deep analysis)

**Capabilities:**
- Linguistic analysis and entity extraction
- Context and subtext interpretation
- Relationship mapping
- Knowledge synthesis and integration
- Disambiguation and conflict resolution

**Tools:** Read, Write, Glob

### Semantic Synthesist Reviewer

**Role:** Quality assurance for semantic memories

**Model:** Claude Sonnet (for efficient validation)

**Capabilities:**
- Pattern adherence validation
- Relationship consistency checks
- Source episode verification
- YAML frontmatter validation
- Status management and git commits

**Tools:** Read, Glob, Grep, MultiEdit, Bash

## Technical Details

### Episodic Memory Format

- **Format:** JSON with ordered conversation data
- **Ordering:** Uses numeric chains (1, 2, 3) and subchains (2.1, 2.2)
- **Speakers:** Identified by name from hook configuration
- **Operations:** `response` (communications) and tool operations (actions)

### Semantic Memory Lifecycle

**Statuses:**
- `new` - Recently created, pending review
- `updated` - Modified with new information
- `active` - Approved and current
- `review-needed` - Failed validation, needs correction
- `archived` - No longer current but retained for history

### Git Integration

The Reviewer agent automatically commits semantic memory changes:
- Stages new/updated files individually
- Commits with descriptive messages
- Updates status after review
- Maintains atomic commit discipline

## Best Practices

1. **Review episodes before synthesis** - Ensure conversations contain valuable information
2. **Use descriptive entity names** - Follow kebab-case naming (e.g., `project-alpha`)
3. **Verify relationships** - Check that entity files exist for all relationship targets
4. **Maintain typology** - Add new relationship types rather than creating similar ones
5. **Source everything** - Always include episode references for facts and decisions
6. **Keep episodes** - Don't delete episodic memories after synthesis (they're the source of truth)
7. **Regular commits** - Let the Reviewer commit changes incrementally

## License

[Specify your license]

## Contributing

[Specify contribution guidelines if applicable]