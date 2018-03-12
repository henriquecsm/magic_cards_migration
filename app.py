from flask import Blueprint
from flask_restful import Api
from resources.moveall import MoveAll
from resources.moveall import GetExpID
from resources.get_cards import GetCards

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(MoveAll, '/moveall')
api.add_resource(GetExpID, '/movecards/<int:id>')
api.add_resource(GetCards, '/card/<int:id>')
