import sys
import logging

from flask import Flask, Response, request

import db

app = Flask(__name__)
app.config.from_object('config')


@app.route("/ping")
def ping():
    return Response('pong', mimetype='text/plain')


@app.route("/", methods=['POST'])
def stream():
    data = request.get_json()
    query = data.get('query')
    params = data.get('params')
    generator = db.gen(query, params)
    return Response(generator, mimetype='application/json')


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    app.run(host='0.0.0.0', port=80)
