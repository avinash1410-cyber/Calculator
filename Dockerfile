# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app/

# Step 4: Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Step 5: Expose the port the app runs on (default is 8000 for Django)
EXPOSE 8000

# Step 6: Set environment variables to ensure the app runs correctly
ENV PYTHONUNBUFFERED 1

# Step 7: Run migrations (optional, to set up the database) and start the Django development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
