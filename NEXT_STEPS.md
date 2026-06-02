# Next Steps

## Recommended Rebranding Plan

| Step | Description | Estimated effort |
| --- | --- | --- |
| Choose product identity | Decide final app name, voice/personality direction, logo needs, and attribution wording. | 1-2 hours |
| Documentation rebrand | Rewrite README and setup docs for the fork while preserving original attribution. | 2-4 hours |
| UI text rebrand | Update window title, badges, footer labels, and setup overlay text. | 2-4 hours |
| Config naming cleanup | Replace legacy names in config comments, setup output, and docs. | 1-2 hours |
| Attribution section | Add a clear "Based on / forked from" section linking to the original project. | 30-60 minutes |

## Recommended Architecture Improvements

| Improvement | Why it helps | Estimated effort |
| --- | --- | --- |
| Split `main.py` | Separates Live API, tool registry, audio, config, and startup logic. | 1-2 days |
| Split `ui.py` | Makes UI easier to redesign and test. | 1-3 days |
| Centralize config | One config module for API keys, OS, voice, models, and permissions. | 4-8 hours |
| Tool registry module | Move tool declarations and dispatch out of `main.py`. | 1-2 days |
| Add diagnostics mode | Quickly checks microphone, speaker, Gemini key, Playwright, and permissions. | 1 day |
| Add test suite | Prevents regressions during rebrand and refactor work. | 1-2 days |

## Recommended Future Features

| Feature | Description | Estimated effort |
| --- | --- | --- |
| Persona system | Add profiles like student, clinician, cabin crew, developer, creator. | 1-3 days |
| Better memory manager | Add memory review, deletion, categories, and timestamps. | 1-3 days |
| Multi-user profiles | Separate memory/config/persona per user. | 2-5 days |
| Voice settings UI | Let users choose Gemini Live voice without editing JSON. | 4-8 hours |
| Push-to-talk mode | Better control over when microphone input is sent. | 4-8 hours |
| Text-only debug mode | Test AI/tool behavior without live audio. | 4-8 hours |
| Tool permissions | Confirm destructive actions before file, system, or browser automation. | 1-3 days |
| Dashboard health panel | Show status for API key, mic, speakers, permissions, Playwright, memory. | 1-2 days |

## Suggested Order

1. Finish repository ownership cleanup.
2. Rewrite README for the fork while preserving original attribution.
3. Add diagnostics mode.
4. Centralize config.
5. Add text-only debug mode.
6. Rebrand UI after the product name is final.
