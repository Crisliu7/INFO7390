import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from scipy.stats import pearsonr
from minepy import MINE


class MidTerm(self):

	def __init__(self):

		# Form training set
		ts = pd.read_csv('training_set.csv')#self.form_training_set()

		# Upload to AWS S3 bucket
    	training_set.csv = pd.write_csv(ts)
    	self.upload(training_set.csv, sys.argv[1], sys.argv[2])

		# Data cleaning
		ts = self.clean(ts)

		# Feature selection

		# Training

    def form_training_set(self):
    	''' Form the training set'''

    	# Read data
    	df_2016 = pd.read_csv("/Users/CJL-RMBP/Documents/INFO7390 Data Science/midterm/Data/properties_2016.csv")
		df_2017 = pd.read_csv("/Users/CJL-RMBP/Documents/INFO7390 Data Science/midterm/Data/properties_2017.csv")
		df_train_2016 = pd.read_csv("/Users/CJL-RMBP/Documents/INFO7390 Data Science/midterm/Data/train_2016_v2.csv")
		df_train_2017 = pd.read_csv("/Users/CJL-RMBP/Documents/INFO7390 Data Science/midterm/Data/train_2017.csv")

		# Concatenate
		df_2016['year'] = 2016
		df_2017['year'] = 2017
		frames = [df_2016, df_2017]
		properties = pd.concat(frames)
		properties.drop_duplicates(subset='parcelid')

		df_train_2016['year'] = 2016
		df_train_2017['year'] = 2017
		frames = [df_train_2016, df_train_2017]
		train = pd.concat(frames)
		train.drop_duplicates(subset='parcelid')

		ts = pd.merge(train, properties, how='left', on='parcelid')

		# Save memory
		del df_2016
		del df_2017
		del df_train_2016
		del df_train_2017
		del properties
		del train

		return ts

    def clean(self, df):

    	df[]
    	df.fillna(0)

    	return df   

    def feature_select() 
    	
		#方差选择法，返回值为特征选择后的数据，参数threshold为方差的阈值
		VarianceThreshold(threshold=3).fit_transform(iris.data)
		
		#选择K个最好的特征，返回选择特征后的数据
		#第一个参数为计算评估特征是否好的函数，该函数输入特征矩阵和目标向量，输出二元组（评分，P值）的数组，数组第i项为第i个特征的评分和P值。在此定义为计算相关系数
		#参数k为选择的特征个数
		SelectKBest(lambda X, Y: array(map(lambda x:pearsonr(x, Y), X.T)).T, k=2).fit_transform(iris.data, iris.target)

		#选择K个最好的特征，返回选择特征后的数据
		SelectKBest(chi2, k=2).fit_transform(iris.data, iris.target)

		#由于MINE的设计不是函数式的，定义mic方法将其为函数式的，返回一个二元组，二元组的第2项设置成固定的P值0.5
		def mic(x, y):
		    m = MINE()
		    m.compute_score(x, y)
		    return (m.mic(), 0.5)

		#选择K个最好的特征，返回特征选择后的数据
		SelectKBest(lambda X, Y: array(map(lambda x:mic(x, Y), X.T)).T, k=2).fit_transform(iris.data, iris.target)

		#递归特征消除法，返回特征选择后的数据
		#参数estimator为基模型
		#参数n_features_to_select为选择的特征个数
		RFE(estimator=LogisticRegression(), n_features_to_select=2).fit_transform(iris.data, iris.target)


    def upload(self, filename, ACCESS_NAME, ACCESS_KEY):
        '''Upload the file to the bucket'''

        print("*************** Uploading to AWS S3 bucket ***************")

        self.__ACCESS_NAME = ACCESS_NAME
        self.__ACCESS_KEY = ACCESS_KEY
        self.__BUCKET_NAME = "ZillowData"
        print("Accessing bucket name %s: " %  self.__BUCKET_NAME)

        data = open(filename, 'rb')

        s3 = boto3.resource(
            's3',
            aws_access_key_id=self.__ACCESS_NAME,
            aws_secret_access_key=self.__ACCESS_KEY,
            config=Config(signature_version='s3v4'))

        s3.Bucket(self.__BUCKET_NAME).put_object(Key=filename, Body=data)


if __name__ == "__main__":

	md = MidTerm()