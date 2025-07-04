FROM python:3.10-bullseye

WORKDIR /app

# копіюємо файл із залежностями
COPY requirements/backend.in ./requirements.txt

# встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# копіюємо увесь код
COPY . .

CMD ["uvicorn", "spaceship.main:app", "--host", "0.0.0.0", "--port", "8000"]
