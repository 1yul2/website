from flask import Blueprint, render_template, request, redirect, url_for
from . import SessionLocal
from .models import Review

# Blueprint: 라우트를 모듈화해서 main 블루프린트에 담음
main = Blueprint("main", __name__)

@main.route("/")
def index():
    """
    리뷰 목록 + 평균 별점 출력
    - DB에서 전체 리뷰 조회
    - 평균 별점 계산
    - index.html 템플릿 렌더링
    """
    db = SessionLocal()
    reviews = db.query(Review).all()

    avg_rating = round(sum([r.rating for r in reviews]) / len(reviews), 1) if reviews else 0
    return render_template("index.html", reviews=reviews, avg_rating=avg_rating)


@main.route("/new", methods=["GET", "POST"])
def new_review():
    """
    새 리뷰 작성
    - GET: 입력 폼 보여주기
    - POST: 입력값(title, content, rating) DB에 저장
    """
    db = SessionLocal()
    if request.method == "POST":
        # 폼 데이터 가져오기
        title = request.form["title"]
        content = request.form["content"]
        rating = int(request.form["rating"])

        # 새 Review 객체 생성 → DB 저장
        review = Review(title=title, content=content, rating=rating)
        db.add(review)
        db.commit()

        # 메인 페이지로 리다이렉트
        return redirect(url_for("main.index"))
    return render_template("new.html")


@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_review(id):
    """
    리뷰 수정
    - GET: 기존 리뷰를 불러와 수정 폼에 출력
    - POST: 수정된 내용을 DB에 반영
    """
    db = SessionLocal()
    review = db.query(Review).get(id)

    if request.method == "POST":
        review.title = request.form["title"]
        review.content = request.form["content"]
        review.rating = int(request.form["rating"])
        db.commit()
        return redirect(url_for("main.index"))

    return render_template("edit.html", review=review)


@main.route("/delete/<int:id>")
def delete_review(id):
    """
    리뷰 삭제
    - 특정 id의 리뷰를 DB에서 삭제
    """
    db = SessionLocal()
    review = db.query(Review).get(id)
    db.delete(review)
    db.commit()
    return redirect(url_for("main.index"))
