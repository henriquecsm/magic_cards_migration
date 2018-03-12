import threading

from flask_restful import Resource
from resources import queue_consumer as consumer
from db import magiccard_db as db


class MoveAll(Resource):
    def get(self):
        t = threading.Thread(target= self.task1())
        t.start()
        return {'Status Code': '202'}

    def task1(self):
        id_list = db.get_expansion_all()
        post = GetExpID()
        flag = True
        for id in id_list:
            if flag or post.post(id):
                flag = False
                post.post(id)


class GetExpID(Resource):
    def post(self, id):
        result = db.get_magiccard_all(str(id))
        if result:
            while True:
                res = consumer.receive()
                if not res:
                    break
            print("Result: %s" % result)
            return result
        else:
            return {'Status Code': 'HTTP 404'}
