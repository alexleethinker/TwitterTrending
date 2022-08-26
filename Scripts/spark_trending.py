from pyspark.sql import SparkSession
import pyspark.sql.functions as f

def SparkTrends(fileName, spark_master, mongo_uri):

    mongo_read = mongo_uri + "/Twitter." + fileName

    spark = SparkSession \
        .builder \
        .master(spark_master)\
        .appName("TwitterTrendingApp") \
        .config("spark.mongodb.input.uri", mongo_read) \
        .config("spark.mongodb.output.uri", mongo_read) \
        .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:3.0.1') \
        .getOrCreate()

    sample_df = spark.read.format("com.mongodb.spark.sql.DefaultSource").load()

    # extract ['created_at','text'] columns from original dataframe for further analysis
    if fileName.lower() == 'sample':
        text_df = sample_df.select("created_at","text").na.drop()
    elif fileName.lower() == 'twitter-sample':
        from pyspark.sql.functions import col
        text_df = sample_df.select(col("interaction.created_at"), col("interaction.content")).na.drop().withColumnRenamed("content","text")
    else:
        print('file name not supported!')

    # do word frequency count on the text field
    # use simplest stop word ' '
    trending = text_df.withColumn('word', f.explode(f.split(f.col('text'), ' ')))\
        .groupBy('word')\
        .count()\
        .sort('count', ascending=False)
        
    # write results into a new collection in mongodb
    mongo_write = mongo_uri + "/Twitter.trends-" + fileName
    trending.select("word","count").write\
        .format('com.mongodb.spark.sql.DefaultSource')\
        .mode("overwrite")\
        .option( "uri", mongo_write) \
        .save()

    spark.stop()


if __name__ == "__main__":
    
    import argparse
    parser = argparse.ArgumentParser(description = 'Load json files into MongoDB.')
    parser.add_argument('--fileName', type = str, default='sample', help = 'The name of the file to load.')
    args = parser.parse_args()
    
    # fileName = 'sample' or "twitter-sample"
    fileName = args.fileName.replace('.json','').lower()

    # can be replaced by os.
    import os
    spark_master = "spark://spark-master:7077" or os.environ.get('SPARK_MASTER')
    mongo_uri = "mongodb://mongo:27017"  or os.environ.get('MONGO_HOST')
    
    SparkTrends(fileName, spark_master, mongo_uri)