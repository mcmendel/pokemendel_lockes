import React, { useEffect, useRef, useState } from 'react';
import Pokemon from './Pokemon';
import { Pokemon as PokemonType } from '../api/lockeApi';
import './Party.css';

interface PartyProps {
  pokemons: Array<PokemonType | null>;
  onPokemonClick: (id: string) => void;
}

function Party({ pokemons, onPokemonClick }: PartyProps) {
  const slotRefs = useRef<(HTMLDivElement | null)[]>([]);
  const [slotHeights, setSlotHeights] = useState<number[]>([]);

  useEffect(() => {
    // Update heights after component mounts and whenever pokemons change
    const heights = slotRefs.current.map(slot => slot?.offsetHeight ?? 0);
    setSlotHeights(heights);
    heights.forEach((height, index) => {
      console.log(`Slot ${index + 1} height:`, height);
    });
  }, [pokemons]);

  return (
    <div className="party-container">
      <div className="party-header">Party</div>
      <div className="party-content">
        {pokemons.map((pokemon, index) => (
          <div 
            key={index} 
            className="party-slot"
            ref={el => slotRefs.current[index] = el}
          >
            {pokemon ? (
              <Pokemon 
                pokemon={pokemon}
                onClick={onPokemonClick}
                height={slotHeights[index] || 0}
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