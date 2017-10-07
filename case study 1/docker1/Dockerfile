#FROM paulflorea/python3-uwsgi-scipy-numpy:alpine
FROM python:3
RUN pip3 install bs4 
RUN pip3 install numpy 
RUN pip3 install pandas 
RUN pip3 install lxml 
RUN pip3 install requests
RUN pip3 install html5lib

COPY ./TableParser.py /src/TableParser.py

CMD ["python3", "TableParser.py"]

