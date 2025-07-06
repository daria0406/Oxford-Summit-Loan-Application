import os
from dotenv import load_dotenv


def setup_environment():
    env_path = os.path.join(os.path.dirname(__file__), '../.env')
    load_dotenv(dotenv_path=env_path)
