FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD hello_world.py /
CMD [ "python", "./hello_world.py" ]