# 📘 Flask 미니 프로젝트 – 책/영화 리뷰 노트

<br/>

## 🎯 목표
- Flask로 CRUD 기능 전체 구현
- SQLite + SQLAlchemy DB 연동 복습
- 템플릿(Jinja2)으로 UI 구성
- ⭐ 평균 별점 계산 기능 추가

<br/>

## 📝 기능 요구사항
1. 리뷰 작성 (Create)
   - 제목(책/영화 이름), 리뷰 내용, 별점(1~5) 입력
2. 리뷰 목록 보기 (Read)
   - 전체 리뷰 리스트 출력
   - ⭐ 평균 별점 표시
3. 리뷰 수정 (Update)
   - 기존 리뷰 내용/별점 수정
4. 리뷰 삭제 (Delete)
   - 리뷰 삭제 버튼

<br/>

## 🏗️ 프로젝트 구조
```plaintext
review_app/
 ├── app/
 │   ├── __init__.py       # Flask 초기화 + DB 연결
 │   ├── models.py         # Review 모델 정의
 │   ├── routes.py         # 라우트 (목록, 작성, 수정, 삭제)
 │   ├── templates/
 │   │    ├── index.html   # 리뷰 목록 & 평균 별점
 │   │    ├── new.html     # 리뷰 작성 폼
 │   │    ├── edit.html    # 리뷰 수정 폼
 │   └── static/           # CSS, JS & 여기서는 사용 x
 ├── instance/
 │   └── reviews.db        # ⚠️ SQLite 파일: 로컬에서 프로그램 실행 시 자동으로 생성
 ├── run.py                # 실행 스크립트
 └── requirements.txt
```
