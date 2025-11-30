import React from 'react';
import { Box, Button, Typography } from '@mui/material';
import { ArrowUpward, ArrowDownward, Remove } from '@mui/icons-material';
import { Pokemon as PokemonType, PokemonMetadata as ApiPokemonMetadata } from '../api/lockeApi';
import lockeApi from '../api/lockeApi';

interface PokemonProps {
  pokemon: PokemonType;
  onClick: (id: string) => void;
  height?: number;
  isEnabled?: boolean;
}

// Nature stat mapping: [increased stat, decreased stat]
// Neutral natures return [null, null]
const getNatureStats = (nature: string | null | undefined): { increased: string | null; decreased: string | null } => {
  if (!nature) return { increased: null, decreased: null };
  
  const natureLower = nature.toLowerCase();
  
  // Neutral natures (no stat changes)
  const neutralNatures = ['hardy', 'docile', 'serious', 'bashful', 'quirky'];
  if (neutralNatures.includes(natureLower)) {
    return { increased: null, decreased: null };
  }
  
  // Stat abbreviations
  const stats: Record<string, string> = {
    'hp': 'HP',
    'atk': 'Atk',
    'def': 'Def',
    'spa': 'SpA',
    'spd': 'SpD',
    'spe': 'Spe'
  };
  
  // Nature to stat mapping
  const natureMap: Record<string, { increased: string; decreased: string }> = {
    'lonely': { increased: 'atk', decreased: 'def' },
    'brave': { increased: 'atk', decreased: 'spe' },
    'adamant': { increased: 'atk', decreased: 'spa' },
    'naughty': { increased: 'atk', decreased: 'spd' },
    'bold': { increased: 'def', decreased: 'atk' },
    'relaxed': { increased: 'def', decreased: 'spe' },
    'impish': { increased: 'def', decreased: 'spa' },
    'lax': { increased: 'def', decreased: 'spd' },
    'timid': { increased: 'spe', decreased: 'atk' },
    'hasty': { increased: 'spe', decreased: 'def' },
    'jolly': { increased: 'spe', decreased: 'spa' },
    'naive': { increased: 'spe', decreased: 'spd' },
    'modest': { increased: 'spa', decreased: 'atk' },
    'mild': { increased: 'spa', decreased: 'def' },
    'quiet': { increased: 'spa', decreased: 'spe' },
    'rash': { increased: 'spa', decreased: 'spd' },
    'calm': { increased: 'spd', decreased: 'atk' },
    'gentle': { increased: 'spd', decreased: 'def' },
    'sassy': { increased: 'spd', decreased: 'spe' },
    'careful': { increased: 'spd', decreased: 'spa' }
  };
  
  const natureEffect = natureMap[natureLower];
  if (!natureEffect) {
    return { increased: null, decreased: null };
  }
  
  return {
    increased: stats[natureEffect.increased] || null,
    decreased: stats[natureEffect.decreased] || null
  };
};

function Pokemon({ pokemon, onClick, height, isEnabled = true }: PokemonProps) {
  const hasNature = !!pokemon.nature;
  // Reserve extra space for nature display if present
  const natureDisplayHeight = hasNature ? 20 : 0;
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
  const natureStats = getNatureStats(pokemon.nature);

  return (
    <Box sx={{ 
      height: height && height > 0 ? `${height}px` : 'auto',
      display: 'flex', 
      flexDirection: 'column', 
      alignItems: 'center',
      position: 'relative',
      width: '100%',
      justifyContent: 'flex-start',
      boxSizing: 'border-box'
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
        sx={{ 
          flex: '0 0 auto',
          height: height && height > 0 
            ? `${Math.max(height - (pokemon.metadata.nickname ? 30 : 0) - natureDisplayHeight - 8, 50)}px`
            : 'auto',
          width: 'auto',
          minHeight: '50px',
          padding: '4px'
        }}
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
        <Typography variant="subtitle1" sx={{ marginTop: '4px', fontSize: '0.8rem', flexShrink: 0 }}>
          {pokemon.metadata.nickname}
        </Typography>
      )}
      {pokemon.nature && (
        <Box sx={{ 
          display: 'flex', 
          alignItems: 'center', 
          justifyContent: 'center',
          gap: '4px',
          marginTop: '2px',
          fontSize: '0.7rem',
          flexShrink: 0,
          height: '18px'
        }}>
          {natureStats.increased ? (
            <Box sx={{ display: 'flex', alignItems: 'center', color: '#2196F3' }}>
              <ArrowUpward sx={{ fontSize: '0.9rem', marginRight: '2px' }} />
              <Typography variant="caption" sx={{ color: '#2196F3', fontWeight: 'bold' }}>
                {natureStats.increased}
              </Typography>
            </Box>
          ) : null}
          {natureStats.decreased ? (
            <Box sx={{ display: 'flex', alignItems: 'center', color: '#F44336' }}>
              <ArrowDownward sx={{ fontSize: '0.9rem', marginRight: '2px' }} />
              <Typography variant="caption" sx={{ color: '#F44336', fontWeight: 'bold' }}>
                {natureStats.decreased}
              </Typography>
            </Box>
          ) : null}
          {!natureStats.increased && !natureStats.decreased && (
            <Box sx={{ display: 'flex', alignItems: 'center', color: '#9E9E9E' }}>
              <Remove sx={{ fontSize: '0.9rem' }} />
            </Box>
          )}
        </Box>
      )}
    </Box>
  );
}

export default Pokemon; 