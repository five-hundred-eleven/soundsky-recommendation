import pymongo
import os

client = pymongo.MongoClient("ds259518.mlab.com", 59518, retryWrites=False)
db = client["soundsky-dev"]
db.authenticate(os.environ["SOUNDSKY_USER"], os.environ["SOUNDSKY_PASS"])


artists = db["artists"]
tracks = db["tracks"]
