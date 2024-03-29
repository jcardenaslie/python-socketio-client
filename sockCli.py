# import socketio

# sio = socketio.Client()

# @sio.event
# def connect():
#     print('connection established')

# @sio.event
# def my_message(data):
#     print('message received with ', data)
#     sio.emit('my response', {'response': 'my response'})

# @sio.event
# def disconnect():
#     print('disconnected from server')

# sio.connect('http://localhost:5000')
# sio.wait()

from aiohttp import web

import socketio

sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)


async def index(request):
    with open('latency.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.event
async def ping_from_client(sid):
    await sio.emit('pong_from_server', room=sid)


app.router.add_static('/static', 'static')
app.router.add_get('/', index)


if __name__ == '__main__':
    web.run_app(app)