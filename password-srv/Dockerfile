# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the password-srv.py file into the container
COPY password-srv.py /app
COPY . .
COPY ../ ../

# Install the dependencies
RUN pip install ffpyplayer

# Run the password-srv.py script when the container launches
CMD ["python", "password-srv.py"]