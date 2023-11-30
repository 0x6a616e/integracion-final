from os import getenv
from flask import Flask, request, jsonify
from flask_cors import cross_origin
from flask_mysqldb import MySQL
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["MYSQL_HOST"] = getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = getenv("MYSQL_DB")
app.config["SECRET_KEY"] = getenv("SECRET_KEY")

mysql = MySQL(app)


@app.route("/login", methods=["GET"])
@cross_origin()
def login():
    return "Hola", 200


if __name__ == "__main__":
    app.run(debug=True)
