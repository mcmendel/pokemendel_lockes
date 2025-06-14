import React from 'react';
import Pokemon from './Pokemon';
import { Pokemon as PokemonType } from '../api/lockeApi';
import './Party.css';

interface PartyProps {
  pokemons: Array<PokemonType | null>;
  onPokemonClick: (id: string) => void;
}

function Party({ pokemons, onPokemonClick }: PartyProps) {
  return (
    <div className="party-container">
      <div className="party-header">Party</div>
      <div className="party-content">
        {pokemons.map((pokemon, index) => (
          <div key={index} className="party-slot">
            {pokemon ? (
              <Pokemon 
                pokemon={pokemon}
                onClick={onPokemonClick}
              />
            ) : (
              <div className="empty-slot">Empty</div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Party; 