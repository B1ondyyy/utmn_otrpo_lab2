# 1. Используем базовый образ Python
FROM python:3.9-slim

# 2. Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    libopencv-dev python3-opencv && \
    rm -rf /var/lib/apt/lists/*

# 3. Указываем рабочую директорию в контейнере
WORKDIR /app

# 4. Копируем скрипт и изображение в контейнер
COPY main.py /app/
COPY faces.jpg /app/

# 5. Устанавливаем Python-библиотеку OpenCV
RUN pip install opencv-python-headless

# 6. Указываем команду по умолчанию
CMD ["python", "main.py", "faces.jpg"]
