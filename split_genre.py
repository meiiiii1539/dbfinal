from pymongo import MongoClient
client = MongoClient("mongodb://dbadmin:peter1234@140.117.71.182:27017/?authMechanism=DEFAULT")
db = client["db_finalproject"]
col = db["anime"]
for x in col.find():
    print(x['anime_id'])
    if 'genre' in x:
        categoty = x['genre'].split(', ')
        col.update_one({
            '_id': x['_id']
        },{
            '$set' : {
                "genre" : categoty
            }
        })
client.close()