from . import db

class Review(db.Model):
    """리뷰 모델: 책/영화 제목, 리뷰 내용, 별점"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # 제목
    content = db.Column(db.Text, nullable=False)       # 리뷰 내용
    rating = db.Column(db.Integer, nullable=False)     # 별점 (1~5)
