import os

# Config File for CBML Bot
# ANY ISSUES FOUND IN THIS FILE SHOULD BE REPORTED TO @CANTARELLA_WUWA IN TELEGRAM

# Helper functions for type casting environment variables
def get_env_bool(key, default=False):
    val = os.getenv(key)
    if val is None:
        return default
    return val.strip().lower() in ("true", "1", "t", "yes")

def get_env_int(key, default=0):
    val = os.getenv(key)
    try:
        return int(val) if val else default
    except ValueError:
        return default

# Required Variables
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = get_env_int("OWNER_ID", 0)
TELEGRAM_API = get_env_int("TELEGRAM_API", 0)
TELEGRAM_HASH = os.getenv("TELEGRAM_HASH", "")

# Optional Configuration
ALLDEBRID_API_KEY = os.getenv("ALLDEBRID_API_KEY", "")
ALLDEBRID_NO_SEED_TIMEOUT = get_env_int("ALLDEBRID_NO_SEED_TIMEOUT", 180)
AS_DOCUMENT = get_env_bool("AS_DOCUMENT", False)
AUTHORIZED_CHATS = os.getenv("AUTHORIZED_CHATS", "")
BASE_URL = os.getenv("BASE_URL", "")
HELPER_TOKENS = os.getenv("HELPER_TOKENS", "")
HELPER_STRINGS = os.getenv("HELPER_STRINGS", "")
STREAM_TOKENS = os.getenv("STREAM_TOKENS", "")
HELPER_BOT_PROXIES = os.getenv("HELPER_BOT_PROXIES", "")
HELPER_USER_PROXIES = os.getenv("HELPER_USER_PROXIES", "")
BOT_MAX_TASKS = get_env_int("BOT_MAX_TASKS", 0)
BOT_PM = get_env_bool("BOT_PM", False)
CMD_SUFFIX = os.getenv("CMD_SUFFIX", "")
DEFAULT_LANG = os.getenv("DEFAULT_LANG", "en")
DATABASE_URL = os.getenv("DATABASE_URL", "")
DEFAULT_UPLOAD = os.getenv("DEFAULT_UPLOAD", "rc")
DELETE_LINKS = get_env_bool("DELETE_LINKS", False)
DEBRID_LINK_API = os.getenv("DEBRID_LINK_API", "")
DISABLE_TORRENTS = get_env_bool("DISABLE_TORRENTS", False)
DISABLE_LEECH = get_env_bool("DISABLE_LEECH", False)
DISABLE_MIRROR = get_env_bool("DISABLE_MIRROR", False)
DISABLE_BULK = get_env_bool("DISABLE_BULK", False)
DISABLE_MULTI = get_env_bool("DISABLE_MULTI", False)
DISABLE_SEED = get_env_bool("DISABLE_SEED", False)
DISABLE_FF_MODE = get_env_bool("DISABLE_FF_MODE", False)
DISABLE_MEGA = get_env_bool("DISABLE_MEGA", False)
DISABLE_PLUGINS = get_env_bool("DISABLE_PLUGINS", False)
DISABLE_JD = get_env_bool("DISABLE_JD", True)
DISABLE_NZB = get_env_bool("DISABLE_NZB", True)
DISABLE_SEEDR = get_env_bool("DISABLE_SEEDR", True)
DISABLE_RSS = get_env_bool("DISABLE_RSS", False)
DISABLE_SEARCH = get_env_bool("DISABLE_SEARCH", False)
DISABLE_STREAM = get_env_bool("DISABLE_STREAM", False)
DISABLE_YTDLP = get_env_bool("DISABLE_YTDLP", False)
ENABLE_ENCODE = get_env_bool("ENABLE_ENCODE", True)
ENABLE_COMPRESS = get_env_bool("ENABLE_COMPRESS", True)
ENABLE_WATERMARK = get_env_bool("ENABLE_WATERMARK", True)
ENABLE_FFMPEG_CMDS = get_env_bool("ENABLE_FFMPEG_CMDS", True)
THUMBNAIL = os.getenv("THUMBNAIL", "")
PLUGIN_INDEXES = []
EQUAL_SPLITS = get_env_bool("EQUAL_SPLITS", False)
EXCLUDED_EXTENSIONS = os.getenv("EXCLUDED_EXTENSIONS", "")
FFMPEG_CMDS = {}
FFMPEG_DUMP = {}
FILELION_API = os.getenv("FILELION_API", "")
MEDIA_STORE = get_env_bool("MEDIA_STORE", True)
FORCE_SUB_IDS = os.getenv("FORCE_SUB_IDS", "")
GOFILE_API = os.getenv("GOFILE_API", "")
GOFILE_FOLDER_ID = os.getenv("GOFILE_FOLDER_ID", "")
GOFILE_AUTO_CREATE_FOLDER = get_env_bool("GOFILE_AUTO_CREATE_FOLDER", False)
PIXELDRAIN_KEY = os.getenv("PIXELDRAIN_KEY", "")
PROTECTED_API = os.getenv("PROTECTED_API", "")
BUZZHEAVIER_API = os.getenv("BUZZHEAVIER_API", "")
DEVUPLOADS_KEY = os.getenv("DEVUPLOADS_KEY", "")
DEVUPLOADS_FOLDER = os.getenv("DEVUPLOADS_FOLDER", "")
VIKINGFILE_HASH = os.getenv("VIKINGFILE_HASH", "")
VIKINGFILE_FOLDER = os.getenv("VIKINGFILE_FOLDER", "")
GDRIVE_ID = os.getenv("GDRIVE_ID", "")
GD_DESP = os.getenv("GD_DESP", "Uploaded with Sitaratoons Bots")
AUTHOR_NAME = os.getenv("AUTHOR_NAME", "Luffytaro")
AUTHOR_URL = os.getenv("AUTHOR_URL", "https://t.me/Og_Luffytaro")
INSTADL_API = os.getenv("INSTADL_API", "")
IMDB_TEMPLATE = os.getenv("IMDB_TEMPLATE", "")
IMAGES = [
    "https://i.pinimg.com/564x/b5/6a/22/b56a229148586984a9333522caa533b9.jpg",
    "https://i.pinimg.com/736x/00/64/e5/0064e52ee1fbe13a1d58645dd968a286.jpg",
    "https://i.pinimg.com/736x/eb/dd/9e/ebdd9ef30457d32bd5ee0b9c22606078.jpg",
    "https://i.pinimg.com/736x/ff/3e/0a/ff3e0a570aa6fdc2c3d2d291e3d6a4a8.jpg",
    "https://i.pinimg.com/736x/d1/39/bf/d139bfbcfb71af1e9e2ff8afca32201c.jpg",
    "https://i.pinimg.com/564x/4c/e6/c2/4ce6c2b18fca27227e8262d16b3c4855.jpg",
    "https://i.pinimg.com/564x/48/ea/00/48ea0003ab040bf6395fee71220a4420.jpg",
    "https://i.pinimg.com/736x/33/5b/17/335b17b76f53d46ab8c95063222b8074.jpg",
    "https://i.pinimg.com/564x/fb/eb/af/fbebafee28eed8b1b776673e545830b4.jpg",
    "https://i.pinimg.com/564x/87/18/2b/87182be3e5d4a482a0f10083131aab6e.jpg",
]
IMG_SEARCH = os.getenv("IMG_SEARCH", "")
IMG_PAGE = get_env_int("IMG_PAGE", 1)
USE_IMAGES = get_env_bool("USE_IMAGES", True)
IMG_SOURCES = ["wallpaperflare"]
INC_TASK_NOTIFY = get_env_bool("INC_TASK_NOTIFY", False)
INC_TASK_RESUME = get_env_bool("INC_TASK_RESUME", False)
INDEX_URL = os.getenv("INDEX_URL", "")
IS_TEAM_DRIVE = get_env_bool("IS_TEAM_DRIVE", False)
JD_EMAIL = os.getenv("JD_EMAIL", "")
JD_PASS = os.getenv("JD_PASS", "")
MEGA_EMAIL = os.getenv("MEGA_EMAIL", "")
MEGA_PASSWORD = os.getenv("MEGA_PASSWORD", "")
SEEDR_EMAIL = os.getenv("SEEDR_EMAIL", "")
SEEDR_PASSWORD = os.getenv("SEEDR_PASSWORD", "")
SEEDR_DELETE_FOLDER = get_env_bool("SEEDR_DELETE_FOLDER", False)
DIRECT_LIMIT = get_env_int("DIRECT_LIMIT", 0)
MEGA_LIMIT = get_env_int("MEGA_LIMIT", 0)
TORRENT_LIMIT = get_env_int("TORRENT_LIMIT", 0)
GD_DL_LIMIT = get_env_int("GD_DL_LIMIT", 0)
RC_DL_LIMIT = get_env_int("RC_DL_LIMIT", 0)
CLONE_LIMIT = get_env_int("CLONE_LIMIT", 0)
JD_LIMIT = get_env_int("JD_LIMIT", 0)
NZB_LIMIT = get_env_int("NZB_LIMIT", 0)
SEEDR_LIMIT = get_env_int("SEEDR_LIMIT", 0)
YTDLP_LIMIT = get_env_int("YTDLP_LIMIT", 0)
PLAYLIST_LIMIT = get_env_int("PLAYLIST_LIMIT", 0)
LEECH_LIMIT = get_env_int("LEECH_LIMIT", 0)
EXTRACT_LIMIT = get_env_int("EXTRACT_LIMIT", 0)
ARCHIVE_LIMIT = get_env_int("ARCHIVE_LIMIT", 0)
STORAGE_LIMIT = get_env_int("STORAGE_LIMIT", 0)
LEECH_LOG_CHAT = os.getenv("LEECH_LOG_CHAT", "")
LEECH_DUMP_CHATS = {}
LINKS_LOG_ID = os.getenv("LINKS_LOG_ID", "")
MIRROR_LOG_ID = os.getenv("MIRROR_LOG_ID", "")
LEECH_PREFIX = os.getenv("LEECH_PREFIX", "")
LEECH_CAPTION = os.getenv("LEECH_CAPTION", "")
LEECH_SUFFIX = os.getenv("LEECH_SUFFIX", "")
LEECH_FONT = os.getenv("LEECH_FONT", "")
LEECH_SPLIT_SIZE = get_env_int("LEECH_SPLIT_SIZE", 2097152000)
MEDIA_GROUP = get_env_bool("MEDIA_GROUP", False)
USE_HYPER = get_env_bool("USE_HYPER", True)
HYPER_THREADS = get_env_int("HYPER_THREADS", 0)
HYPER_PIPELINE = get_env_int("HYPER_PIPELINE", 64)
HYPER_CHUNK = get_env_int("HYPER_CHUNK", 8 * 1024 * 1024)
MEM_BUDGET = get_env_int("MEM_BUDGET", 0)
MEM_DEEP_STATS = get_env_bool("MEM_DEEP_STATS", False)
STREAM_PIPELINE = get_env_int("STREAM_PIPELINE", 32)
STREAM_CHUNK = get_env_int("STREAM_CHUNK", 2097152)
STREAM_PER_CLIENT = get_env_int("STREAM_PER_CLIENT", 12)
STREAM_GATE = get_env_int("STREAM_GATE", 96)
CPU_LIMIT = get_env_int("CPU_LIMIT", 20)
FFMPEG_CORES = os.getenv("FFMPEG_CORES", "auto")
THROTTLE_SERVICES = os.getenv("THROTTLE_SERVICES", "auto")
HYDRA_IP = os.getenv("HYDRA_IP", "")
HYDRA_API_KEY = os.getenv("HYDRA_API_KEY", "")
NAME_SWAP = os.getenv("NAME_SWAP", "")
PROGRESS_BAR = os.getenv("PROGRESS_BAR", "■□")
QUEUE_ALL = get_env_int("QUEUE_ALL", 0)
QUEUE_DOWNLOAD = get_env_int("QUEUE_DOWNLOAD", 0)
QUEUE_UPLOAD = get_env_int("QUEUE_UPLOAD", 0)
RCLONE_FLAGS = os.getenv("RCLONE_FLAGS", "")
RCLONE_PATH = os.getenv("RCLONE_PATH", "")
RCLONE_SERVE_URL = os.getenv("RCLONE_SERVE_URL", "")
SHOW_CLOUD_LINK = get_env_bool("SHOW_CLOUD_LINK", True)
RCLONE_SERVE_USER = os.getenv("RCLONE_SERVE_USER", "")
RCLONE_SERVE_PASS = os.getenv("RCLONE_SERVE_PASS", "")
RCLONE_SERVE_PORT = get_env_int("RCLONE_SERVE_PORT", 8081)
RSS_CHAT = os.getenv("RSS_CHAT", "")
RSS_DELAY = get_env_int("RSS_DELAY", 600)
RSS_SIZE_LIMIT = get_env_int("RSS_SIZE_LIMIT", 0)
SEARCH_API_LINK = os.getenv("SEARCH_API_LINK", "")
SEARCH_LIMIT = get_env_int("SEARCH_LIMIT", 0)
SEARCH_PLUGINS = []
SET_COMMANDS = get_env_bool("SET_COMMANDS", True)
STATUS_LIMIT = get_env_int("STATUS_LIMIT", 10)
STATUS_UPDATE_INTERVAL = get_env_int("STATUS_UPDATE_INTERVAL", 5)
STOP_DUPLICATE = get_env_bool("STOP_DUPLICATE", False)
STREAMWISH_API = os.getenv("STREAMWISH_API", "")
SUDO_USERS = os.getenv("SUDO_USERS", "")
TG_PROXY = None
THUMBNAIL_LAYOUT = os.getenv("THUMBNAIL_LAYOUT", "")
TMDB_ACCESS_TOKEN = os.getenv("TMDB_ACCESS_TOKEN", "")
AUTO_THUMBNAIL = get_env_bool("AUTO_THUMBNAIL", False)
VERIFY_TIMEOUT = get_env_int("VERIFY_TIMEOUT", 0)
LOGIN_PASS = os.getenv("LOGIN_PASS", "")
TORRENT_TIMEOUT = get_env_int("TORRENT_TIMEOUT", 0)
TIMEZONE = os.getenv("TIMEZONE", "Asia/Kolkata")
USER_MAX_TASKS = get_env_int("USER_MAX_TASKS", 0)
USER_TIME_INTERVAL = get_env_int("USER_TIME_INTERVAL", 0)
UPLOAD_PATHS = {}
DRIVE_CATEGORY_MODE = get_env_bool("DRIVE_CATEGORY_MODE", False)
DRIVE_CATEGORY_SA = os.getenv("DRIVE_CATEGORY_SA", "")
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/shinubo28always/WZML")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
USENET_SERVERS = []
USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "")
TRANSMISSION_MODE = os.getenv("TRANSMISSION_MODE", "both")
USE_SERVICE_ACCOUNTS = get_env_bool("USE_SERVICE_ACCOUNTS", False)
ENABLE_TELEMETRY = get_env_bool("ENABLE_TELEMETRY", True)
WEB_ACCESS_PASSWORD = os.getenv("WEB_ACCESS_PASSWORD", "")
WEB_PINCODE = get_env_bool("WEB_PINCODE", True)
YT_DLP_OPTIONS = {}
YT_DESP = os.getenv("YT_DESP", "Uploaded with Unrated Coder")
YT_TAGS = ["telegram", "bot", "youtube"]
YT_CATEGORY_ID = get_env_int("YT_CATEGORY_ID", 22)
YT_PRIVACY_STATUS = os.getenv("YT_PRIVACY_STATUS", "unlisted")
