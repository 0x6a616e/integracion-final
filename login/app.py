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
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

jwt = JWTManager(app)

mysql = MySQL(app)


@app.route("/login", methods=["POST"])
@cross_origin()
def login():
    cursor = mysql.connection.cursor()
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    cursor.execute("SELECT id, is_admin FROM identity WHERE username = %s AND password = %s;", (username, password))
    data = cursor.fetchone()
    cursor.close()
    json_data = {"user_id": None, "is_admin": None, "token": None}
    if data:
        json_data["user_id"] = data[0]
        json_data["is_admin"] = data[1]
        json_data["token"] = create_access_token(identity=data[0])
    return jsonify(json_data)


if __name__ == "__main__":
    app.run(debug=True)
