FROM python:3.9-slim

WORKDIR /app

COPY src /app/src

COPY requirements.txt /app
COPY main.py /app

RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run main.py when the container launches
CMD ["python", "main.py"]
