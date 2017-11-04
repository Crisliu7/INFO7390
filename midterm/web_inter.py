import numpy as np
import pandas as pd
import pickle
from sklearn.externals import joblib

from flask import Flask
from flask import request
from flask import jsonify
from flask import abort

my_rf = pickle.load(open('random_forest.pkl','rb'))

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def make_predict():

	data = request.get_json(force=True)
	print(data.keys())
	d = [data['taxamount'],data['longitude'],data['latitude'],\
		 data['finishedsquarefeet12'],data['lotsizesquarefeet'],\
		 data['regionidzip'],data['month'],data['yearbuilt']]

	test = np.array(d)

	print(test)

	df = pd.DataFrame(test,index=['taxamount','longitude','latitude',\
				  		    	  'finishedsquarefeet12','lotsizesquarefeet','regionidzip',\
				 		    	  'month','yearbuilt'])
	a = df.transpose()
	y_pred = my_rf.predict(a)
	print(y_pred)

	output = [y_pred[0]]

	return jsonify(results=output)

def load_model():

	print("Loading model from AWS S3...")

if "__name__" == "__main__":
	app.run(port=9000, debug=True)

# [data['taxamount'],data['longitude'],data['latitude'],data['bedroomcnt'],\
# 		 data['calculatedfinishedsquarefeet'],data['lotsizesquarefeet'],\
# 		 data['regionidzip'],data['month'],data['yearbuilt']]
# test = pd.DataFrame.from_items((i,d), orient='index', \
# 				 				columns=['taxamount','longitude','latitude','bedroomcnt',\
# 				  		    	'calculatedfinishedsquarefeet','lotsizesquarefeet','regionidzip',\
# 				 		    	'month','yearbuilt'])

