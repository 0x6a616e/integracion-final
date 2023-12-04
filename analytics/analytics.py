from urllib.request import urlopen
import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("analytics").getOrCreate()

response = urlopen("http://34.70.30.227:5000/data/truck")
json_data = response.read().decode('utf-8', 'replace')

d = json.loads(json_data)
df = spark.createDataFrame(d["data"])

df1 = df.select("company_id", "route_count")
df1 = df1.withColumn("route_count", col("route_count").cast("Integer"))
df1 = df1.groupby("company_id").sum("route_count")
df1.write.mode("append").option("header", True).csv("routes_per_company")

df2 = df[["company_id", "total_distance"]]
df2 = df2.withColumn("total_distance", df2.total_distance.cast("float"))
df2 = df2.groupby("company_id").mean()
df2.write.mode("append").option("header", True).csv("distance_per_company")
