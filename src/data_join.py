
import pyspark
from pyspark.sql import SparkSession

from main import spark



df_basic = spark.read.csv("../data/clean/title_basics_clean.csv",  header=True)

df_ratings = spark.read.csv("../data/title_ratings.tsv", sep="\t", header=True)





df_joined = df_basic.join(df_ratings, on='tconst', how='inner')

df_joined.show()