#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "watchdog",
# ]
# ///
"""
Claude Code Transcript Capture
Watches a Claude Code transcript file (JSONL) and incrementally processes new objects
into simplified conversation files (JSON) - NOW WITH EVENT-DRIVEN MONITORING!
"""

import json
import sys
import argparse
import time
import os
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass

# NEW: Import watchdog components
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


@dataclass
class ConversationMessage:
    """Simplified conversation message structure"""

    id: str  # Format: order + "-" + first_5_digits_of_uuid
    parent_id: Optional[str]
    timestamp: str
    speaker: str
    operation: str
    message: str
    is_sidechain: bool
    chain_id: Optional[str] = None  # To track which branch conversation this belongs to
    uuid: str = ""  # Keep original UUID for internal processing
    order: str = ""  # Keep order for internal processing
    original_parent_uuid: Optional[str] = None  # Keep original parent UUID for relationship processing
    original_chain_id: Optional[str] = None  # Keep original chain UUID for relationship processing


# NEW: Create a dedicated event handler class
class TranscriptChangeHandler(FileSystemEventHandler):
    """Handles file system events for the transcript file."""

    def __init__(self, capturer, input_filepath: str, output_filepath: str):
        self.capturer = capturer
        self.input_filepath = os.path.abspath(input_filepath)
        self.output_filepath = output_filepath

    def on_modified(self, event):
        """
        This method is called by watchdog when a file is modified.
        """
        # We only care about modifications to our specific input file
        if (
            not event.is_directory
            and os.path.abspath(event.src_path) == self.input_filepath
        ):
            print(f"Detected change in {self.input_filepath}")
            try:
                # Use the existing processing logic from the capturer
                new_objects = self.capturer._read_new_objects(self.input_filepath)

                if new_objects:
                    print(f"Processing {len(new_objects)} new objects...")
                    self.capturer._process_new_objects(new_objects)
                    self.capturer._update_output_file(self.output_filepath)
                    print(
                        f"Updated {self.output_filepath} with {len(new_objects)} new conversations"
                    )

            except Exception as e:
                print(f"Error during processing event: {e}", file=sys.stderr)


