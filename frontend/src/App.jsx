import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home/Home';

// Placeholder components for other routes so the app doesn't crash
const Placeholder = ({ name }) => (
  <div style={{ display: 'flex', height: '100vh', alignItems: 'center', justifyContent: 'center' }}>
    <h1>{name} Page (Coming Soon)</h1>
  </div>
);

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/shop" element={<Placeholder name="Shop" />} />
        <Route path="/product/:id" element={<Placeholder name="Product Details" />} />
        <Route path="/cart" element={<Placeholder name="Cart" />} />
        <Route path="/profile" element={<Placeholder name="Profile" />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
