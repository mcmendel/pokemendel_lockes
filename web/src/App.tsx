import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import HomePage from './components/HomePage';
import NewRunPage from './components/NewRunPage';
import Layout from './components/Layout';
import './App.css';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/locke_manager" element={<HomePage />} />
          <Route path="/locke_manager/new" element={<NewRunPage />} />
          <Route path="*" element={<Navigate to="/locke_manager" replace />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
