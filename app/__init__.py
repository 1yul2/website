from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from app.config import Config  # 🔥 패키지 import

# SQLAlchemy 기본 세팅
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    echo=True,
    connect_args=Config.CONNECT_ARGS
)

SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))
Base = declarative_base()

def create_app():
    """Flask 앱 생성 및 초기화"""
    app = Flask(__name__)

    # 모델 import
    import app.models  # 🔥 절대경로 import 권장

    # 테이블 생성
    Base.metadata.create_all(bind=engine)

    # 라우트 블루프린트 등록
    from app.routes.review_routes import review_bp
    app.register_blueprint(review_bp)

    # 요청 끝날 때 세션 정리
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        SessionLocal.remove()

    return app

# 🔥 Vercel에서 바로 찾을 수 있게 전역 app 객체 생성
app = create_app()
