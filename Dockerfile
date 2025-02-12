# Используем базовый образ с Python
FROM python:3.12

# Устанавливаем зависимости
RUN pip install --no-cache-dir selenium pytest  # Минимальный набор
# Скопируйте requirements.txt и установите пакеты
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем Git
RUN apt-get update && apt-get install -y git

# Создаем рабочую директорию
WORKDIR /app

# Клонируем репозиторий Git
ARG GIT_REPO
ARG GIT_BRANCH
RUN git clone --depth 1 -b ${GIT_BRANCH} ${GIT_REPO} .

# Команда для запуска тестов
CMD ["python", "-m", "pytest"]  # Запускаем pytest с помощью python -m
