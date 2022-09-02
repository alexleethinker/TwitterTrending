from urllib.request import urlopen
import json



def get_fileName():
    import argparse
    parser = argparse.ArgumentParser(description = 'Load json files into MongoDB.')
    parser.add_argument('--fileName', type = str, default='sample.json', help = 'The name of the file to load.')
    args = parser.parse_args()
    # fileName = 'sample' or "twitter-sample"
    fileName = args.fileName.replace('.json','').lower()
    return fileName

def get_mongo_collection(fileName):
    import pymongo
    from pymongo import MongoClient

    try:
        client = MongoClient('mongo', 27017, serverSelectionTimeoutMS= 10)
        client.server_info()
    except  pymongo.errors.ConnectionFailure:
        client = MongoClient('localhost', 27017)  
    db = client['Twitter']
    collection = db[fileName]
    collection.delete_many({})   # clear all existing documents before writing
    return collection

def url_json_insert(url, collection):
    for line in urlopen(url):
            try:
                    line_d = json.loads(line)
                    collection.insert_one(line_d)
            except Exception as e:
                    print(e)



if __name__ == "__main__":

    user = 'https://raw.github.com/alexleethinker/'
    repo = 'jsonFiles/main/'
    fileName = get_fileName() 

    url = user + repo + str(fileName) + '.json'
    collection = get_mongo_collection(fileName)
    url_json_insert(url, collection)
