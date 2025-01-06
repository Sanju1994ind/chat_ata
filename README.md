# Chat ATA Project
Chat ATA is an online chat application built using Flask, Socket.IO, and MySQL.

## Features

- User authentication (player/coach)
- Real-time messaging using WebSockets
- Video call support via WebRTC

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Sanju1994ind/chat_ata.git
   
# Install dependencies: 
pip install -r requirements.txt

# Set up the database and run the Flask app:
flask db upgrade

flask run
