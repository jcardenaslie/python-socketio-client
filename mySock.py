import socketio
import time

# standard Python
sio = socketio.Client()

start_timer = None

def send_ping():
    global start_timer
    start_timer = time.time()
    sio.emit('ping_from_client')

@sio.event
def message(data):
    print('I received a message!')

@sio.on('my message')
def on_message(data):
    print('I received a message!')

@sio.on('my response')
def on_response(data):
    print(data)

@sio.on('connect')
def on_connect(data):
    print('I received a message!')

@sio.event
def connect():
    sio.emit('my event', {'Joaquin': 'bar'})
    print("I'm connected!")

@sio.event
def disconnect():
    global sio
    sio.disconnect()
    print("I'm disconnected!")

def bg_task():
    while True:
        message = input('Send message: ')
        sio.emit('my event', {'Joaquin': message})
        print(message)

if __name__ == '__main__':
    sio.connect('http://localhost:5000')
    sio.start_background_task(bg_task)
    # sio.wait()