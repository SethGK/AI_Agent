## AI Agent

This project features a conversational AI agent that uses the Google Gemini API to interact with a simulated file system. It understands natural language requests and performs actions by calling various tools.

The agent can:
- List files and directories
- Read file contents
- Execute Python files
- Write or overwrite files

It engages in multi-turn conversations, remembering context to complete tasks step-by-step. All file operations are safely confined to a specific working_directory.