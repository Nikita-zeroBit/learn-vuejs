from pydantic import BaseSettings


class APISettings(BaseSettings):
    postgres_db: str = 'test'
    postgres_user: str = 'postgres'
    postgres_password: str = 'postgres'
    postgres_host: str = 'localhost'
    postgres_port: int = 5432
    


settings = APISettings()
