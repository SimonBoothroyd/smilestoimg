import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):

    API_DEV_STR: str = "/api/dev"

    ACCESS_TOKEN: str = secrets.token_urlsafe(32)


settings = Settings()
