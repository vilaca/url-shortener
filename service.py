from random import randrange

import repository


def redirect(key):
    return repository.get(key)


def exists(new_url):
    return repository.exists(new_url)


def new(new_url):
    short = str()
    while True:
        for x in range(6):
            short += base64[randrange(2 ** 6)]
        if not repository.get(short):
            break
        short = str()
    repository.create(short, new_url)
    return short


base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'

