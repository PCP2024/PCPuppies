#base python image
FROM python:3.9

#set working directory
WORKDIR /app

# Install system dependencies a-la chatGPT
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libegl1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
#copy and install requirements
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#copy the rest of the files
COPY . .