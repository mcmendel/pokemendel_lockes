import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
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
      </header>
      <main>
        {/* Main content will go here */}
      </main>
    </div>
  );
}

export default App;
