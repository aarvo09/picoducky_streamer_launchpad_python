# Streamer Launchpad
  
**One-click streaming setup automation - Get live in 30 seconds**

Automates your entire streaming workflow: launches apps (Discord, Steam, Spotify, Browser, StreamLabs), opens YouTube Studio, and arranges windows perfectly.
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![CircuitPython](https://img.shields.io/badge/CircuitPython-Compatible-purple.svg)](https://circuitpython.org/)
[![Built for PicoDucky](https://img.shields.io/badge/Built%20for-PicoDucky-purple)](https://picoducky.hackclub.com/)

## ✨ Features

- 🚀 Auto-launches all streaming apps
- 📺 Opens YouTube Studio dashboard
- 🪟 Arranges windows: YouTube (left) + Discord (right)
- ⚡ Plug-and-play setup
  ## 🎬 Demo Videos

**PicoDucky Version (main.py)**: [Watch Demo](link-to-your-demo-video)

**Windows Version (notmain.py)**: [Watch Demo](link-to-your-demo-video)

## 🛠️ Installation

### For PicoDucky (main.py)

1. Install CircuitPython on Raspberry Pi Pico
2. Copy `adafruit_hid` library to `/lib` folder
3. Edit `main.py` with your apps and YouTube channel URL
4. Copy `main.py` to Pico root directory

### For Windows (notmain.py)

```bash
pip install pyautogui
python notmain.py
```

## ⚙️ Configuration

Edit these variables in `main.py` or `notmain.py`:

```python
STREAMINGAPP = "stream labs"
CHATTINGAPP = "discord"
GAMINGSTORE = "steam"
MUSICAPP = "spotify"
BROWSER = "brave"
URL = "studio.youtube.com/channel/YOUR_CHANNEL_ID"
```

## 📖 Usage

**PicoDucky**: Plug in Pico → Wait 5 seconds → Ready to stream!

**Windows**: Run `python notmain.py`

## 🔧 Troubleshooting

- **Apps not launching?** Check app names match Windows Search exactly
- **Windows not snapping?** Enable Windows Snap in Settings
- **Slow PC?** Increase `time.sleep()` values in the code

## � License

Free to use and modify for personal streaming setups.

---

**Made with ❤️ for streamers**


