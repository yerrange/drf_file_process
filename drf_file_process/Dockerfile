FROM python:3.10.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]