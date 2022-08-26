#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
app.config["BUNDLE_ERRORS"] = True
api = Api(app)

class Trending(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('source', type=str,  required=True , location='args')
        self.parser.add_argument('topic', type=str,  required=True , location='args')

    def get(self):
        data = self.parser.parse_args()
        source = data.get('source').lower()
        user_topic = data.get('topic').lower()

        collection = db['trends-' + str(source)]

        try:
            result = {  
                        'Hot Topic': str( collection.find({},{ "word": 1, 'count': 1 }).sort("count", -1)[0]['word']), \
                        'Hot Topic Trends' : str( collection.find({},{ "word": 1, 'count': 1 }).sort("count", -1)[0]['count']), \
                        'User Topic': str(user_topic)  ,\
                        'User Topic Trends': str( collection.find({"word": user_topic},{ "word": 1, 'count': 1 })[0]['count']) 
                        }
        except IndexError:
            result = {  
                        'Hot Topic': str( collection.find({},{ "word": 1, 'count': 1 }).sort("count", -1)[0]['word']), \
                        'Hot Topic Trends' : str( collection.find({},{ "word": 1, 'count': 1 }).sort("count", -1)[0]['count']), \
                        'Message': 'The topic you selected was not shown up in the past 7 days'
                        }            
        return jsonify(result)


api.add_resource(Trending, '/api/trends', endpoint = 'trends') 


if __name__ == "__main__":
    from pymongo import MongoClient
    try:
        client = MongoClient('mongo', 27017)
    except:
        client = MongoClient('localhost', 27017)

    db = client['Twitter']
    
    app.run(host="0.0.0.0", port=8383, debug=False)