import React, { useState } from 'react';

function App() {
  const [cookies, setCookies] = useState<number>(0);

  const handleClick = () => {
    setCookies(cookies + 1); // 쿠키를 하나씩 증가
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>🍪 Cookie Clicker 🍪</h1>
      <h2>Cookies: {cookies}</h2>
      <button
        onClick={handleClick}
        style={{
          fontSize: '20px',
          padding: '10px 20px',
          cursor: 'pointer',
          backgroundColor: '#f7c500',
          border: 'none',
          borderRadius: '10px',
        }}
      >
        Click Me!
      </button>
    </div>
  );
}

export default App;
