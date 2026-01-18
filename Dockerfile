FROM python:3.10.19-slim 
#light image to save space

WORKDIR /server

#copy server script
COPY server /server

#install dependencies
RUN pip install flask gunicorn

#expose the API port
EXPOSE 8000 

#use gunicorn to deploy a production server 
ENTRYPOINT ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "server:app"]
