#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, abort, request, jsonify
from flask_restful import Resource, Api
import pandas as pd
import datetime

app = Flask(__name__)
api = Api(app)

tasks = pd.read_csv('pred_results.csv')

class Pred_Result(Resource):
    def get(self, key):
        result = {'issue': str(key) , 'predicted_resolution_date': str( tasks[tasks['_id'] == key ].resovle_date.values[0]) }
        return jsonify(result)
        

class Plan(Resource):
    def get(self, date):
        
        now = '2017-09-01'#datetime.datetime.now()
        
        result = {'now': str(pd.to_datetime(now).tz_localize(tz='UTC')) , \
                  'issues': tasks[ (pd.to_datetime(tasks['resovle_date']) >  pd.to_datetime(now).tz_localize(tz='UTC') ) &\
                                  (pd.to_datetime(tasks['resovle_date']) <  pd.to_datetime(date).tz_localize(tz='UTC') ) ][['_id','resovle_date']].to_dict(orient='records') }
        return jsonify(result)
        


api.add_resource(Pred_Result, '/api/issue/<key>/resolve-prediction/') 
api.add_resource(Plan, '/api/release/<date>/resolved-since-now') 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8383, debug=True)