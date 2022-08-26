import codecs
import json
import argparse

def json_insert(filePath, collection):
    with codecs.open(filePath, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            try:
                # in case regular regression is needed, use:
                # line = re.sub(r"[^\w\s[\u4e00-\u9fa5]:\"\'<>\\/-,{}']+",'', line)
                line_d = json.loads(str(line))
            
                collection.insert_one(line_d)
            
            except Exception as e:
                print(e)
        
        '''
        Errors Summary:

        Expecting ',' delimiter	                            4
        Expecting property name enclosed in double quotes	43
        Expecting value	                                    165
        Invalid control character at	                    1
        Unterminated string starting at	                    7
        '''


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description = 'Load json files into MongoDB.')
    parser.add_argument('--fileName', type = str, default='sample', help = 'The name of the file to load.')
    args = parser.parse_args()


    import os
    script_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(script_path)
    project_path = os.path.dirname(parent_path)

    fileName = args.fileName.replace('.json','')
    filePath = 'TwitterData/' + fileName + '.json'
    filePath = os.path.join(project_path, filePath)

    from pymongo import MongoClient
    
    try:
        client = MongoClient('mongo', 27017)
    except:
        client = MongoClient('localhost', 27017)
        
    db = client['Twitter']
    collection = db[fileName]

    json_insert(filePath, collection)
    
    client.close()