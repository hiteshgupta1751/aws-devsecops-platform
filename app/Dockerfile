FROM python:3.10-slim

WORKDIR /app

# Install deps
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the python package folder
COPY app ./app

EXPOSE 5000

CMD ["python", "-m", "app"]

