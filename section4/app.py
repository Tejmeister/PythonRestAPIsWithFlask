from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "Tejas"
api = Api(app)

jwt = JWT(app=app, authentication_handler=authenticate, identity_handler=identity) # creates an endpoint /auth

items = []

class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price', type=float, required = True, help="This field cannot be blank")

	def get(self, name):
		item = next(filter(lambda x: x['name'] == name, items), None)
		#item = [item for item in items if item['name'] == name]
		if item:
			return item, 200
		return {'message': "Item not found"}, 404

	def post(self, name):
		#item = [item for item in items if item['name'] == name]
		if next(filter(lambda x: x['name'] == name, items), None):
			return {'message': f"Item with name {name} already exist"}, 400

		data = Item.parser.parse_args()

		item = {'name': name, 'price':data['price']}
		items.append(item)
		return item, 201

	def delete(self, name):
		global items
		items = list(filter(lambda x: x['name'] != name, items))
		return {'message': 'Item deleted'}

	def put(self, name):
		data = Item.parser.parse_args()
		
		item = next(filter(lambda x:x['name'] == name, items), None)
		if item is None:
			item = {'name': name, 'price': data['price']}
			items.append(item)
		else:
			item.update(data)

		return item

class ItemList(Resource):
	def get(self):
		return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)