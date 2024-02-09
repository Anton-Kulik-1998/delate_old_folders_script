# Используйте официальный образ Python
FROM python:3.9.6

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем скрипт удаления старых файлов в контейнер
COPY . /app

# Создаем две директории
RUN mkdir -p /data/directory1 /data/directory2

# Устанавливаем зависимости, если нужно
# RUN pip install some-dependency

# Установите необходимые зависимости
# RUN pip install -r requirements.txt

# Указываем точку входа для выполнения скрипта
CMD ["python", "/app/main.py"]
