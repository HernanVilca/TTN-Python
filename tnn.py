import time
import ttn

app_id = "nodes-tecprec"
access_key = "ttn-account-v2.I6xWAARi2j9YAI-HCOZbzP-AqubRSqbqpNgnYmvy_Ok"

def uplink_callback(data, client):
  print("Time : ", str(data.metadata.time))

handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
time.sleep(60)
mqtt_client.close()

# using application manager client
app_client =  handler.application()
my_app = app_client.get()
print(my_app)
my_devices = app_client.devices()
print(my_devices)