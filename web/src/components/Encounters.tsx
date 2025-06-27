import React, { useState, useEffect } from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Dialog, DialogTitle, DialogContent, DialogActions, Button, Typography, Grid, CircularProgress, Box, TextField, InputAdornment, List, ListItem, ListItemButton, ListItemText } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import lockeApi, { RunResponse, Pokemon } from '../api/lockeApi';
import './Encounters.css';

interface Encounter {
  pokemon: string | null;
  route: string;
  status: string;
}

interface EncountersProps {
  encounters: Encounter[];
  runId?: string;
  runData?: RunResponse;
  setRunData?: (data: RunResponse) => void;
  setSnackbar?: (snackbar: { open: boolean; message: string; severity: 'success' | 'error' }) => void;
}

function Encounters({ encounters, runId, runData, setRunData, setSnackbar }: EncountersProps) {
  const [selectedEncounter, setSelectedEncounter] = useState<Encounter | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [encounterPokemons, setEncounterPokemons] = useState<string[]>([]);
  const [loadingEncounters, setLoadingEncounters] = useState(false);
  const [errorEncounters, setErrorEncounters] = useState<string | null>(null);
  const [searchTerm, setSearchTerm] = useState('');
  
  // New state for status selection dialog
  const [isStatusDialogOpen, setIsStatusDialogOpen] = useState(false);
  const [selectedPokemonForStatus, setSelectedPokemonForStatus] = useState<{ pokemon: string; route: string } | null>(null);
  const [updatingStatus, setUpdatingStatus] = useState(false);

  // Helper function to get pokemon display info based on encounter type
  const getPokemonDisplayInfo = (encounter: Encounter) => {
    if (!encounter.pokemon) {
      return { name: null, imageUrl: null, pokemonData: null };
    }

    if (encounter.status === 'Caught') {
      // For "Caught" status, pokemon is an ID - get from runData.pokemons
      const pokemonData = runData?.pokemons[encounter.pokemon];
      if (pokemonData) {
        return {
          name: pokemonData.name,
          imageUrl: lockeApi.getPokemonImageUrl(pokemonData.name),
          pokemonData: pokemonData
        };
      }
      return { name: encounter.pokemon, imageUrl: null, pokemonData: null };
    } else {
      // For "Met", "Killed", "Ran" status, pokemon is the name
      return {
        name: encounter.pokemon,
        imageUrl: lockeApi.getPokemonImageUrl(encounter.pokemon),
        pokemonData: null
      };
    }
  };

  const handleEncounterClick = (encounter: Encounter) => {
    setSelectedEncounter(encounter);
    setIsDialogOpen(true);
    setSearchTerm(''); // Reset search when opening dialog
    // Fetch encounters when dialog opens
    if (runId) {
      setLoadingEncounters(true);
      setErrorEncounters(null);
      lockeApi.getEncounters(runId, encounter.route)
        .then(data => {
          setEncounterPokemons(data);
          setLoadingEncounters(false);
        })
        .catch(error => {
          console.error('Error fetching encounters:', error);
          setErrorEncounters('Failed to load encounters');
          setLoadingEncounters(false);
        });
    }
  };

  const handlePokemonClick = (encounter: Encounter) => {
    // Only handle clicks for "Met" encounters with a pokemon
    if (encounter.status === 'Met' && encounter.pokemon) {
      setSelectedPokemonForStatus({ pokemon: encounter.pokemon, route: encounter.route });
      setIsStatusDialogOpen(true);
    }
    // For "Caught" encounters, we could add different functionality if needed
    // For now, no action for "Caught", "Killed", "Ran" encounters
  };

  const handleStatusSelection = async (status: string) => {
    if (!runId || !selectedPokemonForStatus || !setRunData || !setSnackbar) return;

    setUpdatingStatus(true);
    try {
      const response = await lockeApi.updateEncounterStatus(runId, selectedPokemonForStatus.route, status);
      if (response.status === 'success') {
        // Fetch updated run data
        const updatedRun = await lockeApi.getRun(runId);
        setRunData(updatedRun);
        setSnackbar({
          open: true,
          message: `Successfully updated ${selectedPokemonForStatus.pokemon} status to ${status}!`,
          severity: 'success'
        });
        // Close the status dialog
        handleStatusDialogClose();
      }
    } catch (error) {
      console.error('Error updating encounter status:', error);
      setSnackbar({
        open: true,
        message: `Failed to update encounter status: ${error instanceof Error ? error.message : 'Unknown error'}`,
        severity: 'error'
      });
    } finally {
      setUpdatingStatus(false);
    }
  };

  const handleStatusDialogClose = () => {
    setIsStatusDialogOpen(false);
    setSelectedPokemonForStatus(null);
    setUpdatingStatus(false);
  };

  const handlePokemonDoubleClick = async (pokemonName: string) => {
    if (!runId || !selectedEncounter || !setRunData || !setSnackbar) return;

    try {
      const response = await lockeApi.setEncounter(runId, selectedEncounter.route, pokemonName);
      if (response.status === 'success') {
        // Fetch updated run data
        const updatedRun = await lockeApi.getRun(runId);
        setRunData(updatedRun);
        setSnackbar({
          open: true,
          message: `Successfully set ${pokemonName} as encounter for ${selectedEncounter.route}!`,
          severity: 'success'
        });
        // Close the dialog
        handleDialogClose();
      }
    } catch (error) {
      console.error('Error setting encounter:', error);
      setSnackbar({
        open: true,
        message: `Failed to set encounter: ${error instanceof Error ? error.message : 'Unknown error'}`,
        severity: 'error'
      });
    }
  };

  const handleDialogClose = () => {
    setIsDialogOpen(false);
    setSelectedEncounter(null);
    setEncounterPokemons([]);
    setLoadingEncounters(false);
    setErrorEncounters(null);
    setSearchTerm('');
  };

  // Filter pokemon based on search term
  const filteredPokemons = encounterPokemons.filter(pokemon =>
    pokemon.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="encounters-container">
      <div className="encounters-header">Encounters</div>
      <div className="encounters-content">
        <TableContainer component={Paper} sx={{ backgroundColor: 'transparent', boxShadow: 'none' }}>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell sx={{ color: '#222', fontWeight: 'bold', borderBottom: '1px solid #ccc' }}>
                  Route
                </TableCell>
                <TableCell sx={{ color: '#222', fontWeight: 'bold', borderBottom: '1px solid #ccc' }}>
                  Encounter
                </TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {encounters.map((encounter, index) => {
                // Determine row styling based on status
                let rowStyle = {};
                let cellStyle = { color: '#444', borderBottom: '1px solid #eee' };
                
                if (encounter.status === 'Killed' || encounter.status === 'Ran') {
                  rowStyle = { backgroundColor: '#ffebee' }; // Light red
                } else if (encounter.status === 'Met') {
                  rowStyle = { backgroundColor: '#424242' }; // Dark gray
                  cellStyle = { color: 'white', borderBottom: '1px solid #666' };
                }
                
                return (
                  <TableRow 
                    key={index} 
                    sx={{ 
                      '&:hover': { backgroundColor: encounter.status === 'Met' ? '#616161' : 'rgba(0,0,0,0.03)' },
                      cursor: !encounter.pokemon ? 'pointer' : (encounter.status === 'Met' ? 'pointer' : 'default'),
                      ...rowStyle
                    }}
                    onClick={!encounter.pokemon ? () => handleEncounterClick(encounter) : (encounter.status === 'Met' ? () => handlePokemonClick(encounter) : undefined)}
                  >
                    <TableCell sx={cellStyle}>
                      {encounter.route}
                    </TableCell>
                    <TableCell sx={cellStyle}>
                      {(() => {
                        const pokemonInfo = getPokemonDisplayInfo(encounter);
                        if (pokemonInfo.name && pokemonInfo.imageUrl) {
                          return (
                            <img 
                              src={pokemonInfo.imageUrl}
                              alt={pokemonInfo.name}
                              style={{ 
                                width: '40px', 
                                height: '40px', 
                                objectFit: 'contain',
                                borderRadius: '4px'
                              }}
                              onError={(e) => {
                                const target = e.target as HTMLImageElement;
                                target.src = `https://placehold.co/40x40/1976d2/ffffff?text=${pokemonInfo.name}`;
                              }}
                            />
                          );
                        } else if (pokemonInfo.name) {
                          return (
                            <div style={{ 
                              width: '40px', 
                              height: '40px', 
                              backgroundColor: '#f0f0f0',
                              borderRadius: '4px',
                              display: 'flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                              color: '#888',
                              fontSize: '10px',
                              textAlign: 'center',
                              padding: '2px'
                            }}>
                              {pokemonInfo.name}
                            </div>
                          );
                        } else {
                          return (
                            <div style={{ 
                              width: '40px', 
                              height: '40px', 
                              backgroundColor: encounter.status === 'Met' ? '#666' : '#f0f0f0',
                              borderRadius: '4px',
                              display: 'flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                              color: encounter.status === 'Met' ? 'white' : '#888',
                              fontSize: '12px'
                            }}>
                              ?
                            </div>
                          );
                        }
                      })()}
                    </TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </TableContainer>
      </div>

      <Dialog
        open={isDialogOpen}
        onClose={handleDialogClose}
        aria-labelledby="encounter-dialog-title"
        maxWidth="md"
        fullWidth
      >
        <DialogTitle id="encounter-dialog-title">
          Encounters for Route: {selectedEncounter?.route}
        </DialogTitle>
        <DialogContent>
          {loadingEncounters ? (
            <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
              <CircularProgress />
            </Box>
          ) : errorEncounters ? (
            <Typography sx={{ textAlign: 'center', mt: 2, color: '#d32f2f' }}>
              {errorEncounters}
            </Typography>
          ) : (
            <Grid container spacing={2} sx={{ mt: 1 }}>
              <Grid item xs={12}>
                <TextField
                  label="Search"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  InputProps={{
                    startAdornment: (
                      <InputAdornment position="start">
                        <SearchIcon />
                      </InputAdornment>
                    ),
                  }}
                />
              </Grid>
              {filteredPokemons.map((pokemon, index) => (
                <Grid item xs={6} sm={4} md={3} key={index}>
                  <Box 
                    sx={{ 
                      display: 'flex', 
                      flexDirection: 'column', 
                      alignItems: 'center',
                      p: 2,
                      border: '1px solid #e0e0e0',
                      borderRadius: 2,
                      backgroundColor: '#f9f9f9',
                      cursor: 'pointer',
                      '&:hover': {
                        backgroundColor: '#f0f0f0',
                        borderColor: '#1976d2'
                      }
                    }}
                    onDoubleClick={() => handlePokemonDoubleClick(pokemon)}
                  >
                    <img 
                      src={lockeApi.getPokemonImageUrl(pokemon)}
                      alt={pokemon}
                      style={{ 
                        width: '80px', 
                        height: '80px', 
                        objectFit: 'contain',
                        marginBottom: '8px'
                      }}
                      onError={(e) => {
                        const target = e.target as HTMLImageElement;
                        target.src = `https://placehold.co/80x80/1976d2/ffffff?text=${pokemon}`;
                      }}
                    />
                    <Typography variant="body2" sx={{ textAlign: 'center', fontWeight: 500 }}>
                      {pokemon}
                    </Typography>
                  </Box>
                </Grid>
              ))}
            </Grid>
          )}
          {encounterPokemons.length === 0 && !loadingEncounters && !errorEncounters && (
            <Typography sx={{ textAlign: 'center', mt: 2, color: '#666' }}>
              No encounters found for this route.
            </Typography>
          )}
          {encounterPokemons.length > 0 && filteredPokemons.length === 0 && (
            <Typography sx={{ textAlign: 'center', mt: 2, color: '#666' }}>
              No pokemon found matching "{searchTerm}".
            </Typography>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleDialogClose} color="primary">
            Close
          </Button>
        </DialogActions>
      </Dialog>

      {/* Status Selection Dialog */}
      <Dialog
        open={isStatusDialogOpen}
        onClose={handleStatusDialogClose}
        aria-labelledby="status-dialog-title"
        maxWidth="sm"
        fullWidth
      >
        <DialogTitle id="status-dialog-title">
          Update Status for {selectedPokemonForStatus ? getPokemonDisplayInfo({ pokemon: selectedPokemonForStatus.pokemon, route: selectedPokemonForStatus.route, status: 'Met' }).name : ''}
        </DialogTitle>
        <DialogContent>
          <Typography variant="body1" sx={{ mb: 2 }}>
            Choose the new status for this encounter:
          </Typography>
          <List>
            {['Caught', 'Killed', 'Ran'].map((status) => (
              <ListItem key={status} disablePadding>
                <ListItemButton 
                  onClick={() => handleStatusSelection(status)}
                  disabled={updatingStatus}
                  sx={{
                    '&:hover': {
                      backgroundColor: status === 'Caught' ? '#e8f5e8' : 
                                   status === 'Killed' ? '#ffebee' : '#fff3e0'
                    }
                  }}
                >
                  <ListItemText 
                    primary={status}
                    sx={{
                      color: status === 'Caught' ? '#2e7d32' : 
                             status === 'Killed' ? '#d32f2f' : '#f57c00'
                    }}
                  />
                </ListItemButton>
              </ListItem>
            ))}
          </List>
          {updatingStatus && (
            <Box sx={{ display: 'flex', justifyContent: 'center', mt: 2 }}>
              <CircularProgress size={24} />
            </Box>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleStatusDialogClose} disabled={updatingStatus}>
            Cancel
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}

export default Encounters; 