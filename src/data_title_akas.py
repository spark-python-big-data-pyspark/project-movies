import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode
from explode_row import explode_row
from pyspark.sql.functions import col, sum

from main import spark


# Read data
df_akas = spark.read.csv("../data/title_akas.tsv", sep="\t", header=True)


df_akas.show()

# Print Schema
df_akas.printSchema()

# Filter types = original
df_akas.filter(col("types") == "original").show()

df_akas.write.csv("../data/clean/title_akas_clean.csv", header=True, mode="overwrite")