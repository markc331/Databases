#
#   Function Name: Parser 
#
#   Description: Called within LoRa packet retrieval function, which passes in a string with data in the order of temperature,
#   humidity, moisture, and light intesity along with the signal strength of the LoRa connection as an integer. Function then 
#   splits string into their respective variables and captures the date and time of when the data is received and parsed. The
#   data is then stored into their respective column within the database and the user is notified of the succesful storage of
#   of the received data.
#

from datetime import date
import os
import mysql.connector as database
import time

connection = database.connect( 
    user = 'user',
    password = 'password',
    host = "localhost",
    database = 'sensor_data',
)

cursor = connection.cursor()

def parser(string, rssi):
    floats = [float(x) for x in string.split(" ")]
    print(floats)
    
    temperature = floats[0]
    humidity = floats[1]
    moisture = floats[2]
    light_intensity = floats[3]
    
    print(temperature)
    print(humidity)
    print(moisture)
    print(light_intensity)
    
    print(rssi)
    
    today = date.today()
    
    print(today)
    
    t = time.localtime() 
    current_time = time.strftime("%H:%M:%S", t)
    
    print(current_time)
    
    
    statement = ("INSERT INTO sensor "
               "(humidity, temperature, moisture, rssi, light_intensity, time, date) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    data = (humidity, temperature, moisture, rssi, light_intensity, current_time, today)
    cursor.execute(statement, data)
    connection.commit()
    print("Successfully added entry to database")
    cursor.close()
    connection.close()

        