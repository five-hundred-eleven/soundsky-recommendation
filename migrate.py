from db_service import artists
from csv import reader


with open("/media/sf_projects/lambda/hackathon-soundsky/lastfm-dataset-360K/usersha1-artmbid-artname-plays.tsv", "r") as f:
    read = reader(f, delimiter="\t")
    ix = 0
    for row in read:
        _, _, artist, hits = row
        artists.insert_one({"name": artist, "hits": hits})
