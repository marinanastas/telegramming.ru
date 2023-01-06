import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME", "flask_user")
    MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD", "flask_password")
    MONGODB_HOSTNAME = os.environ.get("MONGODB_HOSTNAME", "mongodb")
    MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE", "flask_db")
    MONGODB_PROTOCOL = os.environ.get("MONGODB_PROTOCOL", "mongodb")
    MONGODB_PORT = os.environ.get("MONGODB_PORT", "27017")

    MONGODB_FULLHOST = MONGODB_HOSTNAME if MONGODB_PROTOCOL == "mongodb+srv" else f"{MONGODB_HOSTNAME}:{MONGODB_PORT}"

    MONGO_URI = os.environ.get("MONGO_URI", None) or f"{MONGODB_PROTOCOL}://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_FULLHOST}/{MONGODB_DATABASE}"
