# FROM python:3.10

# WORKDIR /app
# COPY . .

# RUN pip install --no-cache-dir -r requirements.txt

# CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.enableCORS=false"]

# Use a Python base image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy your code files into the container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir streamlit requests

# Expose the Streamlit default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.enableCORS=false"]
