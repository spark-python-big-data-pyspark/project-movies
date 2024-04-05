
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode
from explode_row import explode_row
from pyspark.sql.functions import col, sum

from main import spark


# Read data
df_name = spark.read.csv("../data/name.tsv", sep="\t", header=True)

df_name.show()

# Print Schema
df_name.printSchema()

# Check Describe option similar to Pandas
#df_name.describe().show()

df_name = explode_row(df_name,"knownForTitles")



# Check Describe option similar to Pandas
df_name.show()


df_name.write.csv("../data/clean/name.csv", header=True, mode="overwrite")