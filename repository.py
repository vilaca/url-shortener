import pymongo
import os


def get(short):
    r = coll.find_one({'key': short})
    if r:
        return r['url']
    return None


def exists(url):
    r = coll.find_one({'url': url})
    if r:
        return r['key']
    return None


def create(key, url):
    coll.insert_one({'key': key, 'url': url})


client = pymongo.MongoClient(os.getenv('URL_SHORTENER_DB', 'mongodb://localhost:27017/'))
db = client["short-urls"]
coll = db["short"]
