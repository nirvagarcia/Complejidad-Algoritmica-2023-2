import os
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from BackEndLogica import *

print("Encendiendo backend...")
app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route('/api/v1/compare', methods=['GET'])
def compare():
    try:
        id1 = request.args.get('id1')
        id2 = request.args.get('id2')
        if id1 is None or id2 is None:
            abort(400)
        response = compute_relation(id1, id2)
        if response == errors.InternalServerError or response is None:
            abort(500)
        if response == errors.NotFound:
            abort(404)
        if response == errors.BadRequest:
            abort(400)
        return response
    except:
        abort(500)

@app.route('/api/v1/getAnimeList', methods=['GET'])
def get_names():
    return animeNames

@app.route('/api/v1/getAnimeImageList', methods=['GET'])
def get_pictures():
    return animePictures

@app.route('/api/v1/getAnimeGenres', methods=['GET'])
def get_anime_genres():
    return list(animeGenres)

@app.route('/api/v1/getAnimeImage', methods=['GET'])
def get_anime_image():
    try:
        id = int(request.args.get('id'))
        if id is None: abort(400)
        if(0 <= id and id < len(animePictures)):
            return animePictures[id]
        else: abort(404)
    except: abort(500)


@app.route('/api/v1/getAnimeData', methods=['GET'])
def get_anime_data():
    try:
        id = int(request.args.get('id'))
        if (0 <= id and id < len(animeData)):
            return animeData[id]
        else: abort(404)
    except: abort(500)

@app.route('/api/v1/getFullAnimeData', methods=['GET'])
def get_full_anime_data():
    response = jsonify(animeData)
    response.headers.add('Content-Type', 'application/json')
    return response


print("Backend operativo")
app.run(debug=True, port=5000)