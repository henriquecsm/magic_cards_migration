import json
import pika
from models import file as of
from os.path import exists

file = "/home/hcesar/Documents/python_app/magic_cards_migration/tmp/cards_db.txt"

def receive():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='moving_cards', exchange_type='direct')

    channel.queue_declare(exclusive=True)

    channel.queue_bind(exchange='moving_cards', queue='moving_cards', routing_key='moving_cards')
    method_frame, header_frame, body = channel.basic_get(queue = 'moving_cards')

    if method_frame is None:
        connection.close()
        return False
    else:
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        connection.close()
        data = json.loads(body)
        temp = ''
        if exists(file):
            temp = of.read_file(file)
            # print("temp: %s" % temp)

        of.write_file(file, json.dumps(data) + "\n" + temp)

        return body

