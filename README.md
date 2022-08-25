# TwitterTrending


tech-assignment

 The [Twitter trending topics](https://en.wikipedia.org/wiki/Twitter#Trending_topics) feature is bound to 
 
 - geographical areas, such as countries or cities
 - for different purposes you may want to determine trending topics amongst arbitrary groups of Twitter users. For example all the followers of your corporate account or networks of people that are somehow of special interest to you.



## Assignment
one or more Spark jobs 
take a set of Twitter data and two user input topic as input and produces a comparison of trend history for last week.
slope of the frequency of occurrence 
API `GET /api/trending_topics?param1=value&param2=value...&paramN=value`
- runs against both the small and larger sample data set.




### Required solution
#### 1. A Spark job which produces historical trend comparison (80%)
thought about the problem and perhaps expose ideas for improvement
#### 2. Presentation (20%)


### Evaluation

- Computer science
- Software development and craftmanship
- Distributed systems
- Coding productivity
- solid software engineering principles
    - testability
    - separation of concerns
    - fit-for-production code, etc.



## Note
If you have any questions or want clarification on the requirements, please email sbhuinya@datapebbles.com





 docker build -t spark:3.3 -f ./Docker/Spark/Dockerfile .
 docker build -t spark-worker:3.3 -f ./Docker/Spark-worker/Dockerfile .
 docker build -t python-runner -f ./Docker/Python-runner/Dockerfile .



docker-compose run --rm etl-runner python etl.py --fileName=Twitter-sample.json


 ! pip install pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row,SQLContext
import sys


mongo_uri = "mongodb://mongo:27017/Twitter.sample"

spark = SparkSession \
    .builder \
    .master("spark://spark-master:7077")\
    .appName("TwitterTrendingApp") \
    .config("spark.mongodb.input.uri", mongo_uri ) \
    .config("spark.mongodb.output.uri", mongo_uri ) \
    .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:3.0.1') \
    .getOrCreate()



df = spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
#df.printSchema()

df1 = df.select("created_at","text").na.drop()


import pyspark.sql.functions as f


trending = df1.withColumn('word', f.explode(f.split(f.col('text'), ' ')))\
    .groupBy('word')\
    .count()\
    .sort('count', ascending=False)
    
    
mongo_write = "mongodb://mongo:27017/Twitter.trending"

trending.select("word","count").write\
    .format('com.mongodb.spark.sql.DefaultSource')\
    .option( "uri", mongo_write) \
    .save()
    
    
client.close()