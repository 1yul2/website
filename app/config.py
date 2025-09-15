import os

class Config:
    """환경 설정 (로컬 SQLite 기본값)"""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///instance/reviews.db")
