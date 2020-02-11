# Imports
import sys
import time
import ttn
import base64
#database
import psycopg2
import uuid

app_id = "nodes-tecprec"
access_key = "ttn-account-v2.I6xWAARi2j9YAI-HCOZbzP-AqubRSqbqpNgnYmvy_Ok"

conn = psycopg2.connect(
  database="db_tecprec",
  user="debs",
  password="123456",
  host="localhost",
  port="5435"
)
# id_t = uuid.uuid4().hex
# cur = conn.cursor()
# cur.execute("INSERT INTO almacen_dato VALUES (%s, %s, %s)", (id_t,'temprepp', '23'))
# conn.commit()

def uplink_callback(data, client):
  print("*** Received uplink ***")
  # Show uplink message
  print(str(data))
  print()
  print("App_id : ", str(data.app_id))
  print("Dev_id : ", str(data.dev_id))
  print("HW serial : ", str(data.hardware_serial))
  print("Frequency : ", str(data.metadata.frequency))
  print("Gateway ID: ", str(data.metadata.gateways[0].gtw_id))
  tem = str(data.payload_fields.temperature_2)
  print("Temperatura : ", tem)
  arra = []
  arra.append(tem)
  print ('ssssssss: ', arra)
  print ('ARRAYS XD: ', arra[0])
  
  print ('id', uuid.uuid4().hex)
  id_tem = uuid.uuid4().hex
  cur = conn.cursor()
  tempt = 'temperatura'
  cur.execute("INSERT INTO almacen_dato VALUES (%s, %s, %s)", (id_tem,tempt, tem))
  conn.commit()
  print ('arrays : ', arra_cont)

  print("Humedad : ", str(data.payload_fields.relative_humidity_7))
  print()
  print("Raw data : ", str(data.payload_raw))
  # Decode base64 message
  message = base64.b64decode(data.payload_raw)
  print("Decode B64: " , message.decode("utf-8"))
  print()
  

# Define TTN handler
print("TTN MQTT client started")
handler = ttn.HandlerClient(app_id, access_key)
# MQTT client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)

mqtt_client.connect()
print("Client connected")


# Endless loop
try:
# Wait for uplink message
  while True:
    time.sleep(60)
except KeyboardInterrupt:
# Ctrl+C pressed
  print()
  print('Interrupted...')
  # Graceful exit
mqtt_client.close()
print("Client closed")
sys.exit(0)
