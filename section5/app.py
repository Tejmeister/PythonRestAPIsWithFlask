from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
# Helps to propogate the actual error codes in the response which might have been generated inside the code
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'Tejas'
api = Api(app)

jwt = JWT(app=app, authentication_handler=authenticate, identity_handler=identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
	app.run(debug=True) 
