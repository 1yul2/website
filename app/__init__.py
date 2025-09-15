from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy 객체 생성 (DB 연결용)
db = SQLAlchemy()

def create_app():
    """Flask 앱 생성 + 설정 + 블루프린트 등록"""
    app = Flask(__name__)

    # SQLite 데이터베이스 설정
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # DB 초기화
    db.init_app(app)

    # 블루프린트 등록
    from .routes import main
    app.register_blueprint(main)

    # 앱 컨텍스트 안에서 DB 테이블 생성
    with app.app_context():
        db.create_all()

    return app
