from flask import Flask, request, jsonify
from main import searchGDrive,search
from similarity_CV import similarity
from flask_cors import CORS
import json
import os


app = Flask(__name__)
CORS(app)  # Abilita CORS per tutte le rotte

@app.route('/api/search', methods=['POST'])
def searchREST():
    #return jsonify(message='Hello, World!')
    #input = ['java', 'welfare']

    print("1")
    print("listdir before")
    print(os.listdir())
    print("listdir after")

    request_data = request.get_json()

    if not request_data or 'terms' not in request_data:
        return jsonify(error='Invalid input'), 400
    
    terms_array = request_data['terms']

    res = search(terms_array)
    #res = searchGDrive(terms_array)
    #return jsonify(message='Hello, World!')
    return jsonify(message=res)

@app.route('/api/similarity', methods=['GET'])
def similarityREST():
    #return jsonify(message='Hello, World!')
    #input = ['java', 'welfare']

    print("1 similarity")

    res = similarity()
    #res = searchGDrive(terms_array)
    #return jsonify(message='Hello, World!')
    return jsonify(message=res)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
