from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
MONGO_URI = "mongodb://database:27017/"
client = MongoClient(MONGO_URI)
db = client["user_data"]
collection = db["users"]

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    if name and email:
        # Store data in MongoDB
        user_data = {'name': name, 'email': email}
        collection.insert_one(user_data)
        return jsonify({'message': 'Data stored successfully'}), 200
    else:
        return jsonify({'error': 'Name and email are required'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
