#class Config:
 #   SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost:3306/video_chat_db'
  #  SQLALCHEMY_TRACK_MODIFICATIONS = False

# class Config:
#    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/video_chat_db'
#    SQLALCHEMY_TRACK_MODIFICATIONS = False

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_hard_to_guess_string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MySQL Configuration (use environment variables for better security in production)
    DB_USERNAME = os.environ.get('DB_USERNAME', 'sanjeev')  # Set default as 'sanjeev' if not set
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'sanju@1994')  # Default password
    DB_HOST = os.environ.get('DB_HOST', 'localhost')  # Default to localhost
    DB_PORT = os.environ.get('DB_PORT', '3306')  # Default to port 3306 for MySQL
    DB_NAME = os.environ.get('DB_NAME', 'flask_chat_db')  # Default database name

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

