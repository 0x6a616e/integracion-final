from urllib.request import urlopen
import json
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("analytics").getOrCreate()

response = urlopen("http://34.70.30.227:5000/data/truck")
json_data = response.read().decode('utf-8', 'replace')

d = json.loads(json_data)
df = spark.read.json(d["data"])

df_routes_per_company = df[["company_id", "route_count"]].astype({"company_id": "string", "route_count": "int"})
df_routes_per_company = df_routes_per_company.groupby("company_id").sum()
df_routes_per_company.to_csv("routes_per_company.csv", sep=",", encoding="utf-8")

df_distance_per_company = df[["company_id", "total_distance"]].astype({"company_id": "string", "total_distance": "float"})
df_distance_per_company = df_distance_per_company.groupby("company_id").mean()
df_distance_per_company.to_csv("distance_per_company.csv", sep=",", encoding="utf-8")
