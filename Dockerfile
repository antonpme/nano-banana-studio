# Nano-Banana Studio - Docker Configuration
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY templates/ templates/
COPY field_library.json .
COPY presets_db.json .

# Create volume mount points for persistent data
VOLUME ["/app/data"]

# Expose port
EXPOSE 5000

# Environment variables (override with docker run -e)
ENV FLASK_ENV=production
ENV PORT=5000
ENV PRESETS_DB_PATH=/app/data/presets_db.json
ENV FIELD_LIBRARY_PATH=/app/field_library.json

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/api/health', timeout=5)"

# Run the application
CMD ["python", "app.py"]
