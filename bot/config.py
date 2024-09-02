from dotenv import load_dotenv
import os
import urllib.parse

os.environ.pop('KEY', None)

os.environ.pop('WELCOME_CHANNEL_ID', None)
os.environ.pop('ALLOWED_CHANNELS', None)

os.environ.pop('EMBED_COLOR', None)

load_dotenv()

KEY = os.getenv("KEY")

WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID"))
ALLOWED_CHANNELS = [int(channel) for channel in os.getenv("ALLOWED_CHANNELS", "").split(",") if channel]

EMBED_COLOR = int(os.getenv("EMBED_COLOR"), 16)
