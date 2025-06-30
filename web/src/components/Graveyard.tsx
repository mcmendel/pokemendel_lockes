import React from 'react';
import { Grid, Typography, Box, Button } from '@mui/material';
import { RunResponse } from '../api/lockeApi';
import lockeApi from '../api/lockeApi';
import './Graveyard.css';

interface GraveyardProps {
  runData: RunResponse;
  onPokemonClick: (id: string) => void;
}

function Graveyard({ runData, onPokemonClick }: GraveyardProps) {
  // Get dead Pokémon from both party and box
  const allPokemonIds = [...runData.run.party, ...runData.run.box];
  const deadPokemons = allPokemonIds
    .map(pokemonId => runData.pokemons[pokemonId])
    .filter(pokemon => pokemon && pokemon.status === 'dead');

  return (
    <div className="graveyard-container">
      <div className="graveyard-header">Graveyard</div>
      <div className="graveyard-content">
        {deadPokemons.length === 0 ? (
          <Box sx={{ 
            display: 'flex', 
            justifyContent: 'center', 
            alignItems: 'center', 
            height: '200px',
            color: '#666'
          }}>
            <Typography variant="body1">No fallen Pokémon</Typography>
          </Box>
        ) : (
          <Grid container spacing={2}>
            {deadPokemons.map((pokemon) => (
              <Grid item xs={6} sm={4} md={3} lg={2} key={pokemon.metadata.id}>
                <Button
                  onClick={() => onPokemonClick(pokemon.metadata.id)}
                  sx={{ 
                    display: 'flex', 
                    flexDirection: 'column', 
                    alignItems: 'center',
                    p: 1,
                    border: '1px solid #d32f2f',
                    borderRadius: 2,
                    backgroundColor: '#ffebee',
                    minHeight: '120px',
                    width: '100%',
                    textTransform: 'none',
                    '&:hover': {
                      backgroundColor: '#ffcdd2',
                      borderColor: '#b71c1c'
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
                      marginBottom: '8px',
                      filter: 'grayscale(100%)'
                    }}
                    onError={(e) => {
                      const target = e.target as HTMLImageElement;
                      target.src = `https://placehold.co/80x80/d32f2f/ffffff?text=${pokemon.name}`;
                    }}
                  />
                  <Typography variant="body2" sx={{ textAlign: 'center', fontWeight: 500, color: '#d32f2f' }}>
                    {pokemon.name}
                  </Typography>
                  {pokemon.metadata.nickname && (
                    <Typography variant="caption" sx={{ textAlign: 'center', color: '#666' }}>
                      "{pokemon.metadata.nickname}"
                    </Typography>
                  )}
                  <Typography variant="caption" sx={{ textAlign: 'center', color: '#d32f2f', fontWeight: 'bold' }}>
                    R.I.P.
                  </Typography>
                </Button>
              </Grid>
            ))}
          </Grid>
        )}
      </div>
    </div>
  );
}

export default Graveyard; 