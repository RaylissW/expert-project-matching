# Базовый образ с Python
FROM python:3.13-slim

# Установка рабочей директории
WORKDIR /app

# Копирование файла зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всех файлов проекта
COPY . .

# Установка переменной окружения для вывода логов
ENV PYTHONUNBUFFERED=1

# Команда для запуска приложения
CMD ["python", "main.py"]

#Подбор пар эксперт-проект