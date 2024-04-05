import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode
from explode_row import explode_row
from pyspark.sql.functions import col, sum


# create SparkSession
spark = SparkSession.builder.appName("Practice").getOrCreate()

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("project-movies") \
    .getOrCreate()


df_name = spark.read.csv("../data/name.tsv", sep="\t", header=True)