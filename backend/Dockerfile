FROM python:3.10-slim

WORKDIR /app

# Copy chỉ requirements để tận dụng caching Docker
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code
COPY . .

# Định nghĩa biến môi trường để sử dụng `.env`
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
