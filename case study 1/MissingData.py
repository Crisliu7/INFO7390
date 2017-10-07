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
import time
import urllib
import requests
import shutil
import numpy as np
from numpy import *
import pandas as pd
from pandas import *
from scipy.stats import mode
import boto3
from botocore.client import Config
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



matplotlib.style.use('ggplot')


__author__ = 'Jiali Cheng(001822320)'

class AnalyseLog:
    ''' This is a table parser that extract all the tables and save them as
        CSV files, the URL generated by a given CID and Acc-no from EDGAR.'''

    def __init__(self, year):

        self.__year = year
        self.__df = DataFrame()

    def getLog(self, month):
        ''' Form the unique URL for a given Accno'''

        qtr = (month+2)//3
        if month<10:
            month = "0"+str(month)
        month = str(month)
        url = ("https://www.sec.gov/dera/data/Public-EDGAR-log-file-data/%s/Qtr%s/log%s01.zip" % (self.__year, qtr, self.__year+month))
        #path = "./log%s01.zip/"%self.__year+month
        #try:

        # Log and print
        operation = "Start retrieving files from "+url
        self.log(operation)
        print(operation)

        # Retrieving
        filename = ("log%s"% self.__year)+month+"01.zip" 
        urllib.request.urlretrieve(url,filename=filename)

        # Log and print
        operation = "Done retrieving."
        self.log(operation)
        print(operation)

        # Unzip the file
        shutil.unpack_archive(filename)

        # Log and print
        operation = "Done unpacking."
        self.log(operation)
        print(operation)

        logfile = ("log%s"% self.__year)+month+"01.csv"

        return logfile

        #except:  

         #   operation = "Failed"
         #   self.log(operation)
         #   print(operation)
          #  exit(0)

    def analyse(self, filename, m):
        '''Read data, analyse data and deal with missing data'''

        with open(filename, 'r') as f:

            df = pd.read_csv(f)
            
            self.analyseIp(filename,df["ip"])
            self.analyseTime(filename,df["time"],m)
            self.analyseCik(filename,df["cik"],m)
            self.analyseCode(filename,df["code"],m)
            self.analyseSize(filename,df["size"],m)
            self.analyseIdx(filename,df["idx"])
            self.analyseRef(filename,df["norefer"])
            self.analyseAgt(filename,df["noagent"],m)
            self.analyseCrw(filename,df["crawler"],m)
            self.analyseBrw(filename,df["browser"],m)

        return

    def analyseIp(self, filename, df):###################################################################################
        '''First three octets of the IP address with the fourth octet obfuscated'''

        print("***************Analysing IP***************")
        class_a = 0
        class_b = 0
        class_c = 0

        # Metrics
        # Calculate the numbers of class A, B, C, D, E and missing IP
        number = df.shape[0]
        missing = df.ix[pd.isnull(df),].shape[0]

        for i in df:

            i1 = i.split('.')[0]
            i1 = int(i1)

            if i1 < 128:
                class_a+=1
            elif i1 > 128 & i1 < 192:
                class_b+=1
            elif i1 > 192 & i1 < 224:
                class_c+=1
            else:
                missing+=1

        # Find anomalies
        # Hear we can do nothing towards IP

        # Handle missing data
        # Here we can do nothing towards IP

        # Write summary
        summary = Series([class_a,class_b,class_c,missing,number], index=["class_a","class_b","class_c","missing","total"])
        self.summarize(summary)

        # Log and print
        operation = (
            "Done analysing IP of %s. %s IP addresses totally. %s " 
            "class A IPs, %s class B IPs, %s class C IPs and %s " 
            "missing IPs.\n" %
            (filename,number,class_a,class_b,class_c,missing))
        self.log(operation)
        print(operation)

    def analyseTime(self, filename, df, m):
        '''Apache log file time'''

        print("***************Analysing Time***************")

        # Find anomalies
        # Sort by time oreder, corecct illegitimate time
        df = df.sort_values(ascending=True)

        # Handle missing data
        # Fill missing time with the former time
        missing = df.ix[pd.isnull(df),].shape[0]
        # if missing != 0:
            #df1.fillna(value=5)

        # Metrics 
        count = df.value_counts()
        count = count.sort_index(ascending=True)
        
        # Log and print
        operation = (
            "Done analysing IP of %s. %s missing values replaced by their adjacent value.\n" %
            (filename,missing))
        self.log(operation)
        print(operation) 

        # Plot
        plt.figure("Access volume - time on %s/1, %s" % (m,self.__year))
        count.plot()

        return
        
    def analyseCik(self, filename, df, m):
        '''SEC Central Index Key (CIK) associated with the document requested'''

        print("***************Analysing CIK***************")

        # Metrics
        number = df.shape[0]
        count = df.value_counts()

        # Find anomalies
        # Hear we can do nothin towards CIK

        # Handle missing data
        # Fill missing CIK with a random one
        missing = df.ix[pd.isnull(df),].shape[0]
        # if missing != 0:
            #df1.fillna(value=5)

        # Plot
        plt.figure("CIK - access volume on %s/1, %s" % (m,self.__year))
        count.plot.hist(logx=True)

    def analyseCode(self, filename, df, m):
        '''Apache log file status code for the request'''

        print("***************Analysing Code***************")

        # Metrics
        number = df.shape[0]
        count = df.value_counts()

        # Find anomalies
        # Hear we can do nothin towards IP

        # Handle missing data
        # Replace all the missing data with 200 OK, which is the most possible case
        missing = df.ix[pd.isnull(df),].shape[0]
        if missing != 0:
            df1.fillna(na,count.index[0])

        # Plot
        plt.figure("Code volume on %s/1, %s" % (m,self.__year))
        count.plot.hist()
        count.plot()

    def analyseSize(self, filename, df, m):
        '''Document file size'''

        number = df.shape[0]

        # Find anomalies
        # Hear we can do nothin towards IP

        # Handle missing data
        # Replace with mean
        missing = df.ix[pd.isnull(df),].shape[0]
        if missing != 0:
            df1.fillna(na, df.mean())

        # Metrics

        # Plot
        plt.figure("File size box on %s/1, %s" % (m,self.__year))
        color = dict(boxes='DarkGreen', whiskers='DarkOrange',
                 medians='DarkBlue', caps='Gray')
        df.plot.box(color=color, sym='r+')

        pass    

    def analyseIdx(self, filename, df):###################################################################################

        # Find anomalies
        # Hear we can do nothin towards IP

        # Handle missing data
        # Here we can do nothing toward IP

        # Metrics

        pass

    def analyseRef(self, filename, df):###################################################################################

        # Find anomalies
        # Hear we can do nothin towards IP

        # Handle missing data
        # Here we can do nothing toward IP

        # Metrics

        pass

    def analyseAgt(self, filename, df, m):###################################################################################

        print("***************Analysing Agent***************")

        # Metrics
        # Calculate the numbers of whether or not using agent and missing
        number = df.shape[0]
        count = df.value_counts()
        if count.index.size>1:
            use_agt = count[1]
            not_agt = count[0]
        else:
            use_agt = count[0]
            not_agt = 0

        # Find anomalies
        # Hear we can do nothin towards IP

        # Handle missing data
        # Replace with mode
        missing = df.ix[pd.isnull(df),].shape[0]
        if missing != 0:
            df.fillna(na,caa95f3c0d41)

        # Write summary
        summary = Series([use_agt,not_agt,missing,number], index=["using agent","not using agent","missing","total"])
        self.summarize(summary)
        print(summary)
        
        # Log and print
        operation = (
            "Done analysing agent of %s. %s items totally. "
            "%s uses agent, %s not and %s missing.\n" %
            (filename,number,use_agt,not_agt,missing))
        self.log(operation)
        print(operation)

        # Plot
        plt.figure("Agnet using distribution on %s/1, %s" % (m,self.__year))
        count.plot.pie(labels=["not using agent","using agent"], autopct='%.2f', fontsize=10, figsize=(6, 6))

    def analyseCrw(self, filename, df, m):

        print("***************Analysing Crawler***************")

        # Metrics
        # Calculate the numbers of whether or not using agent and missing
        number = df.shape[0]
        count = df.value_counts()
        if count.index.size>1:
            use_crw = count[1]
            not_crw = count[0]
        else:
            use_crw = count[0]
            not_crw = 0
        # Find anomalies
        # Hear we can do nothin towards crawler

        # Handle missing data
        # Here we fill missing data with not using crawler
        missing = df.ix[pd.isnull(df),].shape[0]
        if missing != 0:
            df.fillna(value=0)
            count = df.value_counts()
            not_crw = count[0]
            use_crw = count[1]

        # Write summary
        summary = Series([use_crw,not_crw,missing,number], index=["using crawler","not using crawler","missing","total"])
        self.summarize(summary)
        print(summary)
        
        # Log and print
        operation = (
            "Done analysing agent of %s. %s items totally. "
            "%s uses crawler, %s not and %s missing.\n" %
            (filename,count,use_crw,not_crw,missing))
        self.log(operation)
        print(operation)
        
        # Plot
        plt.figure("Crawler using distribution on %s/1, %s" % (m,self.__year))
        count.plot.pie(labels=["using crawler","not using crawler"], autopct='%.2f', fontsize=10, figsize=(6, 6))

    def analyseBrw(self, filename, df, m):

        print("***************Analysing Brwoser***************")

        # Metrics
        # Calculate the numbers of which kind of browser and missing
        number = df.shape[0]
        count = df.value_counts()
        count_number = count.shape[0]

        # Find anomalies
        # Hear we can do nothin towards IP

        # Handle missing data
        # Here we fill missing parts with respect to the proportion of each kind accordingly
        missing = df.ix[pd.isnull(df),].shape[0]
         if missing != 0:
            df.replace(na,count.index[0]) 

        # Write summary
        summary = count
        self.summarize(summary)
        
        # Log and print
        operation = (
            "Done analysing agent of %s. %s items totally.\n" % (filename,number))
        self.log(operation)
        print(operation)
        
        # Plot
        plt.figure("Browser using distribution on %s/1, %s" % (m,self.__year))
        count.plot.pie(labels=count.index, autopct='%.2f', fontsize=10, figsize=(6, 6))

    def log(self, operation):
        '''Log all the operations with a time stamp into a log file'''

        self.__final_log = "%s-final-log.txt" % self.__year
        with open(self.__final_log, 'a') as f:
            data = time.ctime() + ": " + operation
            f.write(data)

    def summarize(self, summary):

        if self.__df.empty:
            self.__df = summary
        else:
            self.__df = pd.concat([self.__df,summary],axis=1)        

    def concatData(self, log_list):###################################################################################
        '''Data should be concatinated calling pd.concat() since they have the same variables'''

        pieces = []
        for f in log_list:
            df = pd.read_csv(f)
            pieces.append(df)

        merged_data = pd.concat(pieces, keys=log_list)
        final_data = "%s-final-data.csv"%self.__year
        merged_data.to_csv(final_data)

        return final_data

    def concatSummary(self, log_list):
        '''Summary of 12 months should be concatinated calling pd.concat() since they have the same variables'''

        merged_data = pd.concat(log_list)#, keys=log_list)
        final_summary = "%s-final-summary.csv"%self.__year
        merged_data.to_csv(final_summary)

        return final_summary

    def upload_path(self, ACCESS_NAME, ACCESS_KEY):###################################################################################
        '''Path of the AWS S3 bucket to upload the file'''

        self.__ACCESS_NAME = ACCESS_NAME
        self.__ACCESS_KEY = ACCESS_KEY
        self.__BUCKET_NAME = "info7390-case1"
        print("Access %s bucket name %s: " % (self.__ACCESS_NAME, self.__BUCKET_NAME))

    def upload(self, filename):###################################################################################
        '''Upload the file to the bucket'''

        print("***************Uploading to AWS S3 bucket***************")

        data = open(filename, 'rb')

        s3 = boto3.resource(
            's3',
            aws_access_key_id=self.__ACCESS_NAME,
            aws_secret_access_key=self.__ACCESS_KEY,
            config=Config(signature_version='s3v4'))

        s3.Bucket(self.__BUCKET_NAME).put_object(Key=filename, Body=data)
        
        # Log and print
        operation = "Done uploading to" + username + ":" + bucketname + ".\n"
        self.log(operation)
        print(operation)
                
    def startanalysing(self):###################################################################################
        ''' Start getting and analysing data from EDGAR log file and upload to the bucket'''

        if True:
            log_list=[]
            sum_list=[]
            for m in range(1,13):

                # Get log of the first day of each month in a year
                filename = self.getLog(m)
                # Add each log into a list
                log_list.append(filename)
                self.__df = DataFrame()
                
                # Analyse this file
                self.analyse(filename,m)
                # df = self.summarize
                sum_list.append(self.__df)
            
            print("***************Done analysing of %s log file***************" % self.__year)
            plt.show()
            self.upload_path(sys.argv[2],sys.argv[3])
            self.__final_data = self.concatData(log_list)
            self.__final_summary = self.concatSummary(sum_list)
            self.upload(self.__final_data)
            self.upload(self.__final_summary)
            self.upload(self.__final_log)
            print("***************Done uploading***************" % self.__year)


if __name__ == '__main__':

    if len(sys.argv) > 0:
        year = sys.argv[1]
        md = AnalyseLog(year)
        md.startanalysing()

