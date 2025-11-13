
FastAPI Project — Modern REST API for Posts, Users & Voting

A modern, production-ready RESTful API built with FastAPI, designed to deliver high performance, clean architecture, and secure user interactions.
This project implements JWT authentication, robust CRUD operations, and an intuitive voting system, backed by PostgreSQL, SQLAlchemy ORM, and Alembic migrations.

Built with scalability, readability, and real-world API design standards in mind, this project serves as a solid blueprint for building maintainable backend applications.

## Features

- CRUD operations for posts
- User authentication using JWT
- Upvote/Downvote voting system
- PostgreSQL database integration
- Alembic migrations for version-controlled schema
- Fully asynchronous API endpoints
- Secure password hashing (bcrypt)
- Modular and scalable project structure
- Pytest-based testing support
- Docker support for easy deployment

## Tech Stack

- Backend: FastAPI, Python 3.11+
- Database: PostgreSQL
- ORM: SQLAlchemy Orm
- Migrations: Alembic
- Authentication: JWT, OAuth2
- Testing: Pytest
- Version Control: Git, GitHub

- Deployment: Docker, GitHub Actions (CI/CD)

- # Project Structure
FastAPI/
│── .github/
│ └── workflows/
│ └── build-deploy.yml
│
│── alembic/
│ ├── versions/
│ ├── env.py
│ ├── README
│ └── script.py.mako
│
│── app/
│ ├── routers/
│ │ ├── auth.py
│ │ ├── calculations.py
│ │ ├── posts.py
│ │ ├── users.py
│ │ └── vote.py
│ ├── init.py
│ ├── database.py
│ ├── config.py
│ ├── main.py
│ ├── models.py
│ ├── oauth2.py
│ ├── schema.py
│ └── utils.py
│
│── tests/
│ ├── conftest.py
│ ├── database.py
│ ├── test_calculations.py
│ ├── test_posts.py
│ ├── test_users.py
│ └── test_votes.py
│
│── .env
│── .gitignore
│── requirements.txt
│── alembic.ini
│── docker-compose-dev.yml
│── docker-compose-production.yml
│── dockerfile
│── README.md




