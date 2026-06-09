import os


TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is required")

STREAM_URL = "https://icecast-bulteam.cdnvideo.ru/bolid128"
AD_URL = "https://advradio.ru"

TG_SHOW_URL = "https://t.me/vpsv88"
VK_SHOW_URL = "https://vk.ru/vpsv88"

SITE_URL = "https://bolidfm.ru"
