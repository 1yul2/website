from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Review

# 블루프린트 생성
main = Blueprint("main", __name__)

@main.route("/")
def index():
    """리뷰 목록 + 평균 별점 페이지"""
    reviews = Review.query.all()

    # 평균 별점 계산 (리뷰 없을 경우 0 처리)
    avg_rating = round(sum([r.rating for r in reviews]) / len(reviews), 1) if reviews else 0

    return render_template("index.html", reviews=reviews, avg_rating=avg_rating)


@main.route("/new", methods=["GET", "POST"])
def new_review():
    """새 리뷰 작성"""
    if request.method == "POST":
        # 폼에서 데이터 가져오기
        title = request.form["title"]
        content = request.form["content"]
        rating = int(request.form["rating"])

        # Review 객체 생성 후 DB에 저장
        review = Review(title=title, content=content, rating=rating)
        db.session.add(review)
        db.session.commit()

        # 저장 후 메인 페이지로 리다이렉트
        return redirect(url_for("main.index"))

    # GET 요청일 경우 → 작성 폼 보여주기
    return render_template("new.html")


@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_review(id):
    """기존 리뷰 수정"""
    review = Review.query.get_or_404(id)

    if request.method == "POST":
        # 폼 데이터로 기존 값 수정
        review.title = request.form["title"]
        review.content = request.form["content"]
        review.rating = int(request.form["rating"])

        db.session.commit()
        return redirect(url_for("main.index"))

    # GET 요청일 경우 → 기존 데이터 채워진 폼 반환
    return render_template("edit.html", review=review)


@main.route("/delete/<int:id>")
def delete_review(id):
    """리뷰 삭제"""
    review = Review.query.get_or_404(id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for("main.index"))
