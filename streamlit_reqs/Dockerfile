# Can specify version and not slim if needed
# FROM python:3.10

# Use the latest Python slim image as a parent image
FROM python:slim

# Update package index and install nano
# RUN apt-get update && apt-get install nano

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt

# RUN pip install -r requirements.txt

# Expose port 8501 to the outside world
EXPOSE 8501

RUN ls

# Define the command to run your Streamlit app when the container starts
CMD ["streamlit", "run", "homepage.py"]