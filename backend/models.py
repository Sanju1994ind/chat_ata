from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# User model for player/coach
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'player' or 'coach'
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)  # Adding index for performance

    # Cascade delete: If a user is deleted, their messages are also deleted
    messages = db.relationship('Message', backref='user', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User {self.username}>"

# Message model for chat history
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False, index=True)  # Add index for better performance
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)  # Index for faster timestamp queries

    def __repr__(self):
        return f"<Message {self.message[:20]}>"
