from pymongo import MongoClient
import datetime

tq_id = "treequest-0_0_0"# UID for treequest models 
conn = MongoClient()
# Set the main DB to our version
db = conn[tq_id]
users = db.users

class User(object):
    def __init__(self, username):
        self.username = username
        self.user = {
                "username": self.username,
                "created": datetime.datetime.utcnow()
                }

    def get(self):
        ret = users.find_one({"username": self.username})
        if ret == "":
            return False
        return ret

    def create(self):
        ret = users.insert(self.user)
        return "created: %s" % ret

    def delete(self):
        users.remove({"username": self.username})
        return True

