import React from 'react';
import { Grid, Typography, Box } from '@mui/material';
import Pokemon from './Pokemon';
import { RunResponse } from '../api/lockeApi';
import './RunBox.css';

interface RunBoxProps {
  runData: RunResponse;
  onPokemonClick: (id: string) => void;
}

function RunBox({ runData, onPokemonClick }: RunBoxProps) {
  // Get alive Pokémon from the box
  const boxPokemons = runData.run.box
    .map(pokemonId => runData.pokemons[pokemonId])
    .filter(pokemon => pokemon && pokemon.status !== 'dead');

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
                <Box sx={{ 
                  display: 'flex', 
                  flexDirection: 'column', 
                  alignItems: 'center',
                  p: 1,
                  border: '1px solid #e0e0e0',
                  borderRadius: 2,
                  backgroundColor: '#f9f9f9',
                  minHeight: '120px'
                }}>
                  <Pokemon 
                    pokemon={pokemon}
                    onClick={onPokemonClick}
                    height={100}
                  />
                </Box>
              </Grid>
            ))}
          </Grid>
        )}
      </div>
    </div>
  );
}

export default RunBox; 