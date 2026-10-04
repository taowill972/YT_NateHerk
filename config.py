from pathlib import Path

# Paths
BASE_DIR = Path("/root/YT_NateHerk")
REPO_DIR = BASE_DIR
TRANSCRIPTS_DIR = BASE_DIR / "YT_NateHerk_Transcript"
CATALOG_FILE = BASE_DIR / "catalog.json"
STATE_FILE = BASE_DIR / "state.json"
WORK_DIR = Path("/tmp/yt_nateherk_work")
SCREENSHOTS_DIR = BASE_DIR / "screenshots"
LOG_FILE = Path("/var/log/yt_nateherk.log")

# Channel Information
CHANNEL_ID = "UC2ojq-nuP8ceeHqiroeKhBA"
CHANNEL_NAME = "Nate Herk | AI Automation"
CHANNEL_HANDLE = "@nateherk"
CHANNEL_URL = "https://www.youtube.com/@nateherk/featured"
RSS_FEED_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
CHANNEL_DOMAIN = "AI Automation, Agents IA, Claude Code, Opus 5.5, Codex, Workflows Autonomes, Make, n8n, Intelligence Artificielle Appliquée"

# Models
AUDIO_GEMINI_MODEL = "gemini-3.5-flash-lite"
AUDIO_FALLBACK_MODELS = ["gemini-3.8-flash", "gemini-2.5-flash-lite"]
WHISPER_MODEL = "large-v3-turbo"

VISUAL_GEMINI_MODEL = "gemini-3.5-flash-lite"
VISUAL_FALLBACK_MODELS = ["gemini-2.5-flash-lite"]

MODEL_SIGNATURE = f"whisper-v3-large-turbo+{VISUAL_GEMINI_MODEL}"

# API Keys & Network
AUDIO_KEYS_FILE = BASE_DIR / "gemini_audio_keys.txt"
VISUAL_KEYS_FILE = BASE_DIR / "gemini_visual_keys.txt"
PROXY = "socks5://127.0.0.1:4001"
PLAYER_CLIENT = "android"

# Processing parameters
BATCH_SIZE = 7
MAX_BLOCK_DURATION = 32.0
MIN_BLOCK_DURATION = 18.0
FRAME_DIFF_THRESHOLD = 15.0
FRAME_MAX_WIDTH = 1280

# Ensure directories exist
BASE_DIR.mkdir(parents=True, exist_ok=True)
TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
WORK_DIR.mkdir(parents=True, exist_ok=True)
