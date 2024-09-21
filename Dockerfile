FROM public.ecr.aws/docker/library/python:3.11-slim as Builder

WORKDIR /app

RUN python -m pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

FROM public.ecr.aws/docker/library/python:3.11-slim

# Copy the Lambda adapter from the official image
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.4 /lambda-adapter /opt/extensions/lambda-adapter

ENV PORT=8000
WORKDIR /var/task

# Install the runtime dependencies
COPY --from=Builder /app/requirements.txt ./
RUN python -m pip install -r requirements.txt

# FIXME: copy only the necessary files
COPY . .

CMD exec uvicorn --host=0.0.0.0 --port=$PORT src.main:app
