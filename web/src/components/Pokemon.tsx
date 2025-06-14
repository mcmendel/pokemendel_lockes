import React from 'react';
import { Pokemon as PokemonType } from '../api/lockeApi';
import './Pokemon.css';

interface PokemonMetadata {
  id: string;
}

interface PokemonProps {
  pokemon: PokemonType & { metadata: PokemonMetadata };
  onClick: (id: string) => void;
}

function Pokemon({ pokemon, onClick }: PokemonProps) {
  return (
    <button 
      className="pokemon-button"
      onClick={() => onClick(pokemon.metadata.id)}
    >
      <span className="pokemon-name">{pokemon.name}</span>
      <span className="pokemon-id">ID: {pokemon.metadata.id}</span>
    </button>
  );
}

export default Pokemon; 