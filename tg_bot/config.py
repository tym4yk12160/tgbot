from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 339279683  # my telegram ID
    OWNER_USERNAME = "Fopstal"  # my telegram username
    API_KEY = "763040691:AAFzYvYGoQy0WbfWx2sefTY-3qkxfwv-DxE"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "")  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
