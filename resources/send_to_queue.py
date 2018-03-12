import pika
import json

QUEUE_TOPIC = 'moving_cards'

def send(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='moving_cards', exchange_type='direct')
    channel.queue_declare(queue='moving_cards')

    message = json.dumps(data)

    channel.basic_publish(exchange='moving_cards', routing_key=QUEUE_TOPIC, body=message)
    connection.close()
