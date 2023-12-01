from os import getenv
from flask import Flask, jsonify, request
from flask_cors import cross_origin
from flask_jwt_extended import JWTManager, create_access_token
from flask_mysqldb import MySQL
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["MYSQL_HOST"] = getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = getenv("MYSQL_DB")
app.config["JWT_SECRET_KEY"] = getenv("APP_SECRET")

jwt = JWTManager(app)

mysql = MySQL(app)


@app.route("/login", methods=["POST"])
@cross_origin()
def login():
    cursor = mysql.connection.cursor()
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    cursor.execute("SELECT id FROM identity WHERE username = %s AND password = %s;", (username, password))
    id = cursor.fetchone()
    cursor.close()
    if id:
        token = create_access_token(identity=id[0])
    else:
        token = ""
    return jsonify(token=token)


if __name__ == "__main__":
    app.run(debug=True)
