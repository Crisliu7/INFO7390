FROM patavee/scipy-py3

RUN pip3 install requests 
RUN pip3 install pandas 
RUN pip3 install numpy 
RUN pip3 install scipy 
RUN pip3 install boto3 
RUN pip3 install matplotlib
RUN pip3 install tk-tools

COPY ./MissingData.py /src/MissingData.py

CMD ["python3", "MissingData.py"]

