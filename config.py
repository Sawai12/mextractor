import os

class Config(object):
    # Load sensitive information from environment variables for security
    BOT_TOKEN = os.environ.get("BOT_TOKEN")  # Token to authenticate the bot with Telegram
    API_ID = int(os.environ.get("API_ID"))   # API ID required for accessing Telegram's API (must be an integer)
    API_HASH = os.environ.get("API_HASH")    # API hash key for Telegram API access, used along with API_ID

    # Admin User IDs (these are unique identifiers for Telegram users with admin privileges)
    ADMIN = '6801378994,6825628464'.split(',')  # Admin user IDs as strings; can add or remove IDs here
    ADMIN_ID = [int(id) for id in ADMIN]  # Convert admin user IDs to integers for consistent ID format

    # Database connection details
    DB_URL = os.environ.get("DB_URL")      # Database URL for connecting to the bot’s database
    DB_NAME = os.environ.get("DB_NAME")    # Name of the database to be used by the bot

    # Telegram Channels for logging different types of bot activity (these IDs refer to specific Telegram channels)
    TXT_LOG = -1002052406049  # Channel ID for logging decrypted text, used for monitoring
    AUTH_LOG = -1002443617338 # Channel ID for notifications when a new user is granted authorization
    CHANNEL = -1002203633085  # ID of the official bot channel, for user updates or forced joining requirements
    HIT_LOG = -1002054849699  # Channel ID for tracking account "hits" or access attempts to the bot
    THUMB_URL = "https://telegra.ph/file/0c9ba36b87dea56546299.jpg" #Replace by with your Thumb URL