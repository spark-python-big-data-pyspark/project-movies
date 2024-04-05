
# Import libreries
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

print("-----------------name-------------------------")
# Read data
df_name = spark.read.csv("../data/clean/name.csv",  header=True)

df_name.head(5)

# Print Schema
df_name.printSchema()


print("-----------------title_akas-------------------------")

df_akas = spark.read.csv('../data/clean/title_akas.csv',header=True)


# Check Describe option similar to Pandas
df_akas.describe().show()

# count_nulls_region = df_akas.select(sum(col("region").isNull().cast("int")).alias("Nulls")).collect()[0]["Nulls"]
# count_nulls_region_N = df_akas.filter(col("region") == "\\N").count()
# print("nulls region':", count_nulls_region,count_nulls_region_N)

# count_nulls_language = df_akas.select(sum(col("language").isNull().cast("int")).alias("Nulls")).collect()[0]["Nulls"]
# print("nulls language':", count_nulls_language)
# print("-----------------title_basics-------------------------")


# # Read data
# df_basic = spark.read.csv("../data/title_basics.tsv", sep="\t", header=True)


# df_basic.show()

# # Print Schema
# df_basic.printSchema()
