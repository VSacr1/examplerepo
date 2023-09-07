FROM python:3.8
COPY . .
RUN python3 -m pip install --upgrade -r requirement.txt
EXPOSE 5000 
RUN python3 create.py 
ENTRYPOINT ["python3","app.py"]