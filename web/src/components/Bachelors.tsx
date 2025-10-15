import React from 'react';
import { Box, Typography, Grid } from '@mui/material';
import Pokemon from './Pokemon';
import { Pokemon as PokemonType } from '../api/lockeApi';

interface BachelorsProps {
  pokemons: Array<PokemonType | null>;
  onPokemonClick: (id: string) => void;
}

function Bachelors({ pokemons, onPokemonClick }: BachelorsProps) {
  const toNormalizedGender = (g: string | null | undefined) => (g || '').trim().toLowerCase();

  const bachelors = (pokemons || [])
    .filter((p): p is PokemonType => !!p)
    // must have gender and not be paired
    .filter(p => !!toNormalizedGender(p.metadata.gender) && !p.metadata.paired);

  const maleBachelors = bachelors.filter(p => toNormalizedGender(p.metadata.gender) === 'male');
  const femaleBachelors = bachelors.filter(p => toNormalizedGender(p.metadata.gender) === 'female');

  return (
    <Box sx={{ width: '100%' }}>
      <Grid container spacing={2}>
        <Grid item xs={12} md={6}>
          <Typography variant="h6" sx={{ mb: 2 }}>Male</Typography>
          <Grid container spacing={2}
            sx={{ alignItems: 'stretch' }}>
            {maleBachelors.map((p) => (
              <Grid item xs={6} sm={4} md={6} key={p.metadata.id}>
                <Pokemon
                  pokemon={p}
                  onClick={onPokemonClick}
                  height={140}
                />
              </Grid>
            ))}
            {maleBachelors.length === 0 && (
              <Grid item xs={12}>
                <Typography color="text.secondary" variant="body2">No male bachelors</Typography>
              </Grid>
            )}
          </Grid>
        </Grid>

        <Grid item xs={12} md={6}>
          <Typography variant="h6" sx={{ mb: 2 }}>Female</Typography>
          <Grid container spacing={2}
            sx={{ alignItems: 'stretch' }}>
            {femaleBachelors.map((p) => (
              <Grid item xs={6} sm={4} md={6} key={p.metadata.id}>
                <Pokemon
                  pokemon={p}
                  onClick={onPokemonClick}
                  height={140}
                />
              </Grid>
            ))}
            {femaleBachelors.length === 0 && (
              <Grid item xs={12}>
                <Typography color="text.secondary" variant="body2">No female bachelors</Typography>
              </Grid>
            )}
          </Grid>
        </Grid>
      </Grid>
    </Box>
  );
}

export default Bachelors;


