# Aiogram-Dialog Bot Template

This repository contains the source code of a minimalistic telegram bot for managing the user's personal tasks. The goal of the project was to create an understandable and uncomplicated service inside Telegram (which for many users is the #1 application in terms of time spent daily), which would not be functionally inferior to well-known analogues from large corporations.

## Used technology
* Python [3.12](https://www.python.org/downloads/release/python-3120/)
* aiogram [3.10](https://pypi.org/project/aiogram/3.10/) (Telegram Bot framework)
* aiogram-dialog [2.1](https://aiogram-dialog.readthedocs.io/en/stable/) (GUI framework for Telegram Bot);
* Docker and Docker Compose [latest](https://www.docker.com/products/docker-desktop/); (containerization);
* Redis [7.4](https://redis.io/download); (cashe and persistent storage for user states);
* NATS JetStream [latest](https://nats.io) (as a broker);
* PostgreSQL [15-alpine](https://www.postgresql.org/download/) (DB);
* SQLAlchemyORM [2.0.32](https://docs.sqlalchemy.org/en/20/orm/) (ORM lib for DB interactions);
* Alembic [1.13.2](https://pypi.org/project/alembic/1.13.2/) (DB migrations);

## Installation
### Requirements
- Installed Git, Docker, and Docker Compose.
1. **Create a directory**
Create a directory for the bot. For example: '/Users/Name/my_bot'. 
2. **Clone a repository**
Open the terminal inside the created directory and run the command:
```bash
git clone https://github.com/agrikol/task-management-telegram-bot.git
```
3. **Set your secrets**
Rename the '.env.example' file to '.env'. Then, following the instructions inside it, put your secrets there.
4. **Run your bot**
Open the terminal inside the bot directory and run the command:
```bash
docker compose up --build
```
5. **Check the logs**
If something goes wrong, log messages inside the terminal will answer your questions.
6. **Get started**
Open Telegram, find the bot, and initiate the `/start` command to begin managing your tasks.
