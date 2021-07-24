from random import choice
import paho.mqtt.client as mqtt
import time
#  function


def connect_msg():
    print('Connected to Broker')


randlist = [i for i in range(0, 100)]
client = mqtt.Client(client_id='Temperature sensor')
client.connect("127.0.0.1", 1883)

# Connecting callback functions
client.on_connect = connect_msg

# Connect to broker

while True:
    randData = choice(randlist)
    temp = 25 + 0.01*randData
    client.publish("house/temp", temp)
    print("Just published " + str(temp))
    time.sleep(2)
