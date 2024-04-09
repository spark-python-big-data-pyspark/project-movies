
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

df_akas = spark.read.csv('../data/clean/title_akas_clean.csv',header=True)


# Check Describe option similar to Pandas
df_akas.describe().show()

print("-----------------title_basics-------------------------")


# Read data
df_basic = spark.read.csv("../data/clean/title_basics_clean.csv",  header=True)


df_basic.show()

# Print Schema
df_basic.printSchema()
