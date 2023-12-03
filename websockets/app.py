from os import getenv
from flask import Flask, request, Response, jsonify
from flask_mysqldb import MySQL
from flask_socketio import SocketIO
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["MYSQL_HOST"] = getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = getenv("MYSQL_DB")

socketio = SocketIO(app, cors_allowed_origins = "*")


mysql = MySQL(app)


def getOrderCoordinates(id):

    cursor = mysql.connection.cursor()
    query = "SELECT latitude, longitude FROM orders WHERE id = %s;"
    cursor.execute(query, (id,))

    data = cursor.fetchone()

    json_data = {}
    json_data["latitude"] = data[0]
    json_data["longitude"] = data[1]

    cursor.close()
    return jsonify(data=json_data, status=200, mimetype="application/json")


@socketio.on('change')
def handle_change(message):

    if message != "User connected!": 

        datos = getOrderCoordinates(message)

        send(datos)



if __name__ == "__main__":
    socketio.run(debug=True)
