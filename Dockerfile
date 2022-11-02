FROM python:3.9

# Update to the latest PIP
RUN pip3 install --upgrade pip
#ADD . /math_api
# Set the curent working directory
ADD . /math_api
WORKDIR /math_api

# install our dependencies
RUN  pip3 install -r requirements.txt
RUN dir -s

ENV PYTHONPATH=/math_api
CMD ["python3", "app/main.py"]
