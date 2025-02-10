import nautobot
from dotenv import load_dotenv
from mypy_django_plugin import main


def plugin(version):
    load_dotenv("development/dev.env")
    nautobot.setup("development/nautobot_config.py")
    return main.plugin(version)
