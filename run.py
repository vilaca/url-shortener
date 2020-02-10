from flask import Flask, request, redirect
from flask_restful import Api, Resource
from validators import url

import service


class Redirects(Resource):
    def get(self, short):
        r = service.redirect(short)
        if not r:
            return {'status': 'NOK', 'message': 'Not found.'}, 404
        return redirect(r)


class Shorten(Resource):
    def post(self):
        new_url = request.form['v']
        if not new_url.startswith('http://') and not new_url.startswith('https://'):
            return reply_ko(400, 'Only available for http/https URLs.')
        if len(new_url) < 10:
            return reply_ko(400, 'Not a valid URL. Too short.')
        if not url(new_url):
            return reply_ko(400, 'Not a valid URL.')
        cached = service.exists(new_url)
        if cached:
            return reply_exists(cached)
        short = service.new(new_url)
        return reply_created(short)


def reply_created(short):
    return {'status': 'OK', 'short': short}, 201


def reply_exists(short):
    return {'status': 'OK', 'short': short}, 409


def reply_ko(status, message):
    return {'status': 'KO', 'message': message}, status


app = Flask(__name__)
api = Api(app)
api.add_resource(Shorten, '/')
api.add_resource(Redirects, '/<short>')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
