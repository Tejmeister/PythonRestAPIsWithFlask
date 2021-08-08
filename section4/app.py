from flask import Flask, request
from flask.json import jsonify
from flask_restful import Resource, Api
from werkzeug.datastructures import T
from werkzeug.wrappers import request

app = Flask(__name__)
api = Api(app)


items = []

class Item(Resource):
	def get(self, name):
		item = next(filter(lambda x: x['name'] == name, items), None)
		#item = [item for item in items if item['name'] == name]
		if item:
			return item, 200
		return {'message': "Item not found"}, 404

	def post(self, name):
		item = [item for item in items if item['name'] == name]
		if item:
			return {'message: Item already exist'}
		data = request.get_json()
		item = {'name': name, 'price':data['price']}
		items.append(item)
		return item, 201

class ItemList(Resource):
	def get(self):
		return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Item, '/items')

app.run(port=5000, debug=True)