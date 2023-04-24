from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Spark Test") \
    .master("local[*]") \
    .getOrCreate()

data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

df.show()
