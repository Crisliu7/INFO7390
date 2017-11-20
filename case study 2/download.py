import pandas as pd
import numpy as np
import urllib
import requests
import time

loan = ["LoanStats3a","LoanStats3b","LoanStats3c","LoanStats3d",\
        "LoanStats_2016Q1","LoanStats_2016Q2","LoanStats_2016Q3",\
        "LoanStats_2016Q4","LoanStats_2017Q1","LoanStats_2017Q2"]
reject = ["RejectStatsA","RejectStatsB","RejectStatsD","RejectStats_2016Q1",\
          "RejectStats_2016Q2","RejectStats_2016Q3","RejectStats_2016Q4",\
          "RejectStats_2017Q1","RejectStats_2017Q2"]

def download(url_list):
    
    for u in url_list:
        url = ("https://resources.lendingclub.com/%s.csv.zip" % u)

        # Log and print
        operation = "Start retrieving files from " + u
        log(operation)
        print(operation)

        # Retrieving
        filename = "/Users/CJL-RMBP/Documents/assignment3data/%s.csv" % u 
        urllib.request.urlretrieve(url,filename=filename)

        # Log and print
        operation = "Done retrieving."
        log(operation)
        print(operation)
    
def log(operation):
    '''Log all the operations with a time stamp into a log file'''

    with open("log_file.txt", 'a') as f:
        data = time.ctime() + ": " + operation
        f.write(data)


# if "__name__" == "__main__":

# download(loan)
download(reject)

