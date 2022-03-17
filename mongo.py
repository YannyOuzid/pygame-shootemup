from pymongo import MongoClient

class Mongo():

    def post(self, post):
        client = MongoClient("mongodb+srv://admin:admin@cluster0.vfeta.mongodb.net/")
        db = client.pygame
        collection = db.score
        test = collection.insert_one({"score": post})

    def getHighscore(self):
        client = MongoClient("mongodb+srv://admin:admin@cluster0.vfeta.mongodb.net/")
        db = client.pygame
        collection = db.score
        highscore = collection.find({}).sort("score", -1).limit(1)
        return highscore[0]['score']

    def getTop(self):
        client = MongoClient("mongodb+srv://admin:admin@cluster0.vfeta.mongodb.net/")
        db = client.pygame
        collection = db.score
        highscore = collection.find({}).sort("score", -1).limit(10)
        return highscore
