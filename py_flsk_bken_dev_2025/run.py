from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB URI
app.config["MONGO_URI"] = "mongodb://localhost:27017/p_f_bken2025"

# Initialize Mongo
mongo = PyMongo(app)

# Reference to the collection
collection = mongo.db.accuzr

# Create
@app.route('/add', methods=['POST'])
def add_record():
    data = request.json  # Get the data from the JSON body
    collection.insert_one(data)  # Insert into MongoDB
    return jsonify(message="Record added successfully"), 201

# Read (get all records)
@app.route('/records', methods=['GET'])
def get_all_records():
    records = list(collection.find())  # Fetch all records from MongoDB
    # Convert ObjectId to string for JSON compatibility
    for record in records:
        record['_id'] = str(record['_id'])
    return jsonify(records), 200

# Read (get a record by ID)
@app.route('/record/<record_id>', methods=['GET'])
def get_record(record_id):
    record = collection.find_one({'_id': ObjectId(record_id)})  # Fetch a specific record by ID
    if record:
        record['_id'] = str(record['_id'])  # Convert ObjectId to string
        return jsonify(record), 200
    return jsonify(message="Record not found"), 404

# Update (update a record)
@app.route('/update/<record_id>', methods=['PUT'])
def update_record(record_id):
    data = request.json  # Get the data to update
    result = collection.update_one({'_id': ObjectId(record_id)}, {'$set': data})
    if result.matched_count > 0:
        return jsonify(message="Record updated successfully"), 200
    return jsonify(message="Record not found"), 404

# Delete (delete a record)
@app.route('/delete/<record_id>', methods=['DELETE'])
def delete_record(record_id):
    result = collection.delete_one({'_id': ObjectId(record_id)})  # Delete the record by ID
    if result.deleted_count > 0:
        return jsonify(message="Record deleted successfully"), 200
    return jsonify(message="Record not found"), 404

if __name__ == "__main__":
    app.run(debug=True)
