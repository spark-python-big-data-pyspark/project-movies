
# Import libreries
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode
from explode_row import explode_row



# create SparkSession
spark = SparkSession.builder.appName("Practice").getOrCreate()

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("project-movies") \
    .getOrCreate()

print("-----------------name-------------------------")
# Read data
df_name = spark.read.csv("../data/name.tsv", sep="\t", header=True)


df_name.show()

# Print Schema
df_name.printSchema()

# Check Describe option similar to Pandas
df_name.describe().show()

explode_row(df_name,"knownForTitles")

# Check Describe option similar to Pandas
df_name.describe().show()


print("-----------------title_akas-------------------------")


# # Read data
# df_akas = spark.read.csv("../data/title_akas.tsv", sep="\t", header=True)


# df_akas.show()

# # Print Schema
# df_akas.printSchema()


# print("-----------------title_basics-------------------------")


# # Read data
# df_basic = spark.read.csv("../data/title_basics.tsv", sep="\t", header=True)


# df_basic.show()

# # Print Schema
# df_basic.printSchema()
