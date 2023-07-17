# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the UI.py file into the container
# COPY UI.py /app
COPY . .
COPY ../ ../

# Install the dependencies
RUN pip install opencv-python-headless ffpyplayer

# Run the UI.py script when the container launches
CMD ["python", "UI.py"]