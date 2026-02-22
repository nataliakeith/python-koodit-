import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='y""o32',
    autocommit=True
)
def airport_area_code(area):
    sql = f"SELECT name, type from airport where iso_country = '{area}' order by type;"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0:
        for row in result:
            print(f"{row[0]} {row[1]}")
    return
area_code = input("Enter area code: ")
airport_area_code(area_code)
