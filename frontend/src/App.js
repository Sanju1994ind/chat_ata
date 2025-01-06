import React, { useState } from 'react';
import VideoChat from './components/VideoChat';
import Chat from './components/Chat';

function App() {
  const [userId, setUserId] = useState(null);

  const createUser = (role) => {
    const username = prompt("Enter username:");
    fetch('http://localhost:5000/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, role })
    })
      .then(res => res.json())
      .then(data => setUserId(data.id));
  };

  return (
    <div className="container">
      <h1>One-to-One Video & Chat App</h1>
      {!userId ? (
        <div>
          <button className="btn btn-primary" onClick={() => createUser('player')}>Join as Player</button>
          <button className="btn btn-secondary" onClick={() => createUser('coach')}>Join as Coach</button>
        </div>
      ) : (
        <>
          <VideoChat />
          <Chat userId={userId} />
        </>
      )}
    </div>
  );
}

export default App;
