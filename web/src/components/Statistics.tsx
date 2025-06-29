import React from 'react';
import { Box, Typography, Grid, Paper } from '@mui/material';
import { RunResponse } from '../api/lockeApi';
import './Statistics.css';

interface StatisticsProps {
  runData: RunResponse;
}

function Statistics({ runData }: StatisticsProps) {
  // Calculate statistics from run data
  const totalEncounters = runData.run.encounters.length;
  const caughtPokemon = runData.run.encounters.filter(e => e.status === 'Caught').length;
  const killedPokemon = runData.run.encounters.filter(e => e.status === 'Killed').length;
  const ranPokemon = runData.run.encounters.filter(e => e.status === 'Ran').length;
  const metPokemon = runData.run.encounters.filter(e => e.status === 'Met').length;
  const partySize = runData.run.party.filter(p => p !== null).length;
  const boxSize = runData.run.box.length;
  const gymsWon = runData.run.gyms.filter(g => g.won).length;
  const totalGyms = runData.run.gyms.length;
  const restarts = runData.run.restarts;
  const deadPokemon = Object.values(runData.pokemons).filter(p => p.status === 'Dead').length;

  return (
    <div className="statistics-container">
      <div className="statistics-header">Statistics</div>
      <div className="statistics-content">
        <Grid container spacing={3}>
          {/* Encounter Statistics */}
          <Grid item xs={12} md={6}>
            <Paper sx={{ p: 3, height: '100%' }}>
              <Typography variant="h6" sx={{ mb: 2, color: '#1976d2' }}>
                Encounters
              </Typography>
              <Grid container spacing={2}>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">Total Encounters</Typography>
                  <Typography variant="h4">{totalEncounters}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">Caught</Typography>
                  <Typography variant="h4" sx={{ color: '#2e7d32' }}>{caughtPokemon}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">Killed</Typography>
                  <Typography variant="h4" sx={{ color: '#d32f2f' }}>{killedPokemon}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">Ran</Typography>
                  <Typography variant="h4" sx={{ color: '#f57c00' }}>{ranPokemon}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">Met</Typography>
                  <Typography variant="h4" sx={{ color: '#666' }}>{metPokemon}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">Catch Rate</Typography>
                  <Typography variant="h4" sx={{ color: '#2e7d32' }}>
                    {totalEncounters > 0 ? Math.round((caughtPokemon / totalEncounters) * 100) : 0}%
                  </Typography>
                </Grid>
              </Grid>
            </Paper>
          </Grid>

          {/* Team & Progress Statistics */}
          <Grid item xs={12} md={6}>
            <Paper sx={{ p: 3, height: '100%' }}>
              <Typography variant="h6" sx={{ mb: 2, color: '#1976d2' }}>
                Team & Progress
              </Typography>
              <Grid container spacing={2}>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">Party Size</Typography>
                  <Typography variant="h4">{partySize}/6</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">Box Size</Typography>
                  <Typography variant="h4">{boxSize}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">Gyms Won</Typography>
                  <Typography variant="h4" sx={{ color: '#2e7d32' }}>{gymsWon}/{totalGyms}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">Restarts</Typography>
                  <Typography variant="h4" sx={{ color: '#d32f2f' }}>{restarts}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">Gym Progress</Typography>
                  <Typography variant="h4" sx={{ color: '#1976d2' }}>
                    {totalGyms > 0 ? Math.round((gymsWon / totalGyms) * 100) : 0}%
                  </Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="text.secondary">Dead Pokemon</Typography>
                  <Typography variant="h4" sx={{ color: '#d32f2f' }}>{deadPokemon}</Typography>
                </Grid>
              </Grid>
            </Paper>
          </Grid>
        </Grid>
      </div>
    </div>
  );
}

export default Statistics; 