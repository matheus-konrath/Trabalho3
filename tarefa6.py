import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Mensagem recebida: {message.payload.decode()}")

def setup_mqtt_client(broker_address="mqtt.eclipse.org"):
    client = mqtt.Client()
    client.on_message = on_message
    try:
        client.connect(broker_address, 1883, 60)
    except Exception as e:
        print(f"Erro ao conectar ao broker MQTT: {e}")
    client.subscribe("iot/sensor")
    return client

if __name__ == "__main__":
    # Tentar conectar ao broker padrão
    client = setup_mqtt_client()
    if not client.is_connected():
        # Se a conexão falhar, tentar um endereço IP alternativo
        client = setup_mqtt_client("test.mosquitto.org")
        if not client.is_connected():
            # Tentar um endereço IP direto (substitua pelo IP correto do broker MQTT)
            client = setup_mqtt_client("192.168.100.1")  
            if not client.is_connected():
                print("Não foi possível conectar a nenhum broker MQTT.")

    client.publish("iot/sensor", "Mensagem segura")
    client.loop_start()
