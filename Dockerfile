# FROM python:3.9-slim
# WORKDIR /app
# COPY app.py requirements.txt utils/ /app/
# COPY templates/ /app/templates/
# COPY static/ /app/static/
# COPY db/ /app/db/
# RUN pip install --no-cache-dir -r requirements.txt
# CMD flask run --host=0.0.0.0 --port=80 --debug --reload

FROM python:3.9-slim
WORKDIR /app

# Only copy existing files
COPY app.py requirements.txt /app/
COPY templates/ /app/templates/
COPY static/ /app/static/
COPY db_init/ /app/db_init/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=80", "--debug", "--reload"]
