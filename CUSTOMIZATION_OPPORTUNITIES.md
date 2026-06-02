# Customization Opportunities

## Features That Can Be Improved

- Split `main.py` into smaller modules:
  - live session
  - tool declarations
  - tool dispatch
  - audio pipeline
  - app startup
- Split `ui.py` into focused UI components.
- Add safer confirmation prompts for destructive tools.
- Add a settings screen for API key, OS, voice, microphone, and permissions.
- Add a built-in diagnostics screen for dependency, audio, and credential checks.

## Missing Functionality

- No clear test suite.
- No structured logging file.
- No plugin system for third-party tools.
- No per-tool permission model.
- No profile switching.
- No simple non-voice fallback mode for debugging the AI session.

## Potential AI Upgrades

- Move all Gemini SDK usage to `google.genai`.
- Add a text-only debug mode that uses a cheaper text model before enabling live audio.
- Add model configuration in `config/api_keys.json` or a separate settings file.
- Add structured tool result schemas so Gemini receives cleaner tool output.
- Add better retries for temporary model/network failures.

## Better Memory Systems

- Separate user profile memory from temporary session notes.
- Add timestamps and source messages for every saved memory.
- Add explicit memory review/edit/delete UI.
- Store memory in SQLite instead of one JSON file.
- Add memory scopes:
  - personal
  - project
  - device
  - temporary session

## Better Voice Systems

- Add a microphone selector.
- Add a speaker/output selector.
- Add a push-to-talk mode.
- Add a text-only fallback if microphone permission fails.
- Add local wake-word support.
- Add visible audio meters for input and output.

## Multi-User Support

- Add a `profiles/` directory.
- Store each user in a separate profile folder.
- Keep separate memory, settings, and persona for each user.
- Add a profile picker in the setup overlay.

## Persona Support

- Move persona behavior out of `core/prompt.txt` into data files.
- Let personas define:
  - tone
  - boundaries
  - default tools
  - memory categories
  - preferred voice
  - UI labels
- Add starter personas such as:
  - doctor
  - air hostess
  - student
  - developer
  - creator

## Dashboard Ideas

- Add a setup/health panel:
  - Gemini key present
  - microphone available
  - speaker available
  - Playwright installed
  - macOS permissions status
- Add a memory panel with editable saved facts.
- Add a tool activity timeline.
- Add a current task queue view.
- Add file upload history.
- Add per-tool enable/disable toggles.

