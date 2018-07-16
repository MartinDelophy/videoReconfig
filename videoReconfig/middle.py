#coding:utf-8
from flask import Flask
from flask import render_template
from flask_socketio import SocketIO,emit
import video

#from video import cap
app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def show():
    return render_template('index.html')

#该方法可用于socket通信
@socketio.on('my event')
def handle_my_custom_event(json):
	
	res=video.readImage(json["data"])
	emit('my response', {'res':res}) 






if __name__ == '__main__':
    
	app.run()