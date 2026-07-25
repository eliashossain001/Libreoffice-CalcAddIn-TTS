# 🔊 Bangla TTS Add-in for LibreOffice Calc

A LibreOffice Calc extension, written in Python using the UNO API, that reads Bangla spreadsheet content aloud. Select a cell range, click **Play**, and the add-in converts the text to speech through a self-hosted TTS inference service. It also converts legacy Bijoy (ANSI) encoded Bangla text to Unicode in place.

## ✨ Features

- **Text-to-speech for cell ranges** — select cells in Calc and play them as natural-sounding Bangla audio
- **Smart text chunking** — long text is split on punctuation and word-count limits so audio starts playing quickly
- **Multi-threaded audio pipeline** — chunks are synthesized concurrently and played back in order
- **ANSI (Bijoy) → Unicode conversion** — fix legacy-encoded Bangla text directly in the selected range
- **Voice options** — dialog controls for gender (male/female) and voice maturity
- **Native LibreOffice dialog** — built with the UNO Dialog Tools (unodit) workflow, launched from `Tools → Add-Ons`

## 📁 Project Structure

```
.
├── extension/                  # LibreOffice extension package
│   ├── src/
│   │   ├── tts_calc.py         # Main add-in: TTS playback + Unicode conversion
│   │   ├── tts_convert.py      # Converter variant of the add-in
│   │   └── pythonpath/         # Generated dialog UI classes
│   ├── META-INF/manifest.xml   # Extension package manifest
│   ├── description.xml         # Extension metadata
│   ├── Addons.xcu              # Tools → Add-Ons menu registration
│   ├── description/            # Title and short description
│   └── registration/           # License text
├── dialogs/
│   └── Default.xdl             # Dialog layout (Basic Dialog Editor format)
├── config.ini                  # unodit project configuration
└── requirements.txt            # Python dependencies
```

## 🛠️ Requirements

- LibreOffice 6+ with Python 3 scripting support
- Python packages (installed into the Python that LibreOffice uses):

```bash
pip install -r requirements.txt
```

- A running TTS inference endpoint that accepts `POST {"text", "model", "gender"}` and returns base64-encoded WAV audio in `{"output": ...}`

## ⚙️ Configuration

The add-in reads the TTS endpoint from the `TTS_API_URL` environment variable (or you can edit the `URL` constant at the top of `extension/src/tts_calc.py`):

```bash
export TTS_API_URL="https://your-tts-server.example.com/infer"
soffice --calc
```

## 🚀 Installation

1. Package the `extension/` directory as an `.oxt` (zip its contents, then rename), or regenerate it with [unodit](https://github.com/kelsa-pi/unodit):

   ```bash
   cd extension && zip -r ../bangla-tts-calc.oxt . && cd ..
   ```

2. Install it via `Tools → Extension Manager → Add`, or from the command line:

   ```bash
   unopkg add bangla-tts-calc.oxt
   ```

3. Restart LibreOffice Calc. The add-in appears under `Tools → Add-Ons → Bangla TTS`.

## 🎯 Usage

1. Open a spreadsheet containing Bangla text.
2. Select the cell range you want to hear.
3. Launch the add-in from `Tools → Add-Ons → Bangla TTS`.
4. Choose voice options, then click **Play**.
5. Use the **Unicode** button to convert Bijoy (ANSI) encoded cells to Unicode in place.

## 🧩 How It Works

1. The selected range's text is collected and split into chunks on punctuation (`। ? ! , ; :` etc.), with long chunks further split at a 20-word limit.
2. Each chunk is sent to the TTS endpoint in its own thread, with automatic retries.
3. Returned base64 WAV audio is decoded with `pydub` and queued.
4. Chunks play back sequentially in original order while later chunks are still being synthesized, minimizing time-to-first-audio.

## 🧪 Development

To debug outside LibreOffice's embedded Python, start LibreOffice with a UNO socket and run the script from your IDE:

```bash
soffice "--accept=socket,host=127.0.0.1,port=2002,tcpNoDelay=1;urp;StarOffice.ComponentContext" --norestore
python3 extension/src/tts_calc.py
```

Dialog UI classes under `extension/src/pythonpath/` are generated from `dialogs/Default.xdl` with [unodit](https://github.com/kelsa-pi/unodit); regenerating them overwrites manual changes.

## 📄 License

The extension scaffolding is based on [UNO Dialog Tools (unodit)](https://github.com/kelsa-pi/unodit), released under the GNU GPL v3.

## 👨‍💼 Author

**Elias Hossain**  
_Machine Learning Researcher | PhD Student | AI x Reasoning Enthusiast_

[![GitHub](https://img.shields.io/badge/GitHub-EliasHossain001-blue?logo=github)](https://github.com/EliasHossain001)
