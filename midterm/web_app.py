import numpy as np
import pandas as pd
from flask import Flask, jsonify, abort, request
import pickle
import base64

my_rf = pickle.load(open('random_forest.pkl','rb'))

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def make_predict():

	data = request.get_json(force=True)
	d = [data['taxamount'],data['longitude'],data['latitude'],data['bedroomcnt'],\
		 data['calculatedfinishedsquarefeet'],data['lotsizesquarefeet'],\
		 data['regionidzip'],data['month'],data['yearbuilt']]
	for i in range(int(len(d)/9)):
		test = pd.DataFrame.from_items((i,d), orient='index', \
						 				columns=['taxamount','longitude','latitude','bedroomcnt',\
						  		    	'calculatedfinishedsquarefeet','lotsizesquarefeet','regionidzip',\
						 		    	'month','yearbuilt'])
	print(test)

	y_pred = my_rf.predict(test)

	output = [y_pred]

	return jsonify(results=output)

if "__name__" == "__main__":
	app.run(port=9000, debug=True)

