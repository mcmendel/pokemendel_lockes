import React from 'react';
import { Box, Button, Typography } from '@mui/material';
import { Pokemon as PokemonType, PokemonMetadata as ApiPokemonMetadata } from '../api/lockeApi';
import lockeApi from '../api/lockeApi';

interface PokemonProps {
  pokemon: PokemonType;
  onClick: (id: string) => void;
  height: number;
  isEnabled?: boolean;
}

function Pokemon({ pokemon, onClick, height, isEnabled = true }: PokemonProps) {
  return (
    <Box sx={{ 
      height: `${height}px`, 
      display: 'flex', 
      flexDirection: 'column', 
      alignItems: 'center'
    }}>
      <Button 
        onClick={() => onClick(pokemon.metadata.id)}
        disabled={!isEnabled}
        sx={{ height: '70%', width: 'auto' }}
      >
        <img 
          src={lockeApi.getPokemonImageUrl(pokemon.name)}
          alt={pokemon.name}
          style={{ maxHeight: '100%' }}
          onError={(e) => {
            const target = e.target as HTMLImageElement;
            target.src = `https://placehold.co/120x120/1976d2/ffffff?text=${pokemon.name}`;
          }}
        />
      </Button>
      {pokemon.metadata.nickname && (
        <Typography variant="subtitle1" sx={{ marginTop: '8px', fontSize: '0.8rem' }}>
          {pokemon.metadata.nickname}
        </Typography>
      )}
    </Box>
  );
}

export default Pokemon; 