import pyspark
from pyspark.sql import SparkSession

from main import spark



# Read data
df = spark.read.csv("../data/title_principals.tsv", sep="\t", header=True)

df.show()

# Print Schema
df.printSchema()# Read data


