FROM python:3.11-slim

# Set working dir inside container
WORKDIR /app

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything (main.py, models.py, database.py etc.)
COPY . .

# Expose port (optional, aber leserlich)
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
