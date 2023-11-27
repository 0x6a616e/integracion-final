from os import getenv
from flask import Flask, request, Response, jsonify
from flask_mysqldb import MySQL
import xml.etree.ElementTree as ET

app = Flask(__name__)

app.config["MYSQL_HOST"] = getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = getenv("MYSQL_DB")

mysql = MySQL(app)


def getColumns(table):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute(f"SHOW COLUMNS FROM `{table}`;")
    except:
        cursor.close()
        return []
    columns = [column[0] for column in cursor.fetchall()]
    cursor.close()
    return columns


@app.route("/<table>", methods=["GET"])
def getTable(table):
    columns = getColumns(table)
    if not columns:
        return "Table not found", 404
    formato = request.args.get("format", "json")
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM `{table}`;")
    datos = cursor.fetchall()
    cursor.close()
    if formato == "json":
        data = []
        for i in range(len(datos)):
            data.append({})
            for j in range(len(datos[i])):
                data[i][columns[j]] = str(datos[i][j])
        return jsonify(data=data, status=200, mimetype="application/json")
    elif formato == "xml":
        entries = ET.Element("entradas")
        for i in range(len(datos)):
            entrie = ET.SubElement(entries, "entrada")
            for j in range(len(datos[i])):
                element = ET.SubElement(entrie, columns[j])
                element.text = str(datos[i][j])
        arbol = ET.ElementTree(entries)
        arbol = ET.tostring(arbol.getroot(), encoding="UTF-8")
        return Response(arbol, content_type="text/xml")
    return "404 :3"


if __name__ == "__main__":
    app.run(debug=True)
