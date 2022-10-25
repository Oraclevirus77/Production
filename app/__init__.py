from flask_restx import Api
from flask import Blueprint


blueprint = Blueprint('api', __name__)
api = Api(blueprint,
          title="Alt School Backend Python",
          version="1.0",
          description="Alt School Backend Python",
          )
