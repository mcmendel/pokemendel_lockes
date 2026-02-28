import React from 'react';
import { Grid, Typography, Box } from '@mui/material';
import Pokemon from './Pokemon';
import { Pokemon as PokemonType } from '../api/lockeApi';
import './WedLockeBox.css';

interface WedLockeBoxProps {
  pokemons: Array<PokemonType | null>;
  onPokemonClick: (id: string) => void;
}

interface PairSlot {
  pokemon1: PokemonType;
  pokemon2: PokemonType;
}

function WedLockeBox({ pokemons, onPokemonClick }: WedLockeBoxProps) {
  const validPokemons = pokemons.filter(
    (p): p is PokemonType =>
      p != null && p.status !== 'dead' && p.status !== 'Dead'
  );

  // Organize into pairs (paired) and singles by gender (unpaired)
  const usedIds = new Set<string>();
  const pairs: PairSlot[] = [];
  const unpairedMales: PokemonType[] = [];
  const unpairedFemales: PokemonType[] = [];
  const unpairedOther: PokemonType[] = [];

  const normalizeGender = (g: string | null) => g?.toLowerCase() ?? '';

  validPokemons.forEach((pokemon) => {
    if (usedIds.has(pokemon.metadata.id)) return;

    if (pokemon.metadata.paired) {
      const partner = validPokemons.find((p) => p.metadata.id === pokemon.metadata.paired);
      if (partner && !usedIds.has(partner.metadata.id)) {
        pairs.push({ pokemon1: pokemon, pokemon2: partner });
        usedIds.add(pokemon.metadata.id);
        usedIds.add(partner.metadata.id);
      } else {
        const g = normalizeGender(pokemon.metadata.gender);
        if (g === 'male') unpairedMales.push(pokemon);
        else if (g === 'female') unpairedFemales.push(pokemon);
        else unpairedOther.push(pokemon);
        usedIds.add(pokemon.metadata.id);
      }
    } else {
      const g = normalizeGender(pokemon.metadata.gender);
      if (g === 'male') unpairedMales.push(pokemon);
      else if (g === 'female') unpairedFemales.push(pokemon);
      else unpairedOther.push(pokemon);
      usedIds.add(pokemon.metadata.id);
    }
  });

  const getGenderEmoji = (gender: string | null) => {
    if (!gender) return '❓';
    const g = gender.toLowerCase();
    return g === 'male' ? '👨' : g === 'female' ? '👩' : '❓';
  };

  return (
    <div className="wedlocke-box-container">
      <div className="wedlocke-box-header">
        <span className="wedlocke-box-heart">💕</span>
        Wedding Box
        <span className="wedlocke-box-heart">💕</span>
      </div>
      <div className="wedlocke-box-content">
        {validPokemons.length === 0 ? (
          <Box
            sx={{
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              height: '200px',
              color: '#d63384',
            }}
          >
            <Typography variant="body1">No Pokémon in box</Typography>
          </Box>
        ) : (
          <>
            {pairs.length > 0 && (
              <div className="wedlocke-box-section">
                <div className="wedlocke-box-section-title">
                  <span className="wedlocke-box-heart">💍</span>
                  Paired
                  <span className="wedlocke-box-heart">💍</span>
                </div>
                <div className="wedlocke-box-pairs">
                  {pairs.map((pair, idx) => (
                    <div key={idx} className="wedlocke-box-pair-row">
                      <div className="wedlocke-box-pair-slot">
                        <div className="wedlocke-box-pokemon-wrapper">
                          <Pokemon
                            pokemon={pair.pokemon1}
                            onClick={onPokemonClick}
                            height={100}
                          />
                          <div className="wedlocke-box-status">
                            {getGenderEmoji(pair.pokemon1.metadata.gender)}
                          </div>
                        </div>
                      </div>
                      <div className="wedlocke-box-pair-connector">💕</div>
                      <div className="wedlocke-box-pair-slot">
                        <div className="wedlocke-box-pokemon-wrapper">
                          <Pokemon
                            pokemon={pair.pokemon2}
                            onClick={onPokemonClick}
                            height={100}
                          />
                          <div className="wedlocke-box-status">
                            {getGenderEmoji(pair.pokemon2.metadata.gender)}
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
            {(unpairedMales.length > 0 || unpairedFemales.length > 0 || unpairedOther.length > 0) && (
              <>
                {unpairedMales.length > 0 && (
                  <div className="wedlocke-box-section">
                    <div className="wedlocke-box-section-title">
                      <span className="wedlocke-box-heart">👨</span>
                      Unpaired — Male
                      <span className="wedlocke-box-heart">👨</span>
                    </div>
                    <Grid container spacing={2}>
                      {unpairedMales.map((pokemon) => (
                        <Grid item xs={6} sm={4} md={3} lg={2} key={pokemon.metadata.id}>
                          <div className="wedlocke-box-single-card">
                            <div className="wedlocke-box-pokemon-wrapper">
                              <Pokemon
                                pokemon={pokemon}
                                onClick={onPokemonClick}
                                height={100}
                              />
                              <div className="wedlocke-box-status">
                                {getGenderEmoji(pokemon.metadata.gender)}
                              </div>
                            </div>
                          </div>
                        </Grid>
                      ))}
                    </Grid>
                  </div>
                )}
                {unpairedFemales.length > 0 && (
                  <div className="wedlocke-box-section">
                    <div className="wedlocke-box-section-title">
                      <span className="wedlocke-box-heart">👩</span>
                      Unpaired — Female
                      <span className="wedlocke-box-heart">👩</span>
                    </div>
                    <Grid container spacing={2}>
                      {unpairedFemales.map((pokemon) => (
                        <Grid item xs={6} sm={4} md={3} lg={2} key={pokemon.metadata.id}>
                          <div className="wedlocke-box-single-card">
                            <div className="wedlocke-box-pokemon-wrapper">
                              <Pokemon
                                pokemon={pokemon}
                                onClick={onPokemonClick}
                                height={100}
                              />
                              <div className="wedlocke-box-status">
                                {getGenderEmoji(pokemon.metadata.gender)}
                              </div>
                            </div>
                          </div>
                        </Grid>
                      ))}
                    </Grid>
                  </div>
                )}
                {unpairedOther.length > 0 && (
                  <div className="wedlocke-box-section">
                    <div className="wedlocke-box-section-title">
                      <span className="wedlocke-box-heart">💒</span>
                      Unpaired — Other
                      <span className="wedlocke-box-heart">💒</span>
                    </div>
                    <Grid container spacing={2}>
                      {unpairedOther.map((pokemon) => (
                        <Grid item xs={6} sm={4} md={3} lg={2} key={pokemon.metadata.id}>
                          <div className="wedlocke-box-single-card">
                            <div className="wedlocke-box-pokemon-wrapper">
                              <Pokemon
                                pokemon={pokemon}
                                onClick={onPokemonClick}
                                height={100}
                              />
                              <div className="wedlocke-box-status">
                                {getGenderEmoji(pokemon.metadata.gender)}
                              </div>
                            </div>
                          </div>
                        </Grid>
                      ))}
                    </Grid>
                  </div>
                )}
              </>
            )}
          </>
        )}
      </div>
    </div>
  );
}

export default WedLockeBox;
