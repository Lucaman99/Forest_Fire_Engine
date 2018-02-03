# This code communicates with a local MySQL Database
from datetime import datetime
import MySQLdb
import time
import math
datetime_data = datetime.now()
db = MySQLdb.connect(host="localhost", user="root", passwd="Password", db="forest_fire_data")
initialize_variables = {"wind_direction":'a', "wind_magnitude":"b", "ambient_humidity":"c", "tree_density":"d", 
"ambient_heat":"e", "terrain_fluctuations_comp":"f", "weather_data_received_online":"g", "time_stamp":"h", "query_number":"i"}
extract_data = True
initialize_variables_index = initialize_variables.keys()
def data_update():
		cur = db.cursor()
		cur.execute("INSERT INTO initial_numerical_values (wind_direction, wind_magnitude, ambient_humidity, tree_density, ambient_heat, terrain_fluctuations_comp, weather_data_score, time_stamp, query_number) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (initialize_variables['wind_direction'], initialize_variables['wind_magnitude'], initialize_variables['ambient_humidity'], initialize_variables['tree_density'], initialize_variables['ambient_heat'], initialize_variables['terrain_fluctuations_comp'], initialize_variables['weather_data_received_online'], initialize_variables['time_stamp'], initialize_variables['query_number']))
	 	db.commit()
	 	db.close()
data_update()
print("Query Sent")
