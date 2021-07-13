from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonreactdb'
mongo = PyMongo(app)
db = mongo.db.users

@app.route('/users', methods=['POST'])
def createUser():
    id = db.insert({
        'userName' : request.json['userName'],
        'userEmail' : request.json['userEmail'],
        'password' : request.json['password']
    })
    print(str(ObjectId(id)))
    return jsonify(str(ObjectId(id)))

@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for user in db.find():
        users.append({
            '_id': str(ObjectId(user['_id'])),
            'name' : user['userName'],
            'email' : user['userEmail'],
            'password' : user['password']
        })
    return jsonify(users)

@app.route('/user/<id>', methods=['GET'])
def getUser(id):
    return "received"

@app.route('/users/<id>', methods=['GET'])
def deleteUser(id):
    return "received"

@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    return "received"

if __name__ == '__main__':
    app.run(debug=True)