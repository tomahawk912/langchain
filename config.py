import os
from dotenv import load_dotenv

load_dotenv()

_config_info = {}

_config_info["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
_config_info["PROXYCURL_API_KEY"] = os.getenv("PROXYCURL_API_KEY")
