class development(object):
    development_mode: bool = True

class database(object):
    MONGO_URI: str = None

class basic_settings(object):
    LOGGING: bool = True
    PM_LOGGER_ID: int = None
    PM_LOGGER_BOT_TOKEN: str = None

class Configuration (development, basic_settings, database):
    API_ID: int = None
    API_HASH: str = None
    USER_ID: int = None
    SESSION_STRING: str = None
