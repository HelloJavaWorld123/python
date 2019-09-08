from aiohttp import web

import logging

logging.basicConfig(level=logging.DEBUG)


def index():
    logging.info("进入的请求")
    return web.Response(body='<h1>首页</h1>'.encode('UTF-8'), content_type='text/html')


def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    web.run_app(app, host="127.0.0.1", port=9000)
    logging.info("server start up on 9000")


init()
