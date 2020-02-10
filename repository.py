import pymongo

client = pymongo.MongoClient("mongodb://192.168.99.100:27017/")
db = client["short-urls"]
col = db["short"]


def get(short):
    r = col.find_one({'key': short})
    if r:
        return r['url']
    return None


def exists(url):
    r = col.find_one({'url': url})
    if r:
        return r['key']
    return None


def create(key, url):
    col.insert_one({'key': key, 'url': url})
