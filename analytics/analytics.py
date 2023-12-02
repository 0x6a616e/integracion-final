from urllib.request import urlopen
import json
import pandas as pd
import matplotlib.pyplot as plt

response = urlopen("http://34.70.30.227:5000/data/truck")
json_data = response.read().decode('utf-8', 'replace')

d = json.loads(json_data)
df = pd.json_normalize(d['data'])

df_routes_per_company = df[["company_id", "route_count"]].astype({"company_id": "string", "route_count": "int"})
df_routes_per_company = df_routes_per_company.groupby("company_id").sum()
df_routes_per_company.to_csv("routes_per_company.csv", sep=",", encoding="utf-8")
plt.xticks(rotation=90)
plt.scatter(df_routes_per_company.index, df_routes_per_company[["route_count"]])
plt.xlabel("ID de la compañía")
plt.ylabel("Cantidad de rutas")
plt.title("Rutas por compañía")
plt.savefig("routes_per_company")

plt.clf()

df_distance_per_company = df[["company_id", "total_distance"]].astype({"company_id": "string", "total_distance": "float"})
df_distance_per_company = df_distance_per_company.groupby("company_id").mean()
df_distance_per_company.to_csv("distance_per_company.csv", sep=",", encoding="utf-8")
plt.xticks(rotation=90)
plt.scatter(df_distance_per_company.index, df_distance_per_company[["total_distance"]])
plt.xlabel("ID de la compañía")
plt.ylabel("Distancia")
plt.title("Distancia media por compañía")
plt.savefig("mean_distance_per_company")
