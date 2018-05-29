#!/usr/bin/env python
# coding=utf-8

from flask import Flask, g
from RedisClient import RedisClient


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
def get_counts():
    conn = get_conn()
    return str(conn.count())

@app.route('/random')
def get_random():
    return get_conn().random()


if __name__ == '__main__':
    app.run()

