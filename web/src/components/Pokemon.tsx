import React from 'react';
import { Pokemon as PokemonType } from '../api/lockeApi';
import lockeApi from '../api/lockeApi';
import './Pokemon.css';

interface PokemonMetadata {
  id: string;
}

interface PokemonProps {
  pokemon: PokemonType & { metadata: PokemonMetadata };
  onClick: (id: string) => void;
  height: number;
}

function Pokemon({ pokemon, onClick, height }: PokemonProps) {
  return (
    <button 
      className="pokemon-button"
      onClick={() => onClick(pokemon.metadata.id)}
      style={{ height: `${height}px` }}
    >
      <img
        src={lockeApi.getPokemonImageUrl(pokemon.name)}
        alt={pokemon.name}
        className="pokemon-image"
        onError={(e) => {
          const target = e.target as HTMLImageElement;
          target.src = `https://placehold.co/120x120/1976d2/ffffff?text=${pokemon.name}`;
        }}
      />
    </button>
  );
}

export default Pokemon; 