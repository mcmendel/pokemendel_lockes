import React from 'react';
import { Box, Typography } from '@mui/material';
import { Pokemon as PokemonType } from '../api/lockeApi';
import lockeApi from '../api/lockeApi';
import './Starter.css';

interface StarterProps {
  starter: PokemonType | null;
  onPokemonClick?: (id: string) => void;
}

function Starter({ starter, onPokemonClick }: StarterProps) {
  if (!starter) {
    return (
      <div className="starter-container">
        <div className="starter-header">Starter</div>
        <div className="starter-content">
          <div className="no-starter">
            <Typography variant="body1" color="text.secondary">
              No starter selected
            </Typography>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="starter-container">
      <div className="starter-header">Starter</div>
      <div className="starter-content">
        <Box 
          className="starter-pokemon"
          onClick={() => onPokemonClick?.(starter.metadata.id)}
          sx={{ cursor: onPokemonClick ? 'pointer' : 'default' }}
        >
          <img 
            src={lockeApi.getPokemonImageUrl(starter.name)}
            alt={starter.name}
            className="starter-pokemon-image"
            onError={(e) => {
              const target = e.target as HTMLImageElement;
              target.src = `https://placehold.co/120x120/1976d2/ffffff?text=${starter.name}`;
            }}
          />
          <Typography variant="h6" className="starter-pokemon-name">
            {starter.name}
          </Typography>
          {starter.metadata.nickname && (
            <Typography variant="subtitle2" className="starter-pokemon-nickname">
              "{starter.metadata.nickname}"
            </Typography>
          )}
        </Box>
      </div>
    </div>
  );
}

export default Starter; 