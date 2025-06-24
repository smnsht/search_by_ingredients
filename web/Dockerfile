FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*

# Create data directory
RUN mkdir -p /app/data

# Download the parquet file
RUN curl -L https://argmax.nyc3.digitaloceanspaces.com/recipes/allrecipes.parquet -o /app/data/allrecipes.parquet

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# by Simon
RUN mkdir -p /app/web
COPY init.sh /app/
COPY src /app/web/
COPY src/*.pkl /app/data/

RUN pip install --no-cache-dir -r requirements.txt


# Expose the port the app runs on
EXPOSE 8080

# Command to run the application - make init.sh executable first
#CMD ["sh", "-c", "dos2unix ./init.sh && chmod +x ./init.sh && ./init.sh"]
CMD ["sh"]