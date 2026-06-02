# Branding Changes

## Pre-Change Visible Branding Report

This report focuses on user-visible `JARVIS`, `Jarvis`, and dotted `J.A.R.V.I.S` branding. Non-visible class names, internal task names, comments, original attribution, and architecture references are intentionally not included as changes.

| File | Location | Text displayed | Type | Planned action |
| --- | --- | --- | --- | --- |
| `ui.py` | line 456 | `J.A.R.V.I.S` | Main UI canvas label | Replace with `ASTRA` |
| `ui.py` | line 736 | `Select a file for JARVIS` | File picker dialog title | Replace with `Select a file for ASTRA` |
| `ui.py` | line 891 | `Configure J.A.R.V.I.S. before first boot.` | Setup overlay label | Replace with `Configure ASTRA before first boot.` |
| `ui.py` | line 993 | `J.A.R.V.I.S — MARK XXXIX` | Window title | Replace with `ASTRA — MARK XXXIX` |
| `ui.py` | line 1142 | `J.A.R.V.I.S` | Main UI title | Replace with `ASTRA` |
| `ui.py` | line 1363 | `Tell JARVIS what to do with it` | File upload hint | Replace with `Tell ASTRA what to do with it` |
| `ui.py` | line 1448 | `SYS: Initialised. OS=... JARVIS online.` | Setup status log | Replace with `ASTRA online` |
| `main.py` | line 784 | `Jarvis: ...` | Conversation transcript label | Replace with `ASTRA: ...` |
| `main.py` | line 862 | `SYS: JARVIS online.` | Startup status log | Replace with `SYS: ASTRA online.` |
| `actions/weather_report.py` | line 49 | `JARVIS: ...` | Weather tool UI log prefix | Replace with `ASTRA: ...` |
| `actions/screen_processor.py` | line 348 | `Jarvis: ...` | Vision transcript label | Replace with `ASTRA: ...` |
| `actions/flight_finder.py` | line 241 | `JARVIS — Flight Search Results` | Saved report heading | Replace with `ASTRA — Flight Search Results` |
| `actions/youtube_video.py` | line 120 | `J.A.R.V.I.S` | URL prompt dialog title | Replace with `ASTRA` |
| `actions/youtube_video.py` | line 191 | `JARVIS — YouTube Summary` | Saved summary heading | Replace with `ASTRA — YouTube Summary` |
| `actions/reminder.py` | lines 52, 60, 88, 96, 111, 121 | `J.A.R.V.I.S Reminder` | Notification title | Replace with `ASTRA Reminder` |

## Left Unchanged On Purpose

| File | Text | Reason |
| --- | --- | --- |
| `main.py` | `JarvisUI`, `JarvisLive`, console `[JARVIS]` diagnostics | Internal code names / developer logs, not UI rebrand scope. |
| `main.py` | fallback prompt text | Hidden behavior prompt, not a visible UI label. |
| `core/prompt.txt` | `JARVIS CORE PROTOCOL` | Prompt architecture, not UI text. |
| `readme.md` | original project mentions | Original attribution/documentation kept. |
| `SYSTEM_OVERVIEW.md` | architecture references | Documentation/architecture kept. |
| `actions/*` task names such as `JARVISReminder`, `JARVIS_GameUpdater`, `JarvisProjects` | Internal identifiers and scheduled task names; changing could affect behavior or compatibility. |
| `actions/file_processor.py` header comment | Comment referencing original tool name. |

## Applied Changes

| File | Visible change |
| --- | --- |
| `ui.py` | Main canvas label changed from `J.A.R.V.I.S` to `ASTRA`. |
| `ui.py` | File picker dialog changed from `Select a file for JARVIS` to `Select a file for ASTRA`. |
| `ui.py` | Setup overlay changed from `Configure J.A.R.V.I.S. before first boot.` to `Configure ASTRA before first boot.` |
| `ui.py` | Window title changed from `J.A.R.V.I.S — MARK XXXIX` to `ASTRA — MARK XXXIX`. |
| `ui.py` | Main UI title changed from `J.A.R.V.I.S` to `ASTRA`. |
| `ui.py` | File hint changed from `Tell JARVIS what to do with it` to `Tell ASTRA what to do with it`. |
| `ui.py` | Setup status log changed from `JARVIS online` to `ASTRA online`. |
| `main.py` | Assistant transcript label changed from `Jarvis:` to `ASTRA:`. |
| `main.py` | Startup status log changed from `SYS: JARVIS online.` to `SYS: ASTRA online.` |
| `actions/weather_report.py` | Weather UI log prefix changed from `JARVIS:` to `ASTRA:`. |
| `actions/screen_processor.py` | Vision transcript label changed from `Jarvis:` to `ASTRA:`. |
| `actions/flight_finder.py` | Saved flight report heading changed from `JARVIS — Flight Search Results` to `ASTRA — Flight Search Results`. |
| `actions/youtube_video.py` | URL prompt title changed from `J.A.R.V.I.S` to `ASTRA`. |
| `actions/youtube_video.py` | Saved YouTube summary heading changed from `JARVIS — YouTube Summary` to `ASTRA — YouTube Summary`. |
| `actions/reminder.py` | Reminder notification titles changed from `J.A.R.V.I.S Reminder` to `ASTRA Reminder`. |
