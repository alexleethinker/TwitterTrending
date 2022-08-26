from pyspark.sql import SparkSession

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
    












from pyspark.sql import SparkSession
from pyspark.sql import Row,SQLContext
import sys



my_spark = SparkSession \
    .builder \
    .appName("TwitterTrendingApp") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1:27017/Tech-assignment.sample") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1:27017/Tech-assignment.sample") \
    .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:3.0.1') \
    .getOrCreate()



df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
df.printSchema()