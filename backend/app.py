from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
# Assuming the MongoDB service is named 'mongo' in your docker-compose.yml,
# and the database name is 'yourdb'.
client = MongoClient("mongodb://mongo:27017/")
db = client['yourdb']

@app.route('/store', methods=['POST'])
def store():
    # Getting data from the request
    name = request.json.get('name')
    email = request.json.get('email')
    # Performing an insert operation
    result = db.users.insert_one({'name': name, 'email': email})
    # Returning a success response
    return jsonify(message="Data stored successfully", id=str(result.inserted_id)), 201

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
