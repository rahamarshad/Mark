# Setup Checklist

## Completed Locally

- Installed Homebrew Python 3.12.
- Created project virtual environment at `.venv/`.
- Installed macOS system dependencies:
  - `portaudio`
  - `ffmpeg`
- Installed Python dependencies from `requirements-macos.txt`.
- Installed Playwright browser binaries.
- Created `config/api_keys.example.json`.
- Created local `config/api_keys.json` with `os_system` set to `mac` and an empty Gemini key.

## Missing Credentials

The app needs one required credential:

```json
{
  "gemini_api_key": "YOUR_GEMINI_API_KEY",
  "os_system": "mac"
}
```

Add it in one of two ways:

1. Launch the app and enter the key in the setup screen.
2. Edit `config/api_keys.json` and replace the empty `gemini_api_key` value.

## Required Service

- Google Gemini API access.
- The code uses:
  - Gemini Live audio model in `main.py` and `actions/screen_processor.py`.
  - Gemini text models in planner, error handler, code helper, file processor, computer settings, desktop, and web search.

## macOS Permissions To Grant

When macOS prompts, allow the terminal/app running the project to access:

- Microphone
- Accessibility
- Screen Recording
- Automation

Without these permissions, voice input, computer control, screen analysis, and some automation tools may fail.

## Run Command

```bash
cd /Users/rahamarshad7/Desktop/Astra
.venv/bin/python main.py
```
