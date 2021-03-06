# We simply inherit the Python 3 image. This image does
# not particularly care what OS runs underneath
FROM python:3.7

# RUN apt-get update && apt-get install -qq -y \
#     build-essential libpq-dev --no-install-recommends


# Set an environment variable with the directory
# where we'll be running the app
ENV APP /app
ENV PYTHONUNBUFFERED 1 # python 執行訊息重新顯示到標準輸出



# celery
# ENV C_FORCE_ROOT true
# ENV CELERY_BROKER_URL redis://:devpassword@redis:6379/0
# ENV CELERY_RESULT_BACKEND redis://:devpassword@redis:6379/0


# Create the directory and instruct Docker to operate
# from there from now on
RUN mkdir $APP
WORKDIR $APP

# Expose the port uWSGI will listen on
EXPOSE 5000

# Copy the requirements file in order to install
# Python dependencies
COPY ./env/flask/requirements.txt .

# Install Python dependencies
RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip3 install -r requirements.txt

# We copy the rest of the codebase into the image
COPY ./webapp/ ./

# Create python-click customer command
RUN pip install --editable .


# Finally, we run uWSGI with the ini file we
# created earlier
CMD [ "uwsgi", "--ini", "app.ini" ]
