import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='y""o32',
    autocommit=True
)

def calculate_distance(icao1, icao2):
    cursor = connection.cursor()
    sql = "select latitude_deg, longitude_deg from airport where ident = %s"

    cursor.execute(sql, (icao1,))
    location1 = cursor.fetchall()

    cursor.execute(sql, (icao2,))
    location2 = cursor.fetchall()

    if location1 and location2:
        distance = geodesic(location1, location2).km
        print(f"Distance: {distance:.2f} km")
    else:
        print("Invalid ICAO code.")


icao1 = input("Enter ICAO code: ")
icao2 = input("Enter ICAO code:")
calculate_distance(icao1, icao2)





