from flask import Flask, request, jsonify
from db_service import tracks
import random

app = Flask(__name__)

@app.route("/music")
def index():

    artist = request.args.get("artist").lower()
    res = tracks.find({"artist": artist})

    return jsonify([x for x in res])
    



if __name__ == "__main__":
    app.run()
