import React, { useState, useEffect } from 'react';
import { Box, Typography, Grid, TextField, CircularProgress } from '@mui/material';
import lockeApi from '../api/lockeApi';
import './SupportedPokemonList.css';

interface SupportedPokemonListProps {
  runId: string;
}

const SupportedPokemonList: React.FC<SupportedPokemonListProps> = ({ runId }) => {
  const [supportedPokemons, setSupportedPokemons] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    const fetchSupportedPokemons = async () => {
      setLoading(true);
      setError(null);
      try {
        const data = await lockeApi.getPotentialPokemons(runId);
        setSupportedPokemons(data);
      } catch (err) {
        console.error('Error fetching supported pokemons:', err);
        setError('Failed to load supported pokemons');
      } finally {
        setLoading(false);
      }
    };

    fetchSupportedPokemons();
  }, [runId]);

  // Filter Pokemon based on search term
  const filteredPokemons = supportedPokemons.filter(pokemon =>
    pokemon.toLowerCase().includes(searchTerm.toLowerCase())
  );

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return (
      <Typography sx={{ textAlign: 'center', mt: 2, color: '#d32f2f' }}>
        {error}
      </Typography>
    );
  }

  return (
    <div className="supported-pokemon-list">
      <Typography variant="h6" className="supported-pokemon-title">
        Supported Pokemon ({supportedPokemons.length})
      </Typography>
      <TextField
        fullWidth
        variant="outlined"
        placeholder="Search Pokemon..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        className="supported-pokemon-search"
        size="small"
      />
      
      <div className="supported-pokemon-grid">
        {filteredPokemons.map((pokemon, index) => (
          <div key={index} className="supported-pokemon-item">
            <img 
              src={lockeApi.getPokemonImageUrl(pokemon)}
              alt={pokemon}
              className="supported-pokemon-image"
              onError={(e) => {
                const target = e.target as HTMLImageElement;
                target.src = `https://placehold.co/60x60/1976d2/ffffff?text=${pokemon}`;
              }}
            />
            <Typography variant="caption" className="supported-pokemon-name">
              {pokemon}
            </Typography>
          </div>
        ))}
      </div>
      
      {filteredPokemons.length === 0 && supportedPokemons.length > 0 && (
        <Typography sx={{ textAlign: 'center', mt: 2, color: '#666' }}>
          No Pokemon found matching "{searchTerm}"
        </Typography>
      )}
    </div>
  );
};

export default SupportedPokemonList; 