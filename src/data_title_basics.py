import pyspark
from pyspark.sql import SparkSession

from explode_row import explode_row

from main import spark


# Read data
df_basic = spark.read.csv("../data/title_basics.tsv", sep="\t", header=True)

df_basic.show()

# Print Schema
df_basic.printSchema()

df_basic = explode_row(df_basic,"genres")
df_basic.show()


df_basic.write.csv("../data/clean/title_basics_clean.csv", header=True, mode="overwrite")