import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='y""o32',
    autocommit=True
)
def airport_icao(icao):
    sql = f"SELECT ident, name, municipality from airport where ident='{icao}';"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0:
        for row in result:
            print(f"Airport is {row[1]} and location is {row[2]}")
    return
icao = input("Enter ICAO code: ")
airport_icao(icao)
