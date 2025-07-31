import React, { useEffect, useRef, useState } from 'react';
import Pokemon from './Pokemon';
import { Pokemon as PokemonType } from '../api/lockeApi';
import './WedLockeParty.css';

interface WedLockePartyProps {
  pokemons: Array<PokemonType | null>;
  onPokemonClick: (id: string) => void;
}

interface PairSlot {
  pokemon1: PokemonType | null;
  pokemon2: PokemonType | null;
}

function WedLockeParty({ pokemons, onPokemonClick }: WedLockePartyProps) {
  const slotRefs = useRef<(HTMLDivElement | null)[]>([]);
  const [slotHeights, setSlotHeights] = useState<number[]>([]);

  // Organize pokemons into pairs based on paired metadata
  const organizeIntoPairs = (): PairSlot[] => {
    const pairs: PairSlot[] = [
      { pokemon1: null, pokemon2: null },
      { pokemon1: null, pokemon2: null },
      { pokemon1: null, pokemon2: null }
    ];
    
    const usedPokemonIds = new Set<string>();
    let pairIndex = 0;

    // First, handle paired pokemons
    pokemons.forEach((pokemon) => {
      if (!pokemon || usedPokemonIds.has(pokemon.metadata.id)) return;
      
      if (pokemon.metadata.paired) {
        // Find the partner
        const partner = pokemons.find(p => p?.metadata.id === pokemon.metadata.paired);
        if (partner && !usedPokemonIds.has(partner.metadata.id)) {
          // Place both pokemons in the same pair
          if (pairIndex < 3) {
            pairs[pairIndex] = { pokemon1: pokemon, pokemon2: partner };
            usedPokemonIds.add(pokemon.metadata.id);
            usedPokemonIds.add(partner.metadata.id);
            pairIndex++;
          }
        }
      }
    });

    // Then, handle single pokemons
    pokemons.forEach((pokemon) => {
      if (!pokemon || usedPokemonIds.has(pokemon.metadata.id)) return;
      
      if (!pokemon.metadata.paired) {
        // Find an empty slot in pairs
        for (let i = 0; i < 3; i++) {
          if (pairs[i].pokemon1 === null) {
            pairs[i].pokemon1 = pokemon;
            usedPokemonIds.add(pokemon.metadata.id);
            break;
          } else if (pairs[i].pokemon2 === null) {
            pairs[i].pokemon2 = pokemon;
            usedPokemonIds.add(pokemon.metadata.id);
            break;
          }
        }
      }
    });

    return pairs;
  };

  const pairs = organizeIntoPairs();

  useEffect(() => {
    // Update heights after component mounts and whenever pokemons change
    const heights = slotRefs.current.map(slot => slot?.offsetHeight ?? 0);
    setSlotHeights(heights);
    heights.forEach((height, index) => {
      console.log(`WedLocke Slot ${index + 1} height:`, height);
    });
  }, [pokemons]);

  return (
    <div className="wedlocke-party-container">
      <div className="wedlocke-party-header">
        <span className="wedlocke-heart">💕</span>
        Wedding Party
        <span className="wedlocke-heart">💕</span>
      </div>
      <div className="wedlocke-party-content">
        {pairs.map((pair, pairIndex) => (
          <div key={pairIndex} className="wedlocke-pair-row">
            {/* First pokemon in pair */}
            <div 
              className="wedlocke-pair-slot"
              ref={el => slotRefs.current[pairIndex * 2] = el}
            >
              {pair.pokemon1 ? (
                <div className="wedlocke-pokemon-wrapper">
                  <Pokemon 
                    pokemon={pair.pokemon1}
                    onClick={onPokemonClick}
                    height={slotHeights[pairIndex * 2] || 0}
                  />
                  <div className="wedlocke-status">
                    {pair.pokemon1.metadata.gender === 'male' ? '👨' : pair.pokemon1.metadata.gender === 'female' ? '👩' : '❓'}
                  </div>
                </div>
              ) : (
                <div className="wedlocke-empty-slot">
                  <span className="wedlocke-ring">💍</span>
                  <span>Available</span>
                </div>
              )}
            </div>

            {/* Second pokemon in pair */}
            <div 
              className="wedlocke-pair-slot"
              ref={el => slotRefs.current[pairIndex * 2 + 1] = el}
            >
              {pair.pokemon2 ? (
                <div className="wedlocke-pokemon-wrapper">
                  <Pokemon 
                    pokemon={pair.pokemon2}
                    onClick={onPokemonClick}
                    height={slotHeights[pairIndex * 2 + 1] || 0}
                  />
                  <div className="wedlocke-status">
                    {pair.pokemon2.metadata.gender === 'male' ? '👨' : pair.pokemon2.metadata.gender === 'female' ? '👩' : '❓'}
                  </div>
                </div>
              ) : (
                <div className="wedlocke-empty-slot">
                  <span className="wedlocke-ring">💍</span>
                  <span>Available</span>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default WedLockeParty; 