import mysql.connector
from flask import Flask

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="airport_game",
    user="root",
    password='y""o32',
)

cursor = connection.cursor()

app = Flask(__name__)

@app.route("/airport/<ident>")

def airport_icao(ident):
    sql = "select ident, name, municipality from airport where ident = %s"
    cursor.execute(sql, (ident,))
    result = cursor.fetchone()
    response = {
        "ICAO": result[0],
        "Name": result[1],
        "Location": result[2]
    }
    return response

if __name__ == '__main__':
    app.run()