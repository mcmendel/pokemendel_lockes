import React, { useEffect, useState } from 'react';
import LockeRunsTable from './LockeRunsTable';
import lockeApi from '../api/lockeApi';
import { Run } from '../api/lockeApi';

const HomePage: React.FC = () => {
  const [runs, setRuns] = useState<Run[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchRuns = async () => {
      try {
        const data = await lockeApi.getRuns();
        setRuns(data);
      } catch (err) {
        setError('Failed to fetch runs');
        console.error('Error fetching runs:', err);
      }
    };

    fetchRuns();
  }, []);

  return (
    <div>
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
        {error ? (
          <div className="error-message">{error}</div>
        ) : (
          <LockeRunsTable runs={runs} />
        )}
      </main>
    </div>
  );
};

export default HomePage; 