import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Mensagem recebida: {message.payload.decode()}")

def setup_mqtt_client():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("mqtt.eclipse.org", 1883, 60)
    client.subscribe("iot/sensor")
    return client

if __name__ == "__main__":
    client = setup_mqtt_client()
    client.publish("iot/sensor", "Mensagem segura")
    client.loop_start()
