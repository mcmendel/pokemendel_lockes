import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import HomePage from './components/HomePage';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/locke_manager" element={<HomePage />} />
        <Route path="*" element={<Navigate to="/locke_manager" replace />} />
      </Routes>
    </Router>
  );
}

export default App;
