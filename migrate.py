from db_service import artists
from csv import reader

import sys
import csv

csv.field_size_limit(sys.maxsize)

artists.drop()

with open("/media/sf_projects/lambda/hackathon-soundsky/lastfm-dataset-360K/usersha1-artmbid-artname-plays.tsv", "r") as f:
    read = reader(f, delimiter="\t")
    
    rows = []
    for row in read:
        _, user, artist, hits = row
        rows.append({"name": artist, "hits": hits, "user": user})


for sec in [rows[ix:ix+500] for ix in range(0, len(rows), 500)]:
    print(sec)
    try:
        artists.insert_many(sec)
    except Exception as e:
        print(e)
