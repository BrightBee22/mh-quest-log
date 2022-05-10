#define base image
FROM python:3.6
#copy contents
COPY . .
#set up env variables
ENV DATABASE_URI=sqlite:///data.db
ENV SECRET_KEY=SECRET_KEY
#expose ports
EXPOSE 5000
#install requirements
RUN pip3 install -r requirements.txt
#run app
ENTRYPOINT ["python3", "app.py"]