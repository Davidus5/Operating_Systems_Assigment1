#get python:3.9-slim image as instructed
FROM python:3.9-slim


#define the work folder inside the container
WORKDIR /app

#copy requirements file to the container, for installing libraries
COPY requirements.txt .

#install the libraries as listed in requirements file
RUN pip install --no-cache-dir -r requirements.txt

#copy the python app file inside the container
COPY app.py .

#expose port 5000 for the flask server
EXPOSE 5000

#command that will run when the container is up
CMD ["python", "app.py"]