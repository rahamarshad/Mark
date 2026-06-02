# System Overview

## Complete Architecture

MARK XXXIX is a Python desktop assistant. It combines:

- A PyQt6 desktop UI.
- A Gemini Live voice session.
- Microphone input and speaker output through `sounddevice`.
- Gemini function calling for tools.
- Local JSON memory.
- A queue-based agent system for larger multi-step tasks.
- Many local action modules for apps, files, browser control, screen analysis, reminders, media, and code help.

## Startup Sequence

1. `main.py` runs `main()`.
2. `JarvisUI` from `ui.py` creates the PyQt6 window.
3. A background thread waits for API setup with `ui.wait_for_api_key()`.
4. If `config/api_keys.json` is missing or incomplete, the UI shows the setup overlay.
5. After setup, `JarvisLive` starts.
6. `JarvisLive.run()` creates a Gemini client and opens a live audio session.
7. Four async tasks run together:
   - send microphone audio to Gemini
   - read microphone audio
   - receive Gemini responses/tool calls
   - play Gemini audio output

## Voice Pipeline

Input:

1. `sounddevice.InputStream` records microphone PCM audio.
2. Audio chunks are pushed into `out_queue`.
3. `_send_realtime()` sends chunks to Gemini Live as `audio/pcm`.

Output:

1. `_receive_audio()` receives audio bytes from Gemini.
2. Audio bytes are pushed into `audio_in_queue`.
3. `_play_audio()` writes bytes to `sounddevice.RawOutputStream`.
4. UI state changes between `LISTENING`, `THINKING`, and `SPEAKING`.

Transcripts:

- Gemini input transcription is logged as `You: ...`.
- Gemini output transcription is logged as `Jarvis: ...`.

## Memory Pipeline

Main files:

- `memory/memory_manager.py`
- `memory/long_term.json`

Flow:

1. `load_memory()` reads `memory/long_term.json`.
2. `_build_config()` in `main.py` formats memory into the system instruction.
3. Gemini can call the `save_memory` tool.
4. `_execute_tool()` handles `save_memory` silently.
5. `update_memory()` writes categorized facts back to JSON.

Categories:

- `identity`
- `preferences`
- `projects`
- `relationships`
- `wishes`
- `notes`

## Tool Execution Pipeline

1. Tool schemas are declared in `TOOL_DECLARATIONS` inside `main.py`.
2. Gemini chooses a function call.
3. `_receive_audio()` sees `response.tool_call`.
4. `_execute_tool()` dispatches by tool name.
5. Most tools run in an executor thread so the live session does not block.
6. Tool output is wrapped in `types.FunctionResponse`.
7. Gemini receives the tool result and continues the conversation.

Important tool modules:

- `actions/open_app.py`
- `actions/browser_control.py`
- `actions/file_controller.py`
- `actions/file_processor.py`
- `actions/screen_processor.py`
- `actions/computer_control.py`
- `actions/computer_settings.py`
- `actions/web_search.py`
- `actions/code_helper.py`
- `actions/dev_agent.py`
- `actions/reminder.py`

## Agent Pipeline

Main files:

- `agent/planner.py`
- `agent/task_queue.py`
- `agent/executor.py`
- `agent/error_handler.py`

Flow:

1. Gemini calls `agent_task` for complex multi-step work.
2. `TaskQueue.submit()` queues the goal.
3. `AgentExecutor.execute()` asks `planner.py` for steps.
4. Each step calls a tool through `_call_tool()`.
5. Failed steps can be retried, skipped, replanned, or aborted.

## Important Files

- `main.py`: live session, tool schemas, tool dispatch, audio pipeline.
- `ui.py`: PyQt6 desktop interface and first-run setup overlay.
- `core/prompt.txt`: main assistant behavior instructions.
- `config/api_keys.json`: local API key and OS selection.
- `memory/memory_manager.py`: persistent memory logic.
- `actions/*`: tool implementations.
- `agent/*`: multi-step planning and execution.
- `requirements-macos.txt`: macOS dependency list.
- `setup.py`: dependency/bootstrap installer.

## Files Safe To Modify

- `core/prompt.txt`
- `requirements-macos.txt`
- `SETUP_CHECKLIST.md`
- `TEST_RESULTS.md`
- `SYSTEM_OVERVIEW.md`
- `CUSTOMIZATION_OPPORTUNITIES.md`
- Individual `actions/*` files when fixing a specific tool
- `memory/memory_manager.py` when improving memory behavior

## Files To Modify Carefully

- `main.py`: central runtime and tool dispatch.
- `ui.py`: large UI file with many connected widgets and signals.
- `agent/executor.py`: can run generated code and local tools.
- `actions/computer_control.py`: controls mouse, keyboard, and screen.
- `actions/file_controller.py`: reads/writes/moves/deletes user files.

## Files That Should Not Be Committed With Secrets

- `config/api_keys.json`
- `memory/long_term.json`

