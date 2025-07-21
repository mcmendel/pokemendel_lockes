import React, { useEffect, useState } from 'react';
import { useParams, Navigate } from 'react-router-dom';
import { Box, Typography, Paper, Grid, Container, CircularProgress, Button } from '@mui/material';
import { RunResponse, Pokemon } from '../api/lockeApi';
import lockeApi from '../api/lockeApi';
import './Celebration.css';

function Celebration() {
  const { runId } = useParams<{ runId: string }>();
  const [runData, setRunData] = useState<RunResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!runId) return;
    
    (async () => {
      try {
        const runResponse = await lockeApi.getRun(runId);
        setRunData(runResponse);
        
        // Redirect to run page if the run is not finished
        if (!runResponse.run.finished) {
          window.location.href = `/locke_manager/run/${runId}`;
          return;
        }
      } catch (e) {
        console.error('Error fetching run data:', e);
        setError("Failed to fetch run data.");
      } finally {
        setLoading(false);
      }
    })();
  }, [runId]);

  if (!runId) return <Navigate to="/locke_manager" replace />;
  if (error) return <div>Error: {error}</div>;
  if (loading) {
    return (
      <div className="celebration-container">
        <Container maxWidth="lg">
          <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '50vh' }}>
            <CircularProgress size={60} />
          </Box>
        </Container>
      </div>
    );
  }
  if (!runData) return <div>No run data found</div>;

  // Get surviving Pokemon from the party
  const survivingPokemon = runData.run.party
    .map(pokemonId => runData.pokemons[pokemonId])
    .filter(pokemon => pokemon && pokemon.status !== 'dead');

  // Get all Pokemon that were caught during the run (including dead ones)
  const allCaughtPokemon = Object.values(runData.pokemons);

  return (
    <div className="celebration-container">
      <Container maxWidth="lg">
        <Box className="celebration-header">
          <Typography variant="h2" className="celebration-title">
            🎉 Run Complete! 🎉
          </Typography>
          <Typography variant="h4" className="run-name">
            {runData.run.run_name}
          </Typography>
          <Typography variant="h6" className="completion-message">
            Congratulations! You've completed your Locke run!
          </Typography>
          <Button 
            variant="contained" 
            color="primary" 
            size="large"
            onClick={() => window.location.href = '/locke_manager'}
            sx={{ 
              mt: 3, 
              px: 4, 
              py: 1.5,
              fontSize: '1.1rem',
              borderRadius: '25px',
              boxShadow: '0 4px 12px rgba(0,0,0,0.2)',
              '&:hover': {
                transform: 'translateY(-2px)',
                boxShadow: '0 6px 16px rgba(0,0,0,0.3)'
              }
            }}
          >
            Back to Runs
          </Button>
        </Box>

        <Box className="celebration-content">
          <Paper elevation={3} className="survivors-section">
            <Typography variant="h4" className="section-title">
              🏆 Survivors ({survivingPokemon.length})
            </Typography>
            <Typography variant="body1" className="section-subtitle">
              These Pokemon made it through the entire journey!
            </Typography>
            
            <Grid container spacing={3} className="survivors-grid">
              {survivingPokemon.map((pokemon) => (
                <Grid item xs={12} sm={6} md={4} lg={3} key={pokemon.metadata.id}>
                  <Paper elevation={2} className="pokemon-card survivor-card">
                    <Box className="pokemon-image-container">
                      <img 
                        src={lockeApi.getPokemonImageUrl(pokemon.name)}
                        alt={pokemon.name}
                        className="pokemon-image"
                        onError={(e) => {
                          const target = e.target as HTMLImageElement;
                          target.src = `https://placehold.co/200x200/4caf50/ffffff?text=${pokemon.name}`;
                        }}
                      />
                    </Box>
                    <Box className="pokemon-info">
                      <Typography variant="h6" className="pokemon-name">
                        {pokemon.name}
                      </Typography>
                      {pokemon.metadata.nickname && (
                        <Typography variant="subtitle1" className="pokemon-nickname">
                          "{pokemon.metadata.nickname}"
                        </Typography>
                      )}
                      <Typography variant="body2" className="pokemon-status">
                        Survivor
                      </Typography>
                    </Box>
                  </Paper>
                </Grid>
              ))}
            </Grid>
          </Paper>

          <Paper elevation={3} className="statistics-section">
            <Typography variant="h4" className="section-title">
              📊 Run Statistics
            </Typography>
            
            <Grid container spacing={4} className="stats-grid">
              <Grid item xs={12} md={6}>
                <Box className="stat-card">
                  <Typography variant="h3" className="stat-number">
                    {survivingPokemon.length}
                  </Typography>
                  <Typography variant="h6" className="stat-label">
                    Survivors
                  </Typography>
                </Box>
              </Grid>
              
              <Grid item xs={12} md={6}>
                <Box className="stat-card">
                  <Typography variant="h3" className="stat-number">
                    {allCaughtPokemon.filter(p => p.status === 'dead').length}
                  </Typography>
                  <Typography variant="h6" className="stat-label">
                    Fallen Comrades
                  </Typography>
                </Box>
              </Grid>
              
              <Grid item xs={12} md={6}>
                <Box className="stat-card">
                  <Typography variant="h3" className="stat-number">
                    {allCaughtPokemon.length}
                  </Typography>
                  <Typography variant="h6" className="stat-label">
                    Total Pokemon Caught
                  </Typography>
                </Box>
              </Grid>
              
              <Grid item xs={12} md={6}>
                <Box className="stat-card">
                  <Typography variant="h3" className="stat-number">
                    {runData.run.gyms.filter(gym => gym.won).length}
                  </Typography>
                  <Typography variant="h6" className="stat-label">
                    Gyms Defeated
                  </Typography>
                </Box>
              </Grid>
            </Grid>
          </Paper>

          <Paper elevation={3} className="all-pokemon-section">
            <Typography variant="h4" className="section-title">
              📋 All Pokemon from the Run
            </Typography>
            
            <Grid container spacing={2} className="all-pokemon-grid">
              {allCaughtPokemon.map((pokemon) => (
                <Grid item xs={6} sm={4} md={3} lg={2} key={pokemon.metadata.id}>
                  <Paper 
                    elevation={1} 
                    className={`pokemon-mini-card ${pokemon.status === 'dead' ? 'dead-pokemon' : 'alive-pokemon'}`}
                  >
                    <img 
                      src={lockeApi.getPokemonImageUrl(pokemon.name)}
                      alt={pokemon.name}
                      className={`pokemon-mini-image ${pokemon.status === 'dead' ? 'dead-image' : ''}`}
                      onError={(e) => {
                        const target = e.target as HTMLImageElement;
                        target.src = `https://placehold.co/80x80/1976d2/ffffff?text=${pokemon.name}`;
                      }}
                    />
                    <Typography variant="caption" className="pokemon-mini-name">
                      {pokemon.name}
                    </Typography>
                    {pokemon.metadata.nickname && (
                      <Typography variant="caption" className="pokemon-mini-nickname">
                        "{pokemon.metadata.nickname}"
                      </Typography>
                    )}
                  </Paper>
                </Grid>
              ))}
            </Grid>
          </Paper>
        </Box>
      </Container>
    </div>
  );
}

export default Celebration; 