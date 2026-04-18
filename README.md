# 소나기 게시판 (Sonagi Board)

> FastAPI + Supabase + Docker + AWS EC2 기반 웹 게시판 서비스

## 📌 프로젝트 개요

스터디 활동을 위한 웹 기반 게시판 서비스입니다.  
단순 CRUD 구현에 그치지 않고, 클라우드 인프라 환경에서 실제 서비스처럼 설계합니다.

## 🛠️ 기술 스택

| 역할 | 기술 |
|------|------|
| Backend | FastAPI |
| Database | Supabase (PostgreSQL) |
| Authentication | Supabase Auth |
| Container | Docker |
| Deploy | AWS EC2 |
| Web Server | Nginx |

## 📁 프로젝트 구조

```
sonagi/
├── app/
│   ├── main.py           # FastAPI 앱 진입점
│   ├── core/
│   │   └── config.py     # 환경변수 설정
│   ├── routers/
│   │   ├── auth.py       # 인증 라우터
│   │   └── posts.py      # 게시글 라우터
│   └── schemas/
│       ├── auth.py       # 인증 요청/응답 스키마
│       └── posts.py      # 게시글 요청/응답 스키마
├── .env                  # 환경변수 (Git 제외)
├── .gitignore
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## ✨ 주요 기능

- 회원가입 / 로그인 (Supabase Auth)
- 게시글 작성 / 조회 / 수정 / 삭제 (CRUD)
- 사용자 권한에 따른 접근 제어

## 🚀 로컬 실행 방법

### 1. 환경변수 설정

```bash
cp .env.example .env
# .env 파일에 Supabase URL, API Key 등 입력
```

### 2. 가상환경으로 실행

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Docker로 실행

```bash
docker compose up --build
```

서버 실행 후 아래 주소에서 확인:

- API: http://localhost:8000
- Swagger 문서: http://localhost:8000/docs

## 📅 개발 일정

| 주차 | 내용 |
|------|------|
| 1주차 | 프로젝트 기획 |
| 2주차 | 개발 환경 구축 및 기본 구조 설계 |
| 3주차 | 인증 및 DB 연동 |
| 4주차 | 게시판 기능 구현 |
| 5주차 | AWS EC2 배포 |
| 6주차 | 테스트 및 문서 작성 |
| 8주차 | 발표 및 회고 |

## 📄 API 명세

| Method | Endpoint | 설명 |
|--------|----------|------|
| POST | /auth/signup | 회원가입 |
| POST | /auth/login | 로그인 |
| GET | /posts | 게시글 목록 조회 |
| POST | /posts | 게시글 작성 |
| GET | /posts/{id} | 게시글 상세 조회 |
| PUT | /posts/{id} | 게시글 수정 |
| DELETE | /posts/{id} | 게시글 삭제 |

## 👤 담당

- 류상우
