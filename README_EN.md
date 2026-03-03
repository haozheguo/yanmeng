# Yanmeng Project | Postgraduate Exam Information Platform

<p align="center">
  <a href="docs/media/yanemengvideo15mbcrop1.mp4">
    <img src="docs/images/ppt/image5.png" alt="Yanmeng Demo Video Cover" width="90%" />
  </a>
</p>

<p align="center">
  <a href="docs/media/yanemengvideo15mbcrop1.mp4"><strong>▶ Watch Project Demo Video</strong></a>
</p>

<p align="center">
  English · <a href="./README.md">中文</a>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white">
  <img alt="Django" src="https://img.shields.io/badge/Django-4.2-092E20?logo=django&logoColor=white">
  <img alt="Vue" src="https://img.shields.io/badge/Vue-3-42B883?logo=vue.js&logoColor=white">
  <img alt="Vite" src="https://img.shields.io/badge/Vite-5-646CFF?logo=vite&logoColor=white">
  <img alt="SQLite" src="https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white">
</p>

<p align="center">
  <a href="#-core-strengths">Core Strengths</a> ·
  <a href="#-feature-showcase">Feature Showcase</a> ·
  <a href="#-quick-start">Quick Start</a> ·
  <a href="#-demo-accounts">Demo Accounts</a> ·
  <a href="#-open-source-release-notes">Release Notes</a>
</p>

## Overview

**Yanmeng** is an integrated platform for postgraduate exam preparation scenarios, focusing on a full workflow of content access, discussion, trend analysis, and governance.

- Frontend capabilities: articles, forum, search, trend word cloud, user center
- Governance capabilities: fine-grained moderation via admin panel (`/admin`)
- Collaboration capabilities: built-in API docs (`/docs`) for faster frontend/backend integration

## Core Strengths

### 1. End-to-end product workflow

- A complete user path from browsing and searching to posting and interaction
- Centralized moderation and governance for users, posts, and articles
- Well-suited for coursework, capstone projects, and campus-level operations

<p align="center">
  <img src="docs/images/ppt/image11.png" alt="End-to-end Workflow" width="88%" />
</p>

### 2. Strong admin capabilities (`/admin`)

- Django Admin + SimpleUI for fast onboarding and low maintenance
- Efficient filtering and management of users/articles/posts
- Fine-grained moderation for real-world community governance

<p align="center">
  <img src="docs/images/showcase/admin-users.png" alt="Admin Users" width="72%" />
</p>

### 3. Built-in API docs (`/docs`)

- Docs entry: `http://127.0.0.1:8000/docs/`
- Clear routes, parameters, and response structures
- Lower onboarding cost and higher integration efficiency

<p align="center">
  <img src="docs/images/showcase/api-docs.png" alt="API Docs" width="88%" />
</p>

## Feature Showcase

### Article List

- Category-based browsing and recommendation aggregation for clear information organization.

<p align="center">
  <img src="docs/images/showcase/article-list.png" alt="Article List" width="88%" />
</p>

### Article Detail

- Optimized for deep reading and long-form content retention.

<p align="center">
  <img src="docs/images/showcase/article-detail.png" alt="Article Detail" width="88%" />
</p>

### Article Creation

- Built-in content publishing flow for sustainable content growth.

<p align="center">
  <img src="docs/images/showcase/article-create.png" alt="Article Creation" width="88%" />
</p>

### Forum List

- Topic-oriented discussion feed emphasizing community interaction.

<p align="center">
  <img src="docs/images/showcase/forum-list.png" alt="Forum List" width="88%" />
</p>

### Forum Detail

- Post-level interaction view for experience sharing and Q&A.

<p align="center">
  <img src="docs/images/showcase/forum-detail.png" alt="Forum Detail" width="88%" />
</p>

### Search

- Unified search across articles and forum posts for fast information retrieval.

<p align="center">
  <img src="docs/images/showcase/search.png" alt="Search" width="88%" />
</p>

### Trend Word Cloud

- Visualized trend analysis to improve content insight efficiency.

<p align="center">
  <img src="docs/images/showcase/trend-wordcloud.png" alt="Trend Word Cloud" width="88%" />
</p>

### Login / Signup / User Center

<p align="center">
  <img src="docs/images/showcase/login.png" alt="Login" width="31%" />
  <img src="docs/images/showcase/signup.png" alt="Signup" width="31%" />
  <img src="docs/images/showcase/user-center.png" alt="User Center" width="31%" />
</p>

## Quick Start

### 1) Clone repository

```bash
git clone <YOUR_REPO_URL>
cd yanmengProject
```

### 2) Backend (conda recommended)

```bash
conda create -n yanmeng python=3.8 -y
conda activate yanmeng

cd ymbackend
pip install -r requirements.txt

# Recommended for open-source deployment
export DJANGO_SECRET_KEY='replace-with-your-own-secret-key'

python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

### 3) Frontend

```bash
cd ../ymfrontend
npm install
npm run dev
```

### 4) Entry points

- Frontend: `http://localhost:5173`
- Admin panel: `http://127.0.0.1:8000/admin/`
- API docs: `http://127.0.0.1:8000/docs/`

## Demo Accounts

### Admin

- Username: `admin`
- Password: `YanmengAdmin@2026!`

> Please change this password immediately after first login.

### Frontend demo user

- Phone: `18800000001`
- Password: `demo123456`

Optional accounts: `18800000002` ~ `18800000007` (same password).

## Project Structure

```text
yanmengProject/
├─ ymbackend/              # Django backend
│  ├─ ymbackend/           # settings, urls
│  ├─ userInfo/            # user app
│  ├─ ymblog/              # article app
│  ├─ ymforum/             # forum app
│  └─ media/               # local static/media assets
├─ ymfrontend/             # Vue3 + Vite frontend
└─ docs/
   ├─ images/showcase/     # README showcase images
   └─ media/               # README video assets
```

## Open-Source Release Notes

- Disable `DEBUG` and tighten `ALLOWED_HOSTS` in production
- Keep all secrets in environment variables
- Recommended additions: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`
