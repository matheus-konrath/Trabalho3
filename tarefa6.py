import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Mensagem recebida: {message.payload.decode()}")

def setup_mqtt_client():
    client = mqtt.Client()
    client.on_message = on_message
    try:
        client.connect("mqtt.eclipse.org", 1883, 60)
    except Exception as e:
        print(f"Erro ao conectar ao broker MQTT: {e}")
    client.subscribe("iot/sensor")
    return client

if __name__ == "__main__":
    client = setup_mqtt_client()
    client.publish("iot/sensor", "Mensagem segura")
    client.loop_start()
