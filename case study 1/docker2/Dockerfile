FROM python:3

RUN pip3 install requests 
RUN pip3 install pandas 
RUN pip3 install numpy 
RUN pip3 install scipy 
RUN pip3 install boto3 
RUN pip3 install matplotlib

COPY ./MissingData.py /src/MissingData.py

CMD ["python3", "MissingData.py"]

