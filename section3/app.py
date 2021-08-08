from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
	{
		"name" : "Tejas Store",
		"items": [{
			"name": "Item1",
			"price": 23
			}
		]
	}
]

@app.route('/')
def home():
	return render_template('index.html')

# GET stores
@app.route('/store', methods=['GET'])
def get_stores():
	return jsonify({'stores': stores})

# GET store by name
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
	found_store = [store for store in stores if store['name'] == name]

	if found_store:
		return jsonify(found_store)
	return "No store found with name {name}"

# GET store items
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
	return f"Getting item from store {name}"

# POST store
@app.route('/store', methods=['POST'])
def create_store():
	request_data = request.get_json()
	new_store = {
		'name': request_data['name'],
		'items': []
	}

	stores.append(new_store)
	return jsonify(new_store)

# POST store item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
	return f"Creating item in store {name}"


app.run(port=5000)