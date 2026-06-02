# Voice Options

## Current Voice

The project now reads the Gemini Live voice from:

```json
{
  "gemini_voice_name": "Charon"
}
```

The original hard-coded voice was `Charon`, and the default has been reverted to `Charon`.

Voice configurability is still enabled, so you can test other Gemini Live voices without editing the code.

## Where Voice Is Configured

Voice is configured in `config/api_keys.json`:

```json
{
  "gemini_api_key": "YOUR_KEY",
  "os_system": "mac",
  "gemini_voice_name": "Charon"
}
```

Both Gemini Live sessions read this same setting:

- `main.py`
- `actions/screen_processor.py`

## Available Gemini Live Voices

According to the Google Cloud Gemini Live API voice documentation, `voice_name` currently supports these 30 prebuilt voices:

| Voice | Google description |
| --- | --- |
| Zephyr | Bright |
| Kore | Firm |
| Orus | Firm |
| Autonoe | Bright |
| Umbriel | Easy-going |
| Erinome | Clear |
| Laomedeia | Upbeat |
| Schedar | Even |
| Achird | Friendly |
| Sadachbia | Lively |
| Puck | Upbeat |
| Fenrir | Excitable |
| Aoede | Breezy |
| Enceladus | Breathy |
| Algieba | Smooth |
| Algenib | Gravelly |
| Achernar | Soft |
| Gacrux | Mature |
| Zubenelgenubi | Casual |
| Sadaltager | Knowledgeable |
| Charon | Informative |
| Leda | Youthful |
| Callirrhoe | Easy-going |
| Iapetus | Clear |
| Despina | Smooth |
| Rasalgethi | Informative |
| Alnilam | Firm |
| Pulcherrima | Forward |
| Vindemiatrix | Gentle |
| Sulafat | Warm |

Source: Google Cloud Gemini Live API language and voice documentation, last updated 2026-05-29.

## Recommended Voices To Test

For a calm, polished, Jarvis-inspired assistant feel without cloning any actor:

1. `Charon` - original voice, informative.
2. `Gacrux` - mature, worth testing for a more polished feel.
3. `Rasalgethi` - informative, likely good for assistant-style responses.
4. `Sadaltager` - knowledgeable, good for a composed expert feel.
5. `Algieba` - smooth, worth testing for a softer delivery.
6. `Despina` - smooth, another softer option.
7. `Sulafat` - warm, better if you want less formal delivery.

## How To Change Voice

Edit `config/api_keys.json`:

```json
"gemini_voice_name": "Rasalgethi"
```

Then restart the app:

```bash
.venv/bin/python main.py
```

## Limitations

- Gemini Live provides prebuilt voices, not exact actor voice cloning.
- The project should not clone or imitate any real actor's voice exactly.
- A specific British accent is not guaranteed by `voice_name` alone.
- The current project uses Gemini Live audio, so voice quality and style are controlled by Gemini's available Live API voices.
- For more exact voice direction later, a dedicated TTS system could be evaluated, but ElevenLabs or other external TTS providers are intentionally not added yet.