class TranscriptCapturer:
    def __init__(self, human_name: str = "Human", primary_agent: str = "Assistant"):
        self.human_name = human_name
        self.primary_agent = primary_agent
        self.conversations: List[ConversationMessage] = []
        self.all_objects: List[Dict[str, Any]] = []
        self.processed_objects_count = 0  # Track how many objects we've processed

        # Maps for tracking relationships
        self.task_to_chain_mapping: Dict[str, str] = {}  # Maps task prompt to task UUID
        self.chain_to_agent_mapping: Dict[
            str, str
        ] = {}  # Maps chain UUID to agent name
        self.tool_errors: Dict[str, bool] = {}  # Maps tool_use UUID to error status
        self.tool_use_mapping: Dict[
            str, Dict[str, Any]
        ] = {}  # Maps tool_use_id to tool details

    # CHANGED: Replaced the polling loop with an event-driven setup
    def start_watching(self, input_filepath: str, output_filepath: str):
        """Watch input file for changes using an event-driven observer."""
        print(f"Starting to watch {input_filepath} for changes...")
        print(f"Output will be written to {output_filepath}")

        # Ensure output directory exists
        Path(output_filepath).parent.mkdir(parents=True, exist_ok=True)

        # Initialize output file if it doesn't exist
        if not Path(output_filepath).exists():
            self._write_initial_output(output_filepath)

        # --- Initial processing for any content that already exists ---
        if Path(input_filepath).exists():
            print("Processing existing content in input file...")
            new_objects = self._read_new_objects(input_filepath)
            if new_objects:
                self._process_new_objects(new_objects)
                self._update_output_file(output_filepath)
                print(f"Initial processing complete. Found {len(new_objects)} objects.")

        # --- Setup watchdog observer ---
        event_handler = TranscriptChangeHandler(self, input_filepath, output_filepath)
        observer = Observer()
        # Watch the DIRECTORY of the input file, as observers work on directories
        watch_dir = os.path.dirname(os.path.abspath(input_filepath))
        observer.schedule(event_handler, watch_dir, recursive=False)

        print(f"Now watching directory '{watch_dir}' for events...")
        observer.start()

        try:
            # Keep the main thread alive, the observer is running in the background
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopping file watcher...")
            observer.stop()

        observer.join()

    # REMOVED: The old watch_and_process method is gone.
    # The logic from its loop is now in TranscriptChangeHandler.on_modified.

    def _write_initial_output(self, output_filepath: str):
        """Write initial empty output file"""
        initial_output = {
            "metadata": [
                ["generated_at", int(time.time())],
                ["message_count", 0],
                ["primary_chain_count", 0],
                ["sidechain_count", 0],
            ],
            "conversations_headers": [
                "id",
                "order",
                "parent_id",
                "timestamp",
                "speaker",
                "operation",
                "message",
            ],
            "conversations_data": [],
        }

        with open(output_filepath, "w") as f:
            json.dump(initial_output, f, separators=(",", ":"))

    def _read_new_objects(self, filepath: str) -> List[Dict[str, Any]]:
        """Read only new objects from the file since last processing"""
        try:
            with open(filepath, "r") as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            return []

        # Parse all JSON objects from content
        json_objects = []
        current_obj = ""
        brace_count = 0

        for char in content:
            current_obj += char
            if char == "{":
                brace_count += 1
            elif char == "}":
                brace_count -= 1
                if brace_count == 0 and current_obj.strip():
                    # We've completed a JSON object
                    try:
                        obj = json.loads(current_obj.strip())
                        json_objects.append(obj)
                    except json.JSONDecodeError as e:
                        print(f"Error parsing JSON object: {e}", file=sys.stderr)
                        print(
                            f"Object (first 200 chars): {current_obj[:200]}",
                            file=sys.stderr,
                        )
                    current_obj = ""

        # Return only new objects
        new_objects = json_objects[self.processed_objects_count :]
        return new_objects

    def _process_new_objects(self, new_objects: List[Dict[str, Any]]):
        """Process new objects and add them to conversations"""
        # Add new objects to our collection
        self.all_objects.extend(new_objects)

        # Update processed count
        self.processed_objects_count = len(self.all_objects)

        # Re-identify task chains and tool errors with all objects
        self._identify_task_chains()
        self._identify_tool_errors()

        # Process only the new objects, but with context of all objects
        new_conversations = []
        for obj in new_objects:
            conv_msg = self._process_object(obj)
            if conv_msg:
                new_conversations.append(conv_msg)

        # Add new conversations to our collection
        self.conversations.extend(new_conversations)

        # Re-process relationships for all conversations
        self._fix_parent_uuids()
        self._propagate_chain_ids()
        self._assign_conversation_order()
        self._generate_compact_ids()

        # Sort all conversations by order
        self.conversations.sort(key=lambda x: self._parse_order_for_sorting(x.order))

    def _update_output_file(self, output_filepath: str):
        """Update the output file with current conversations"""
        output_data = self._format_conversation_output(self.conversations)

        with open(output_filepath, "w") as f:
            json.dump(output_data, f, separators=(",", ":"))

    def _identify_task_chains(self):
        """First pass: identify Task operations and map them to chains"""
        for obj in self.all_objects:
            message = obj.get("message", {})
            if isinstance(message, dict):
                content = message.get("content", [])
                if isinstance(content, list):
                    for item in content:
                        if (
                            isinstance(item, dict)
                            and item.get("type") == "tool_use"
                            and item.get("name") == "Task"
                        ):
                            task_uuid = obj.get("uuid", "")
                            task_input = item.get("input", {})
                            prompt = task_input.get("prompt", "")
                            subagent = task_input.get("subagent_type", "Agent")

                            # Map the prompt to the task UUID
                            self.task_to_chain_mapping[prompt] = task_uuid
                            # Map the task UUID to the agent name
                            self.chain_to_agent_mapping[task_uuid] = subagent

    def _identify_tool_errors(self):
        """Second pass: identify tool errors from tool results"""
        for obj in self.all_objects:
            message_type = obj.get("type", "")
            if message_type == "user":
                message = obj.get("message", {})
                if isinstance(message, dict):
                    content = message.get("content", [])
                    if isinstance(content, list):
                        for item in content:
                            if (
                                isinstance(item, dict)
                                and item.get("type") == "tool_result"
                            ):
                                is_error = item.get("is_error", False)
                                parent_uuid = obj.get("parentUuid")
                                if parent_uuid and is_error:
                                    self.tool_errors[parent_uuid] = True

    def _propagate_chain_ids(self):
        """Propagate chain_ids through sidechain conversations and update speakers"""
        # First restore original chain_ids
        for conv in self.conversations:
            if conv.original_chain_id is not None:
                conv.chain_id = conv.original_chain_id

        # Build a map of UUID to conversation message
        uuid_to_conv = {conv.uuid: conv for conv in self.conversations}

        # Find all sidechain starts and propagate their chain_id
        for conv in self.conversations:
            if conv.is_sidechain and conv.chain_id:
                # Propagate this chain_id to all children in the sidechain
                self._propagate_chain_id_to_children(
                    uuid_to_conv, conv.uuid, conv.chain_id
                )

        # Update speakers for sidechain assistant messages
        for conv in self.conversations:
            if conv.is_sidechain and conv.chain_id and conv.speaker == "Agent":
                if conv.chain_id in self.chain_to_agent_mapping:
                    conv.speaker = self.chain_to_agent_mapping[conv.chain_id]

    def _fix_parent_uuids(self):
        """Fix parent UUIDs to point to valid parents that weren't filtered out"""
        # Create a map of UUID to conversation message for quick lookup
        uuid_to_conv = {conv.uuid: conv for conv in self.conversations}

        # Create a map of UUID to raw object for traversing the original chain
        uuid_to_raw = {
            obj.get("uuid", ""): obj for obj in self.all_objects if obj.get("uuid")
        }

        for conv in self.conversations:
            # Reset parent_id to original parent UUID before processing
            conv.parent_id = conv.original_parent_uuid

            # parent_id currently stores the original parent_uuid
            if conv.parent_id and conv.parent_id not in uuid_to_conv:
                # Parent was filtered out, find the next valid parent up the chain
                new_parent_uuid = self._find_valid_parent(
                    conv.parent_id, uuid_to_raw, uuid_to_conv
                )
                conv.parent_id = (
                    new_parent_uuid  # Store the corrected parent UUID temporarily
                )

    def _find_valid_parent(
        self,
        current_parent_uuid: Optional[str],
        uuid_to_raw: Dict[str, Dict[str, Any]],
        uuid_to_conv: Dict[str, ConversationMessage],
    ) -> Optional[str]:
        """Recursively find the closest valid parent that wasn't filtered out"""
        if not current_parent_uuid:
            return None

        # If the current parent exists in our conversations, we're done
        if current_parent_uuid in uuid_to_conv:
            return current_parent_uuid

        # Otherwise, find the parent of the filtered-out object and continue searching
        if current_parent_uuid in uuid_to_raw:
            raw_obj = uuid_to_raw[current_parent_uuid]
            next_parent_uuid = raw_obj.get("parentUuid")
            return self._find_valid_parent(next_parent_uuid, uuid_to_raw, uuid_to_conv)

        return None

    def _generate_compact_ids(self):
        """Generate compact IDs based on UUID prefixes, keep order separate"""
        # Create a mapping from UUID to conversation for parent lookups
        uuid_to_conv = {conv.uuid: conv for conv in self.conversations}

        for conv in self.conversations:
            # Generate compact ID: just the first 5 characters of UUID
            uuid_prefix = conv.uuid[:5] if conv.uuid else "00000"
            conv.id = uuid_prefix

            # Generate compact parent_id if parent exists (format: order-uuid_prefix for lookup)
            if conv.parent_id and conv.parent_id in uuid_to_conv:
                parent_conv = uuid_to_conv[conv.parent_id]
                parent_uuid_prefix = (
                    parent_conv.uuid[:5] if parent_conv.uuid else "00000"
                )
                # Store the compact parent ID with its order for now
                conv.parent_id = f"{parent_conv.order}-{parent_uuid_prefix}"
            elif conv.parent_id:
                # Parent doesn't exist in our conversations, set to None
                conv.parent_id = None

            # Convert chain_id to just the order of the originating task
            if conv.chain_id and conv.chain_id in uuid_to_conv:
                chain_conv = uuid_to_conv[conv.chain_id]
                # For chain_id, just use the order of the originating task
                conv.chain_id = chain_conv.order
            elif conv.chain_id:
                # Chain ID doesn't exist in our conversations, keep as None
                conv.chain_id = None

    def _assign_conversation_order(self):
        """Assign order numbers to conversations - primary chain (1,2,3...) and sidechain (task.1, task.2...)"""
        # First restore original chain_ids
        for conv in self.conversations:
            if conv.original_chain_id is not None:
                conv.chain_id = conv.original_chain_id

        # Sort all conversations by timestamp first
        all_conversations = sorted(self.conversations, key=lambda x: x.timestamp)

        # Track order counters
        primary_order = 1
        chain_order_map = {}  # chain_id -> next order number for that chain
        uuid_to_conv = {conv.uuid: conv for conv in self.conversations}

        for conv in all_conversations:
            if not conv.is_sidechain:
                # Primary chain: simple sequential numbering
                conv.order = str(primary_order)
                primary_order += 1
            else:
                # Sidechain: find the originating task and number sequentially
                if conv.chain_id:
                    # Find the task that created this chain
                    task_conv = uuid_to_conv.get(conv.chain_id)
                    if task_conv and hasattr(task_conv, "order") and task_conv.order:
                        # Initialize chain order if not exists
                        if conv.chain_id not in chain_order_map:
                            chain_order_map[conv.chain_id] = 1

                        # Extract base order number (just the number part, not sub-levels)
                        base_order = (
                            task_conv.order.split(".")[0]
                            if "." in task_conv.order
                            else task_conv.order
                        )
                        conv.order = f"{base_order}.{chain_order_map[conv.chain_id]}"
                        chain_order_map[conv.chain_id] += 1
                    else:
                        # Fallback if we can't find the task
                        conv.order = f"unknown.{primary_order}"
                        primary_order += 1
                else:
                    # No chain_id, fallback ordering
                    conv.order = f"unknown.{primary_order}"
                    primary_order += 1

    def _parse_order_for_sorting(self, order: str) -> tuple:
        """Parse order string for proper sorting (e.g., '2.1' -> (2, 1))"""
        if not order:
            return (float("inf"),)

        try:
            parts = order.replace("unknown.", "999.").split(".")
            return tuple(int(part) for part in parts)
        except ValueError:
            # Fallback for non-numeric parts
            return (float("inf"),)

    def _propagate_chain_id_to_children(
        self,
        uuid_to_conv: Dict[str, ConversationMessage],
        parent_uuid: str,
        chain_id: str,
    ):
        """Recursively propagate chain_id to all children"""
        for conv in self.conversations:
            # parent_id currently stores the original parent_uuid during processing
            if conv.parent_id == parent_uuid and conv.is_sidechain:
                conv.chain_id = chain_id
                conv.original_chain_id = chain_id  # Also preserve the original
                # Recursively propagate to its children
                self._propagate_chain_id_to_children(uuid_to_conv, conv.uuid, chain_id)

    def _process_object(self, obj: Dict[str, Any]) -> Optional[ConversationMessage]:
        """Process a single conversation object"""
        # Skip system messages
        if obj.get("type") == "system":
            return None

        # Skip meta messages
        if obj.get("isMeta", False):
            return None

        # Skip TodoWrite operations
        if self._is_todo_write(obj):
            return None

        # Skip tool result messages (they're handled separately)
        if self._is_tool_result(obj):
            return None

        uuid = obj.get("uuid", "")
        parent_uuid = obj.get("parentUuid")
        timestamp = obj.get("timestamp", "")
        is_sidechain = obj.get("isSidechain", False)

        # Determine chain_id
        chain_id = self._determine_chain_id(obj)

        # Determine speaker
        speaker = self._determine_speaker(obj, is_sidechain, chain_id)

        # Extract operation and message based on content
        operation, message = self._extract_operation_and_message(obj)

        # Check if this is a tool use that had an error
        if uuid in self.tool_errors and message:
            message = f"FAILED: {message}"

        if operation and message:
            conv_msg = ConversationMessage(
                id="",  # Will be generated later
                parent_id="",  # Will be generated later
                timestamp=timestamp,
                speaker=speaker,
                operation=operation,
                message=message,
                is_sidechain=is_sidechain,
                chain_id=chain_id,
                uuid=uuid,  # Keep for internal processing
                order="",  # Will be assigned later
                original_parent_uuid=parent_uuid,  # Store original parent UUID
                original_chain_id=chain_id  # Store original chain UUID
            )
            # Store parent_uuid temporarily for processing
            conv_msg.parent_id = (
                parent_uuid  # Store temporarily, will be converted later
            )
            return conv_msg

        return None

    def _determine_chain_id(self, obj: Dict[str, Any]) -> Optional[str]:
        """Determine the chain_id for a conversation object"""
        is_sidechain = obj.get("isSidechain", False)
        parent_uuid = obj.get("parentUuid")

        if is_sidechain:
            if parent_uuid is None:
                # This is the start of a sidechain
                # Check if this content matches a Task prompt
                message = obj.get("message", {})
                if isinstance(message, dict):
                    content = message.get("content", "")
                    if (
                        isinstance(content, str)
                        and content in self.task_to_chain_mapping
                    ):
                        return self.task_to_chain_mapping[content]
            # Chain ID will be propagated later
        return None

    def _determine_speaker(
        self, obj: Dict[str, Any], is_sidechain: bool, chain_id: Optional[str]
    ) -> str:
        """Determine the speaker based on rules"""
        message_type = obj.get("type", "")

        if not is_sidechain:
            # Primary conversation chain
            if message_type == "user":
                return self.human_name
            elif message_type == "assistant":
                return self.primary_agent
        else:
            # Branch conversation chain
            if message_type == "user":
                return self.primary_agent
            elif message_type == "assistant":
                # Try to find the agent name from the chain_id
                if chain_id and chain_id in self.chain_to_agent_mapping:
                    return self.chain_to_agent_mapping[chain_id]
                return "Agent"  # Default if we can't determine

        return "System"

    def _is_todo_write(self, obj: Dict[str, Any]) -> bool:
        """Check if this is a TodoWrite operation"""
        message = obj.get("message", {})
        if isinstance(message, dict):
            content = message.get("content", [])
            if isinstance(content, list):
                for item in content:
                    if isinstance(item, dict):
                        if (
                            item.get("type") == "tool_use"
                            and item.get("name") == "TodoWrite"
                        ):
                            return True
        return False

    def _is_tool_result(self, obj: Dict[str, Any]) -> bool:
        """Check if this is a tool result message"""
        message_type = obj.get("type", "")
        if message_type == "user":
            message = obj.get("message", {})
            if isinstance(message, dict):
                content = message.get("content", [])
                if isinstance(content, list):
                    for item in content:
                        if isinstance(item, dict) and item.get("type") == "tool_result":
                            return True
        return False

    def _extract_operation_and_message(self, obj: Dict[str, Any]) -> Tuple[str, str]:
        """Extract operation and message from conversation object"""
        message = obj.get("message", {})

        if not isinstance(message, dict):
            return "", ""

        content = message.get("content")

        # Handle string content
        if isinstance(content, str):
            return "response", content

        # Handle array content
        if isinstance(content, list):
            for item in content:
                if not isinstance(item, dict):
                    continue

                item_type = item.get("type", "")

                # Handle text content
                if item_type == "text":
                    return "response", item.get("text", "")

                # Handle tool use
                if item_type == "tool_use":
                    tool_name = item.get("name", "")
                    tool_id = item.get("id", "")
                    tool_input = item.get("input", {})

                    # Store tool mapping for later reference
                    self.tool_use_mapping[tool_id] = {
                        "name": tool_name,
                        "input": tool_input,
                    }

                    return self._process_tool_use(tool_name, tool_input)

                # Skip tool results - they are handled separately
                if item_type == "tool_result":
                    continue

        # Handle direct content if it's neither string nor list
        elif isinstance(content, dict):
            content_type = content.get("type", "")
            if content_type == "text":
                return "response", content.get("text", "")

        return "", ""

    def _process_tool_use(
        self, tool_name: str, tool_input: Dict[str, Any]
    ) -> Tuple[str, str]:
        """Process tool use based on rules"""
        if tool_name == "Task":
            subagent = tool_input.get("subagent_type", "Agent")
            description = tool_input.get("description", "")
            return (
                "Tool:Task",
                f"Going to chat with Agent({subagent}). Topic: {description}",
            )

        elif tool_name == "Read":
            file_path = tool_input.get("file_path", "")
            return "Tool:Read", f"Reading the file at {file_path}"

        elif tool_name == "Write":
            file_path = tool_input.get("file_path", "")
            return "Tool:Write", f"Writing a file at {file_path}"

        elif tool_name == "Bash":
            command = tool_input.get("command", "")
            description = tool_input.get("description", "")
            message = f"Running Bash command `{command}`"
            if description:
                message += f". Focus: {description}"
            return "Tool:Bash", message

        elif tool_name in ["MultiEdit", "Edit"]:
            file_path = tool_input.get("file_path", "")
            return f"Tool:{tool_name}", f"Editing the file at {file_path}"

        elif tool_name == "WebFetch":
            url = tool_input.get("url", "")
            return "Tool:WebFetch", f"Fetching the URL {url}"

        elif tool_name == "WebSearch":
            query = tool_input.get("query", "")
            return "Tool:WebSearch", f"Searching the web for {query}"

        elif tool_name == "Glob":
            pattern = tool_input.get("pattern", "")
            return "Tool:Glob", f"Searching for files matching {pattern}"

        elif tool_name == "Grep":
            pattern = tool_input.get("pattern", "")
            return "Tool:Grep", f"Searching for patterns matching {pattern}"

        elif tool_name.startswith("mcp"):
            # MCP tools
            custom_fields = json.dumps(tool_input)
            return f"Tool:{tool_name}", f"Running MCP with {custom_fields}"

        elif tool_name == "TodoWrite":
            return "", ""  # Ignore TodoWrite

        else:
            # Unknown tool
            return (
                f"Tool:{tool_name}",
                f"Running {tool_name} with input: {json.dumps(tool_input)}",
            )

    def _format_conversation_output(
        self, conversations: List[ConversationMessage]
    ) -> Dict[str, Any]:
        """Format conversations for JSON output as array of arrays"""
        import time

        # Convert conversations to array of arrays format
        headers = [
            "id",
            "order",
            "parent_id",
            "timestamp",
            "speaker",
            "operation",
            "message",
        ]
        data = []

        for conv in conversations:
            # Convert ISO timestamp to Unix timestamp
            try:
                from datetime import datetime

                dt = datetime.fromisoformat(conv.timestamp.replace("Z", "+00:00"))
                unix_timestamp = int(dt.timestamp())
            except:
                unix_timestamp = int(time.time())  # Fallback to current time

            # Extract only the 5-character UUID part from parent_id (after the hyphen)
            parent_id = conv.parent_id
            if parent_id and "-" in parent_id:
                parent_id = parent_id.split("-", 1)[
                    1
                ]  # Take everything after the first hyphen

            row = [
                conv.id,  # Just the 5-character UUID prefix
                conv.order,  # The order as a separate field
                parent_id,  # Now just the 5-character UUID part
                unix_timestamp,
                conv.speaker,
                conv.operation,
                conv.message,
            ]
            data.append(row)

        # Format metadata as array of arrays
        current_unix_time = int(time.time())
        metadata = [
            ["generated_at", current_unix_time],
            ["message_count", len(conversations)],
            [
                "primary_chain_count",
                sum(1 for c in conversations if not c.is_sidechain),
            ],
            ["sidechain_count", sum(1 for c in conversations if c.is_sidechain)],
        ]

        output = {
            "metadata": metadata,
            "conversations_headers": headers,
            "conversations_data": data,
        }
        return output


