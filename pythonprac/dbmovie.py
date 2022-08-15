from pymongo import MongoClient
client = MongoClient('@@@@') #mongodb 주소
db = client.dbsparta

db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})


