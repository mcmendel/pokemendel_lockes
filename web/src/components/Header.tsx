import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Header.css';

const Header: React.FC = () => {
  const navigate = useNavigate();

  return (
    <header className="App-header">
      <div className="header-content">
        <img 
          src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png" 
          alt="Gengar" 
          className="pokemon-logo"
        />
        <h1>LockeManager</h1>
        <img 
          src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png" 
          alt="Charizard" 
          className="pokemon-logo"
        />
      </div>
      <button 
        className="home-button"
        onClick={() => navigate('/locke_manager')}
        title="Go to Home"
      >
        🏠
      </button>
    </header>
  );
};

export default Header; 