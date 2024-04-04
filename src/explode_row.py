import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode

def explode_row(df, column):



  df = df.withColumn(column, split(df[column], ","))

  print("separado")
  df.show()

  # Expand rows for each separate item in knownForTitles
  df_explode = df.select("*", explode(df[column]).alias(f'{column}_split'))

  print("expandido")
  df_explode.show(truncate=False)

  return df_explode