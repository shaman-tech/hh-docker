FROM tiangolo/uwsgi-nginx:python3.5
RUN pip install flask
COPY nginx.conf /etc/nginx/conf.d/
COPY . /app
RUN /usr/local/bin/pip install -r /app/requirements.txt
