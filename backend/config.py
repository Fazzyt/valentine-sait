import json
import logging
from dataclasses import MISSING, dataclass, fields

_DEFAULT_CONFIG_PATH = "config.json"  # Default config file
logger = logging.getLogger(__name__)


@dataclass
class Config:
    API_ID: int
    API_HASH: str
    PHONE_NUMBER: str

    URL_SITE: str
    USE_BOT: bool

    HOST: str
    PORT: int

    DEBUG: bool = False
    
    def __init__(self, config_file_path="config.json") -> None:
        try:
            with open(config_file_path, "r") as config_file:
                config_content = json.load(config_file)
        except FileNotFoundError:
            logger.critical(f"{config_file_path} does not exist!")
            raise
        logging.debug(config_content)
        for field in fields(self):
            val = config_content.get(field.name, field.default)
            if val is MISSING:
                raise ValueError(f"No value for {field.name}")
            logging.debug(f"{field.name}: {val}")
            setattr(self, field.name, val)


config = Config(_DEFAULT_CONFIG_PATH)
