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
  const getChessRoleSymbol = (role: string) => {
    switch (role.toLowerCase()) {
      case 'king':
        return '♔';
      case 'queen':
        return '♕';
      case 'rook':
        return '♖';
      case 'bishop':
        return '♗';
      case 'knight':
        return '♘';
      case 'pawn':
        return '♙';
      default:
        return null;
    }
  };
  const getGenderSymbol = (gender: string) => {
    switch (gender) {
      case 'Male':
        return '♂';
      case 'Female':
        return '♀';
      case 'Genderless':
        return '⚪';
      default:
        return null;
    }
  };

  const genderSymbol = pokemon.metadata.gender ? getGenderSymbol(pokemon.metadata.gender) : null;
  const chessRoleSymbol = pokemon.metadata.chesslocke_role ? getChessRoleSymbol(pokemon.metadata.chesslocke_role) : null;

  return (
    <Box sx={{ 
      height: `${height}px`, 
      display: 'flex', 
      flexDirection: 'column', 
      alignItems: 'center',
      position: 'relative'
    }}>
      {genderSymbol && (
        <Box
          sx={{
            position: 'absolute',
            top: '4px',
            left: '4px',
            zIndex: 1,
            width: '16px',
            height: '16px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '12px',
            fontWeight: 'bold',
            color: pokemon.metadata.gender === 'Male' ? '#4A90E2' : 
                   pokemon.metadata.gender === 'Female' ? '#E91E63' : '#9E9E9E',
            textShadow: '1px 1px 1px rgba(0,0,0,0.5)'
          }}
        >
          {genderSymbol}
        </Box>
      )}
      {chessRoleSymbol && (
        <Box
          sx={{
            position: 'absolute',
            top: '4px',
            right: '4px',
            zIndex: 1,
            width: '20px',
            height: '20px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '14px',
            fontWeight: 'bold',
            color: '#FFD54F',
            textShadow: '1px 1px 1px rgba(0,0,0,0.6)'
          }}
          title={`Chess role: ${pokemon.metadata.chesslocke_role}`}
        >
          {chessRoleSymbol}
        </Box>
      )}
      <Button 
        onClick={() => onClick(pokemon.metadata.id)}
        disabled={!isEnabled}
        sx={{ height: '70%', width: 'auto' }}
      >
        <img 
          src={lockeApi.getPokemonImageUrl(pokemon.name)}
          alt={pokemon.name}
          style={{ 
            maxHeight: '100%',
            filter: pokemon.status === 'dead' || pokemon.status === 'Dead' ? 'grayscale(100%) brightness(0.7)' : 'none',
            opacity: pokemon.status === 'dead' || pokemon.status === 'Dead' ? 0.6 : 1
          }}
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