def main():
    parser = argparse.ArgumentParser(
        description="Watch Claude Code transcript files and incrementally convert to conversation format"
    )
    parser.add_argument(
        "input", type=str, help="Input JSONL transcript file path to watch"
    )
    parser.add_argument("output", type=str, help="Output JSON file path")
    parser.add_argument(
        "--human",
        type=str,
        default="Human",
        help="Name for human speaker (default: Human)",
    )
    parser.add_argument(
        "--agent",
        type=str,
        default="Assistant",
        help="Name for primary agent (default: Assistant)",
    )
    parser.add_argument(
        "--test-once",
        action="store_true",
        help="Process the file once and exit (for testing)"
    )

    args = parser.parse_args()

    # Create capturer instance
    capturer = TranscriptCapturer(human_name=args.human, primary_agent=args.agent)

    try:
        if args.test_once:
            # Process the file once for testing
            capturer._write_initial_output(args.output)
            if Path(args.input).exists():
                new_objects = capturer._read_new_objects(args.input)
                if new_objects:
                    capturer._process_new_objects(new_objects)
                    capturer._update_output_file(args.output)
                    print(f"Processed {len(new_objects)} objects and wrote to {args.output}")
                else:
                    print("No objects found in input file")
            else:
                print(f"Input file {args.input} does not exist")
        else:
            # CHANGED: Call the new watching method
            capturer.start_watching(args.input, args.output)
    except Exception as e:
        print(f"Error during capture: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
