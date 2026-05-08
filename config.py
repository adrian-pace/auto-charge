from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    easee_email: str
    easee_password: str
    easee_charger_id: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
