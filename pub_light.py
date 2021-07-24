from random import choice
import paho.mqtt.client as mqtt
import time
#  function


def connect_msg():
    print('Connected to Broker')


randlist = [i for i in range(0, 100)]
client = mqtt.Client(client_id='Light')


client.connect("127.0.0.1", 1883)
client.on_connect = connect_msg

while True:
    randData = ["On", "Off"]
    light1 = choice(randData)
    client.publish("house/light1", light1)
    print("Just published " + str(light1))
    time.sleep(2)
