FROM python:3.12.2-slim-bullseye

WORKDIR /usr/src/notes-app-backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    netcat \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade-strategy only-if-needed -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/notes-app-backend/entrypoint.sh
RUN chmod +x /usr/src/notes-app-backend/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/notes-app-backend/entrypoint.sh"]