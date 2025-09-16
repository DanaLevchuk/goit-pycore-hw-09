# Використовуємо офіційний образ Python
FROM python:3.13-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли проєкту в контейнер
COPY . /app

# Встановлюємо Poetry
RUN pip install poetry

# Встановлюємо залежності через Poetry
RUN poetry install --no-root

# Команда запуску (твій помічник)
CMD ["python", "assistant_bot/main.py"]
