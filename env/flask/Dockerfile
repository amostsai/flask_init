# We simply inherit the Python 3 image. This image does
# not particularly care what OS runs underneath
FROM python:3.6

# Set an environment variable with the directory
# where we'll be running the app
ENV APP /app
ENV PYTHONUNBUFFERED 1 # python 執行訊息重新顯示到標準輸出



# test celery
ENV C_FORCE_ROOT true
ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0



# Create the directory and instruct Docker to operate
# from there from now on
RUN mkdir $APP
WORKDIR $APP

# Expose the port uWSGI will listen on
EXPOSE 5000 22 8888

# Copy the requirements file in order to install
# Python dependencies
COPY ./env/flask/requirements.txt .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# We copy the rest of the codebase into the image
COPY ./webapp/ ./

# Create python-click customer command
RUN pip install --editable .

# ssh test
# RUN apt update && apt install -y openssh-server && \
#     mkdir /var/run/sshd && \
#     echo 'root:root' | chpasswd && \
#     sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
#     sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
#     mkdir /root/.ssh && \
#     apt clean && \
#     rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Finally, we run uWSGI with the ini file we
# created earlier
CMD [ "uwsgi", "--ini", "app.ini" ]
#CMD ["/usr/sbin/sshd", "-D"]
#CMD ["sh", "-c", "uwsgi --ini app.ini; /usr/sbin/sshd -D"]
#CMD ["./flask_cmd"]
#ENTRYPOINT ["./flask_cmd.sh"]