# Stage 1: Build the dependencies
FROM nvidia/cuda:12.8.1-cudnn-devel-ubuntu22.04 AS builder

RUN apt update

RUN apt install software-properties-common -y

RUN apt-get install -y python3.9

RUN apt install python3-pip -y

WORKDIR /app/api

# Install Poetry
RUN pip3 install --no-cache-dir poetry

# Copy only the dependency files
COPY pyproject.toml poetry.lock ./

# Copy files
COPY . .


# Install dependencies
RUN poetry install

# Install Watchdog for auto discovery
RUN poetry add watchdog

# Stage 2: Build the final image

RUN pip3 install --upgrade --force-reinstall --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128

FROM builder AS final

# Set the working directory
WORKDIR /app/api/modular-fastapi

# Run the server
ENTRYPOINT ["bash", "./start.sh"]
