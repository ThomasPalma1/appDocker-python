FROM python:3.10
EXPOSE 8080
WORKDIR /app
COPY /app .
RUN pwd
RUN ls
RUN pip3 install -r ./requirements.txt
CMD ["python3", "main.py"]
