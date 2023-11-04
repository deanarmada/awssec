FROM python:3.10.1
WORKDIR /usr/src/app
EXPOSE 8000

# Install vim, enable compilemessages and m2crypto
RUN apt-get update &&  \
    apt-get install vim -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
