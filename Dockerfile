# coping a base image from docker hub
FROM python:3.6-alpine
# changing working directory
WORKDIR /project
# copy local files to project/working directory
ADD . /project

# install all the requirments
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Run file 
CMD ["python","main.py"]