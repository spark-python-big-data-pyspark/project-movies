import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode

def explode_row(df, column):

  new_column = f'{column}_split'

  df = df.withColumn(column, split(df[column], ","))

  print("separado")
  df.show()

  # Expand rows for each separate item in knownForTitles
  df_explode = df.select("*", explode(df[column]).alias(new_column))

  df_explode.show(truncate=False)

  df_explode = df_explode.drop(column)

  df_explode = df_explode.withColumnRenamed(new_column, column)

  return df_explode