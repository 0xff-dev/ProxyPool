#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from pp.RedisClient imprt RedisClient


__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis

@app.route('/')
def index():
    return '<h1> Proxy Pool System</h1>'


@app.route('/count')
def get_count():
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run()


