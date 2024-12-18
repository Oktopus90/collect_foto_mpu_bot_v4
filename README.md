# collect_foto_mpu_bot_v4


docker compose -f docker-compose.local.yml up --build

python -m ruff check ./app
ruff check --fix

.env
```
BOT_TOKEN = 'BOT_TOKEN'
DATABASE_URL = 'sqlite:///app/datebase/mpu_foto.db'
```
alembic revision --autogenerate -m 'initial'
alembic upgrade head