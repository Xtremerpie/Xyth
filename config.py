import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# BOT
# ==========================================

TOKEN = os.getenv("TOKEN")

BOT_PREFIX = os.getenv(
    "BOT_PREFIX",
    "!"
)

BOT_STATUS = os.getenv(
    "BOT_STATUS",
    "Xyth Community"
)

BOT_ACTIVITY = os.getenv(
    "BOT_ACTIVITY",
    "watching"
)

# ==========================================
# AI
# ==========================================

GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)

# ==========================================
# COLORS
# ==========================================

MAIN_COLOR = int(
    os.getenv("MAIN_COLOR", "0x5865F2"),
    16
)

ERROR_COLOR = int(
    os.getenv("ERROR_COLOR", "0xFF0000"),
    16
)

SUCCESS_COLOR = int(
    os.getenv("SUCCESS_COLOR", "0x00FF00"),
    16
)

# ==========================================
# LEVELING
# ==========================================

XP_PER_MESSAGE = int(
    os.getenv("XP_PER_MESSAGE", 15)
)

LEVEL_MULTIPLIER = int(
    os.getenv("LEVEL_MULTIPLIER", 100)
)

# ==========================================
# ECONOMY
# ==========================================

START_BALANCE = int(
    os.getenv("START_BALANCE", 100)
)

DAILY_REWARD = int(
    os.getenv("DAILY_REWARD", 250)
)

WORK_REWARD_MIN = int(
    os.getenv("WORK_REWARD_MIN", 50)
)

WORK_REWARD_MAX = int(
    os.getenv("WORK_REWARD_MAX", 200)
)

# ==========================================
# AUTOMOD
# ==========================================

SPAM_MESSAGE_LIMIT = int(
    os.getenv("SPAM_MESSAGE_LIMIT", 5)
)

SPAM_TIME_SECONDS = int(
    os.getenv("SPAM_TIME_SECONDS", 5)
)

# ==========================================
# WELCOME
# ==========================================

WELCOME_ENABLED = os.getenv(
    "WELCOME_ENABLED",
    "True"
) == "True"

LEAVE_ENABLED = os.getenv(
    "LEAVE_ENABLED",
    "True"
) == "True"

# ==========================================
# MUSIC
# ==========================================

DEFAULT_VOLUME = float(
    os.getenv("DEFAULT_VOLUME", 0.5)
)