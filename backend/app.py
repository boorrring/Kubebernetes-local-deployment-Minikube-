from flask import Flask, render_template, jsonify
from connections import collection # Importing the collection from connections.py
import os

app = Flask(__name__)

PORT = os.environ.get('PORT', 8000)
@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the backend'})




@app.route('/api/add/<name>')
def add_name(name):
    collection.insert_one({'name': name})
    return jsonify({'message': f'Name {name} added successfully'})


@app.route('/api/get')
def api():   
    names = collection.find()
    result = []
    for name in names:
        result.append(name['name'])
    result = {'Names': result}

    return jsonify(result)


@app.route('/api/delete/<name>')
def delete_name(name):
    collection.delete_one({'name': name})
    return jsonify({'message': f'Name {name} deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True,port=PORT, host='0.0.0.0')
