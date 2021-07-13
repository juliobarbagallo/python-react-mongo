from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonreactdb'
mongo = PyMongo(app)
CORS(app)
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
    user = db.find_one({'_id':ObjectId(id)})
    print(user)
    return jsonify({
        '_id' : str(ObjectId(user['_id'])),
        'name' : user['userName'],
        'email' : user['userEmail'],
        'password' : user['password']
    })

@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    db.delete_one({'_id':ObjectId(id)})
    return jsonify({'msg':'User deleted'})

@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    db.update_one({'_id': ObjectId(id)}, {'$set': {
        'userName': request.json['userName'],
        'userEmail': request.json['userEmail'],
        'password' : request.json['password']
    }})
    return jsonify({'msg': 'User updated.'})

if __name__ == '__main__':
    app.run(debug=True)