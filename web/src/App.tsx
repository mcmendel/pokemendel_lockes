import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import './App.css';
import HomePage from './components/HomePage';

// Test data
const testRuns = [
  {
    "created_at": "Tue, 10 Sep 2024 10:57:19 GMT",
    "finished": false,
    "game": "Blue",
    "id": "78c447ef0eb44b049be1f69ad20e82f4",
    "locke": "WrapLocke",
    "name": "wraplocke",
    "num_badges": 12,
    "num_deaths": 4,
    "num_pokemons": 18,
    "num_restarts": 1,
    "randomized": false,
    "starter": "Ivysaur"
  },
  {
    "created_at": "Tue, 05 Nov 2024 23:58:22 GMT",
    "finished": true,
    "game": "Blue",
    "id": "7255c7aa5ea7419894d804b2afbff47e",
    "locke": "ColorLocke",
    "name": "color_green",
    "num_badges": 12,
    "num_deaths": 1,
    "num_pokemons": 7,
    "num_restarts": 1,
    "randomized": false,
    "starter": "Venusaur"
  },
  {
    "created_at": "Tue, 10 Sep 2024 10:57:19 GMT",
    "finished": false,
    "game": "Blue",
    "id": "78c447ef0eb44b049be1f69ad20e82f4",
    "locke": "WrapLocke",
    "name": "wraplocke",
    "num_badges": 12,
    "num_deaths": 4,
    "num_pokemons": 18,
    "num_restarts": 1,
    "randomized": false,
    "starter": "Ivysaur"
  },
  {
    "created_at": "Tue, 05 Nov 2024 23:58:22 GMT",
    "finished": true,
    "game": "Blue",
    "id": "7255c7aa5ea7419894d804b2afbff47e",
    "locke": "ColorLocke",
    "name": "color_green",
    "num_badges": 12,
    "num_deaths": 1,
    "num_pokemons": 7,
    "num_restarts": 1,
    "randomized": false,
    "starter": "Venusaur"
  },{
    "created_at": "Tue, 10 Sep 2024 10:57:19 GMT",
    "finished": false,
    "game": "Blue",
    "id": "78c447ef0eb44b049be1f69ad20e82f4",
    "locke": "WrapLocke",
    "name": "wraplocke",
    "num_badges": 12,
    "num_deaths": 4,
    "num_pokemons": 18,
    "num_restarts": 1,
    "randomized": false,
    "starter": "Ivysaur"
  },
  {
    "created_at": "Tue, 05 Nov 2024 23:58:22 GMT",
    "finished": true,
    "game": "Blue",
    "id": "7255c7aa5ea7419894d804b2afbff47e",
    "locke": "ColorLocke",
    "name": "color_green",
    "num_badges": 12,
    "num_deaths": 1,
    "num_pokemons": 7,
    "num_restarts": 1,
    "randomized": false,
    "starter": "Venusaur"
  },
];

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Navigate to="/locke_manager" replace />} />
          <Route path="/locke_manager" element={<HomePage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
