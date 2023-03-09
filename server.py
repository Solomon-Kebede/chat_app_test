#!/usr/bin/env python3

import aiohttp
from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
	return web.Response(text="Hello, world!")

@routes.get('/ws')
async def websocket_handler(request):
	ws = web.WebSocketResponse()
	await ws.prepare(request)

	async for msg in ws:
		if msg.type == aiohttp.WSMsgType.TEXT:
			print(msg.data)
			if msg.data == 'close':
				await ws.close()
			else:
				await ws.send_str(f'Your message: {msg.data}')
		elif msg.type == aiohttp.WSMsgType.ERROR:
			print(f'ws connection closed with exception: {ws.exception()}')

	print('websocket connection closed')

	return ws

app = web.Application()
app.add_routes(routes)
web.run_app(app)