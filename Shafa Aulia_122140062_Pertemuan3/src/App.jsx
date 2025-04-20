import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home/Home';
import Stats from './pages/Stats/Stats';

export default function App() {
  return (
    <Router>
      <nav className="navbar">
        <Link to="/">Home</Link> | <Link to="/stats">Stats</Link>
      </nav>
      <main className="app-container">
        <Routes>
          <Route path="/"      element={<Home />} />
          <Route path="/stats" element={<Stats />} />
        </Routes>
      </main>
    </Router>
  );
}
