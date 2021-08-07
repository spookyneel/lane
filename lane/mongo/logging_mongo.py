from lane import laneMongo
from config import Configuration

settings = laneMongo.settings

def set_logging(toggle: bool):
    user_data = settings.find_one({'_id': 1})
    if user_data is not None:
        settings.update_one(
            {
                '_id': 1
            },
            {
                '$set': {
                    'logging': toggle
                }
            },
            upsert=True
        )

def is_logging_enabled() -> bool:
    user_data = settings.find_one({'_id': 1})
    if user_data is not None:
        if 'logging' in user_data:
            return user_data['logging']
        else:
            return Configuration.LOGGING
    else:
        return Configuration.LOGGING