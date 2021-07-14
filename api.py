from flask import Flask
from flask_restful import Resource, Api
from usage_search import search_entry
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)

#search entry endpoint
class SearchWord(Resource):
    def get(self, word):
        return {'results': search_entry(word)}

api.add_resource(SearchWord, '/<string:word>')

if __name__ == '__main__':
    app.run(debug=True)