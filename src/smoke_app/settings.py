from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = "127.0.0.1"
    server_port: int = 8000
    database_url: str = "postgresql://user:123qwe@db:5432/smoke_app_db"


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8')

