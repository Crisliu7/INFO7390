#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Given a company with CIK (company ID) XXX (omitting leading zeroes) and
document accession number YYY (acc-no on search results), programmatically
generate the url to get data (http://www.sec.gov/Archives/edgar/data/51143
/000005114313000007/0000051143-13-000007-index.html for IBM for example).
Parse the file to locate the link to the 10q file (quarterly financial
filing form) (https://www.sec.gov/Archives/edgar/data/51143/000005114313
000007/ibm13q3_10q.htm for the above example). Parse this file to
extract “all” tables in this filing and save them as csv files.
'''

import sys
import requests
import lxml
import numpy as np
import re
import pandas as pd
import csv
import time
import boto3
from botocore.client import Config
from bs4 import BeautifulSoup

__author__ = 'Jiali Cheng(001822320), Sicheng Zhang and Mengqi Zhao'

class TableParser:

    ''' This is a table parser that extract all the tables and save them as
        CSV files, the URL generated by a given CID and Acc-no from EDGAR.'''

    def __init__(self, rawacc):

        self.__rawAcc = rawacc
        print("Access number selected: "+self.__rawAcc)

    def getCid(self, rawacc):
        ''' Ommiting the leading zeros in CID'''

        Cid = ''
        for i in rawacc:
            if i != '0':
                if i == '-':
                    break
                Cid = Cid + i

        print("CID got: "+Cid)
            
        return Cid

    def getAcc(self, rawacc):
        ''' Get rid of the '-' in the raw Accno'''

        Acc = ''
        for char in rawacc:
            if char != '-':
                Acc = Acc + char

        print("Acc-no got: "+Acc)
        return Acc

    def formUrl(self, rawacc):
        ''' Form the unique URL for a given Accno'''

        url = (
            "https://www.sec.gov/Archives/edgar/data/%s/%s/%s-index.html" % \
            (self.getCid(self.__rawAcc),
             self.getAcc(self.__rawAcc),
             self.__rawAcc))

        print("Company database got: ", url)
        
        return url

    def get10q(self, rawurl):
        ''' Locate to the 10q file'''

        # Get the tag of 10q file from the previous page
        response = requests.get(rawurl)
        soup = BeautifulSoup(response.text,'lxml')
        file = soup.find_all('a',string=re.compile("10q"))[0]
        url_temp = file.attrs.get('href')

        # Get the URL of 10q file
        url_10q = "https://www.sec.gov" + url_temp
        print("10q file got: " + url_10q)
        
        return url_10q

    def extract(self, url):
        ''' Get all the table items from a URL'''

        print("Extracting tables from URL: ", url)
        
        # Parse the HTML as a string
        response = requests.get(url)
        #soup = BeautifulSoup(response.text,'lxml')

        df = pd.read_html(url)
        for t in df[4:]:
            t.to_csv("0000051143-13-000007.csv",mode='a')

        # for t in df:
        #     new = pd.DataFrame()
        #     i = 0
        #     for row in t.loc[:]:
        #         j = 0
        #         for co in t.iloc[:]:
        #             if t.ix[i,j]:
        #                 new.ix[i,j] = t.ix[i,j]
        #                 j+=1
        #             else:
        #                 j+=1
        #                 continue                        
        #         i+=1
            # new.to_csv("0000051143-13-000007.csv",mode='a')

    def log(self, operation):
        '''Log all the operations with a time stamp into a log file'''

        self.__log = "%s-log.txt" % self.__rawAcc
        with open(self.__log, 'a') as f:
            data = time.ctime() + ": " + operation
            f.write(data)

    def upload_path(self, ACCESS_NAME, ACCESS_KEY):###################################################################################
        '''Path of the AWS S3 bucket to upload the file'''

        print("***************Uploading to AWS S3 bucket***************")

        self.__ACCESS_NAME = ACCESS_NAME
        self.__ACCESS_KEY = ACCESS_KEY
        self.__BUCKET_NAME = "info7390-case1"
        print("Accessing bucket name %s: " %  self.__BUCKET_NAME)

    def upload(self, filename):###################################################################################
        '''Upload the file to the bucket'''

        data = open(filename, 'rb')

        s3 = boto3.resource(
            's3',
            aws_access_key_id=self.__ACCESS_NAME,
            aws_secret_access_key=self.__ACCESS_KEY,
            config=Config(signature_version='s3v4'))

        s3.Bucket(self.__BUCKET_NAME).put_object(Key=filename, Body=data)
        
        # Log and print
        operation = "Done uploading.\n"
        self.log(operation)
        print(operation)
        
        
    def startparsing(self):
        ''' Start parsing tables from EDGAR'''

        url = self.formUrl(self.__rawAcc)
        url_10q = self.get10q(url)
        self.extract(url_10q)
        self.upload_path(sys.argv[2],sys.argv[3])
        self.upload("0000051143-13-000007.csv")
        print("***********Done!***********")



if __name__ == '__main__':

    if len(sys.argv) > 0:
        rawacc = sys.argv[1]
        tp = TableParser(rawacc)
        tp.startparsing()
