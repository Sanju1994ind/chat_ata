import eventlet
eventlet.monkey_patch()  # Ensure eventlet patches are applied before any other imports

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config
from models import db, User, Message

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize CORS, SQLAlchemy, and SocketIO
CORS(app, origins=["http://localhost:3000"])  # restrict CORS to frontend URL
db.init_app(app)
socketio = SocketIO(app, cors_allowed_origins='*', logger=True, engineio_logger=True)

# Define routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test')
def test():
    return 'Hello, Flask is working!'

# Create a new user (either player or coach)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    role = data.get('role')

    if not username or not role:
        return jsonify({'error': 'Missing username or role'}), 400

    user = User(username=username, role=role)
    db.session.add(user)
    db.session.commit()

    return jsonify({'id': user.id, 'username': user.username, 'role': user.role})

# Retrieve chat messages
@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    messages_data = [{'id': msg.id, 'user': msg.user.username, 'message': msg.message, 'timestamp': msg.timestamp} for msg in messages]
    return jsonify(messages_data)

# WebSocket event for sending chat messages
@socketio.on('message')
def handle_message(data):
    user_id = data.get('user_id')
    text = data.get('message')

    if user_id and text:
        msg = Message(user_id=user_id, message=text)
        db.session.add(msg)
        db.session.commit()

        # Emit message to all connected clients
        emit('message', {'user': msg.user.username, 'message': msg.message}, broadcast=True)

# WebRTC signaling events
@socketio.on('offer')
def handle_offer(data):
    print("Received offer:", data)  # Debugging log
    emit('offer', data, broadcast=True)

@socketio.on('answer')
def handle_answer(data):
    print("Received answer:", data)  # Debugging log
    emit('answer', data, broadcast=True)

@socketio.on('candidate')
def handle_candidate(data):
    print("Received candidate:", data)  # Debugging log
    emit('candidate', data, broadcast=True)

# Run the app
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
