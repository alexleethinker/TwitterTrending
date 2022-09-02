# from hdfs import *
# client = Client("http://localhost:9870")

from hdfs import InsecureClient
client = InsecureClient('http://localhost:9870')

with client.read('/sample.json') as reader:
  print(reader)
