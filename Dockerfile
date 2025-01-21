# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any required dependencies (in this case none are needed)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the server will run on
EXPOSE 8080

# Run the server when the container launches
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=8080"]
