from flask_restful import Resource
from models import file as f
from os.path import exists
import json

file = '/home/hcesar/Documents/python_app/magic_cards_migration/tmp/cards_db.txt'

class GetCards(Resource):
    def get(self, id):

        if not exists(file):
            return {"status": "HTTP 404"}

        d =f.read_file(file)

        lines = d.split("\n")
        data = []
        list_item = []

        for line in lines:
            if not line == "":
                data = data + json.loads(line)
                print(line)

        for i in data:
            if i['GathererId'] == str(id):
                list_item.append(i)

        print(list_item)

        return {"status": "success", "data": list_item}, 200
