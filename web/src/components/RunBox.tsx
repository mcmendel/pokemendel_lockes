import React from 'react';
import { Grid, Typography, Box, Button } from '@mui/material';
import Pokemon from './Pokemon';
import { RunResponse } from '../api/lockeApi';
import lockeApi from '../api/lockeApi';
import './RunBox.css';

interface RunBoxProps {
  runData: RunResponse;
  onPokemonClick: (id: string) => void;
}

function RunBox({ runData, onPokemonClick }: RunBoxProps) {
  // Get alive Pokémon from the box
  const boxPokemons = runData.run.box
    .map(pokemonId => runData.pokemons[pokemonId])
    .filter(pokemon => pokemon && pokemon.status !== 'Dead');

  return (
    <div className="run-box-container">
      <div className="run-box-header">Box</div>
      <div className="run-box-content">
        {boxPokemons.length === 0 ? (
          <Box sx={{ 
            display: 'flex', 
            justifyContent: 'center', 
            alignItems: 'center', 
            height: '200px',
            color: '#666'
          }}>
            <Typography variant="body1">No Pokémon in box</Typography>
          </Box>
        ) : (
          <Grid container spacing={2}>
            {boxPokemons.map((pokemon) => (
              <Grid item xs={6} sm={4} md={3} lg={2} key={pokemon.metadata.id}>
                <Button
                  onClick={() => onPokemonClick(pokemon.metadata.id)}
                  sx={{ 
                    display: 'flex', 
                    flexDirection: 'column', 
                    alignItems: 'center',
                    p: 1,
                    border: '1px solid #e0e0e0',
                    borderRadius: 2,
                    backgroundColor: '#f9f9f9',
                    minHeight: '120px',
                    width: '100%',
                    textTransform: 'none',
                    '&:hover': {
                      backgroundColor: '#e3f2fd',
                      borderColor: '#1976d2'
                    }
                  }}
                >
                  <img 
                    src={lockeApi.getPokemonImageUrl(pokemon.name)}
                    alt={pokemon.name}
                    style={{ 
                      width: '80px', 
                      height: '80px', 
                      objectFit: 'contain',
                      marginBottom: '8px'
                    }}
                    onError={(e) => {
                      const target = e.target as HTMLImageElement;
                      target.src = `https://placehold.co/80x80/1976d2/ffffff?text=${pokemon.name}`;
                    }}
                  />
                  <Typography variant="body2" sx={{ textAlign: 'center', fontWeight: 500 }}>
                    {pokemon.name}
                  </Typography>
                  {pokemon.metadata.nickname && (
                    <Typography variant="caption" sx={{ textAlign: 'center', color: '#666' }}>
                      "{pokemon.metadata.nickname}"
                    </Typography>
                  )}
                </Button>
              </Grid>
            ))}
          </Grid>
        )}
      </div>
    </div>
  );
}

export default RunBox; 