import React, { useEffect, useState } from "react";
import { useParams, Navigate, useNavigate } from "react-router-dom";
import lockeApi, { RunResponse, Pokemon, StatusResponse } from "../api/lockeApi";
import SaveIcon from '@mui/icons-material/Save';
import UploadIcon from '@mui/icons-material/Upload';
import FlagIcon from '@mui/icons-material/Flag';
import Party from './Party';
import WedLockeParty from './WedLockeParty';
import Starter from './Starter';
import Encounters from './Encounters';
import Tabs from './Tabs';
import Rules from './Rules';
import SupportedPokemonList from './SupportedPokemonList';
import { 
    Tooltip, 
    Snackbar, 
    Alert, 
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    Button,
    Typography,
    Box,
    List,
    ListItem,
    ListItemText,
    CircularProgress,
    TextField
} from '@mui/material';
import './Run.css';

function RunComponent() {
  const { runId } = useParams<{ runId: string }>();
  const navigate = useNavigate();
  const [runData, setRunData] = useState<RunResponse | null>(null);
  const [starterOptions, setStarterOptions] = useState<string[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [selectedStarter, setSelectedStarter] = useState<string | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [selectedGymLeader, setSelectedGymLeader] = useState<string | null>(null);
  const [isGymDialogOpen, setIsGymDialogOpen] = useState(false);
  const [selectedPokemonId, setSelectedPokemonId] = useState<string | null>(null);
  const [isPokemonActionsDialogOpen, setIsPokemonActionsDialogOpen] = useState(false);
  const [pokemonActions, setPokemonActions] = useState<string[]>([]);
  const [loadingPokemonActions, setLoadingPokemonActions] = useState(false);
  const [selectedAction, setSelectedAction] = useState<string | null>(null);
  const [isActionInputDialogOpen, setIsActionInputDialogOpen] = useState(false);
  const [actionInputType, setActionInputType] = useState<string>('');
  const [actionInputOptions, setActionInputOptions] = useState<string[]>([]);
  const [actionInputText, setActionInputText] = useState<string>('');
  const [loadingActionInfo, setLoadingActionInfo] = useState(false);
  const [isBlackoutDialogOpen, setIsBlackoutDialogOpen] = useState(false);
  const [lockeType, setLockeType] = useState<string | null>(null);
  const [snackbar, setSnackbar] = useState<{ open: boolean; message: string; severity: 'success' | 'error' }>({
    open: false,
    message: '',
    severity: 'success'
  });

  useEffect(() => {
    if (!runId) return;
    
    (async () => {
      try {
        const runResponse = await lockeApi.getRun(runId);
        console.log('Run response:', runResponse);
        setRunData(runResponse);

        if (!runResponse.run.starter) {
          const options = await lockeApi.getStarterOptions(runId);
          console.log('Starter options:', options);
          setStarterOptions(options);
        }

        // Fetch locke type from list runs API
        const runs = await lockeApi.getRuns();
        const currentRun = runs.find(run => run.run_id === runId);
        if (currentRun) {
          setLockeType(currentRun.locke_name);
        }
      } catch (e) {
        console.error('Error fetching data:', e);
        setError("Failed to fetch run data.");
      }
    })();
  }, [runId]);

  // Helper function to get Pokémon name from ID
  const getPokemonName = (pokemonId: string | null): string => {
    if (!pokemonId || !runData) return '';
    return runData.pokemons[pokemonId]?.name || pokemonId;
  };

  const handleSave = async () => {
    if (!runId) return;
    
    try {
      const result = await lockeApi.saveRun(runId);
      if (result.status === 'success') {
        setSnackbar({
          open: true,
          message: 'Run saved successfully!',
          severity: 'success'
        });
      }
    } catch (e) {
      setSnackbar({
        open: true,
        message: 'Failed to save run',
        severity: 'error'
      });
    }
  };

  const handleLoad = async () => {
    if (!runId) return;
    
    try {
      const loadedRun = await lockeApi.loadRun(runId);
      setRunData(loadedRun);
      setSnackbar({
        open: true,
        message: 'Run loaded successfully!',
        severity: 'success'
      });
    } catch (e) {
      setSnackbar({
        open: true,
        message: 'Failed to load run',
        severity: 'error'
      });
    }
  };

  const handleIconClick = async (action: string) => {
    if (!runId) return;

    try {
      switch (action) {
        case 'Save':
          await handleSave();
          break;
        case 'Load':
          await handleLoad();
          break;
        case 'Finish':
          const updatedRun = await lockeApi.finishRun(runId);
          setRunData(updatedRun);
          setSnackbar({
            open: true,
            message: 'Run marked as finished!',
            severity: 'success'
          });
          break;
      }
    } catch (e) {
      if (e instanceof Error && (e as any).status === 322) {
        // Redirect to ContinueRun page when status 322 is received
        navigate(`/locke_manager/continue/${runId}`);
        return;
      }
      
      setSnackbar({
        open: true,
        message: `Failed to ${action.toLowerCase()} run: ${e instanceof Error ? e.message : 'Unknown error'}`,
        severity: 'error'
      });
    }
  };

  const handleCloseSnackbar = () => {
    setSnackbar(prev => ({ ...prev, open: false }));
  };

  const handleStarterClick = (pokemon: string) => {
    setSelectedStarter(pokemon);
    setIsDialogOpen(true);
  };

  const handleDialogClose = () => {
    setIsDialogOpen(false);
    setSelectedStarter(null);
  };

  const handleConfirmStarter = async () => {
    if (!runId || !selectedStarter) return;

    try {
      const response = await lockeApi.setStarter(runId, selectedStarter);
      if (response.status === 'success') {
        // Fetch updated run data
        const updatedRun = await lockeApi.getRun(runId);
        setRunData(updatedRun);
        setSnackbar({
          open: true,
          message: `Successfully chose ${selectedStarter} as your starter!`,
          severity: 'success'
        });
      }
    } catch (e) {
      setSnackbar({
        open: true,
        message: `Failed to set starter: ${e instanceof Error ? e.message : 'Unknown error'}`,
        severity: 'error'
      });
    } finally {
      handleDialogClose();
    }
  };

  const handlePokemonClick = async (pokemonId: string) => {
    try {
      setLoadingPokemonActions(true);
      setSelectedPokemonId(pokemonId);
      const actions = await lockeApi.getPokemonActions(runId!, pokemonId);
      setPokemonActions(actions);
      setIsPokemonActionsDialogOpen(true);
    } catch (error) {
      console.error('Error fetching pokemon actions:', error);
      setSnackbar({
        open: true,
        message: `Failed to fetch pokemon actions: ${error instanceof Error ? error.message : 'Unknown error'}`,
        severity: 'error'
      });
    } finally {
      setLoadingPokemonActions(false);
    }
  };

  const handlePokemonActionsDialogClose = () => {
    setIsPokemonActionsDialogOpen(false);
    setSelectedPokemonId(null);
    setPokemonActions([]);
  };

  const handleActionClick = async (action: string) => {
    if (!selectedPokemonId || !runId) return;

    try {
      setLoadingActionInfo(true);
      setSelectedAction(action);
      const actionInfo = await lockeApi.getPokemonActionInfo(runId, selectedPokemonId, action);
      
      setActionInputType(actionInfo.input_type);
      setActionInputOptions(actionInfo.input_options || []);
      setActionInputText('');

      if (actionInfo.input_type === 'Nothing') {
        // Execute action immediately with empty string value
        await executeAction(action, '');
        // Close the Pokemon actions popup after successful execution
        handlePokemonActionsDialogClose();
      } else {
        // Show input dialog for "Free text" or "One of"
        setIsActionInputDialogOpen(true);
      }
    } catch (error) {
      console.error('Error fetching action info:', error);
      setSnackbar({
        open: true,
        message: `Failed to get action info: ${error instanceof Error ? error.message : 'Unknown error'}`,
        severity: 'error'
      });
    } finally {
      setLoadingActionInfo(false);
    }
  };

  const executeAction = async (action: string, value: string) => {
    if (!selectedPokemonId || !runId) return;

    try {
      const response = await lockeApi.executePokemonAction(runId, selectedPokemonId, action, value);
      
      if (response.status === 'success') {
        // Refresh the run data
        const updatedRun = await lockeApi.getRun(runId);
        setRunData(updatedRun);
        
        setSnackbar({
          open: true,
          message: `Action "${action}" executed successfully!`,
          severity: 'success'
        });
      }
    } catch (error: any) {
      console.error('Error executing action:', error);
      
      // Check if it's a 522 status code (blackout)
      if (error.status === 522) {
        setIsBlackoutDialogOpen(true);
      } else {
        setSnackbar({
          open: true,
          message: `Failed to execute action: ${error instanceof Error ? error.message : 'Unknown error'}`,
          severity: 'error'
        });
      }
    }
  };

  const handleActionInputDialogClose = () => {
    setIsActionInputDialogOpen(false);
    setSelectedAction(null);
    setActionInputType('');
    setActionInputOptions([]);
    setActionInputText('');
  };

  const handleActionInputSubmit = async () => {
    if (!selectedAction) return;
    
    // Execute the action with the input value
    await executeAction(selectedAction, actionInputText);
    
    // Close dialogs
    handleActionInputDialogClose();
    handlePokemonActionsDialogClose();
  };

  const handleBlackoutDialogClose = () => {
    setIsBlackoutDialogOpen(false);
  };

  const handleBlackoutContinue = async () => {
    handleBlackoutDialogClose();
    // Call the same logic as the Load button
    await handleLoad();
  };

  const handleGymClick = (leader: string) => {
    setSelectedGymLeader(leader);
    setIsGymDialogOpen(true);
  };

  const handleGymDialogClose = () => {
    setIsGymDialogOpen(false);
    setSelectedGymLeader(null);
  };

  const handleConfirmGymVictory = async () => {
    if (!runId || !selectedGymLeader) return;

    try {
      // Call the API to mark gym as won
      const response = await lockeApi.markGymWon(runId, selectedGymLeader);
      
      if (response.status === 'success') {
        // Refresh the run data to get updated gym status
        const updatedRun = await lockeApi.getRun(runId);
        setRunData(updatedRun);
        
        setSnackbar({
          open: true,
          message: `Successfully defeated ${selectedGymLeader}!`,
          severity: 'success'
        });
      }
    } catch (e) {
      setSnackbar({
        open: true,
        message: `Failed to mark gym victory: ${e instanceof Error ? e.message : 'Unknown error'}`,
        severity: 'error'
      });
    } finally {
      handleGymDialogClose();
    }
  };

  // Helper function to get starter Pokemon data
  const getStarterPokemon = (): Pokemon | null => {
    if (!runData || !runData.run.starter) return null;
    return runData.pokemons[runData.run.starter] || null;
  };

  // Helper function to transform party data
  const getPartyPokemons = (): Array<Pokemon | null> => {
    if (!runData) return Array(6).fill(null);
    
    // Log the first pokemon to see its structure
    const firstPokemonId = runData.run.party[0];
    if (firstPokemonId) {
      console.log('First pokemon data:', runData.pokemons[firstPokemonId]);
    }
    
    // Create array of 6 slots
    return Array.from({ length: 6 }, (_, index) => {
      const pokemonId = runData.run.party[index];
      if (!pokemonId) return null;
      
      return runData.pokemons[pokemonId] || null;
    });
  };

  if (!runId) return <p>Error: No run ID provided</p>;
  if (error) return <p>Error: {error}</p>;
  if (!runData) return <p>Loading…</p>;
  
  // Redirect to celebration page if run is finished
  if (runData.run.finished) {
    return <Navigate to={`/locke_manager/celebration/${runId}`} replace />;
  }

  console.log('Current run data:', runData);
  console.log('Current run starter:', runData.run.starter);

  return (
    <div className="pokemendel-run-container">
      <div className="run-header">
        <div className="run-title">{runData.run.run_name}</div>
        <div className="run-actions">
          <Tooltip title="Save" placement="top">
            <span className="run-action-icon" onClick={() => handleIconClick("Save")}>
              <SaveIcon />
            </span>
          </Tooltip>
          <Tooltip title="Load" placement="top">
            <span className="run-action-icon" onClick={() => handleIconClick("Load")}>
              <UploadIcon />
            </span>
          </Tooltip>
          <Tooltip title="Finish" placement="top">
            <span className="run-action-icon" onClick={() => handleIconClick("Finish")}>
              <FlagIcon />
            </span>
          </Tooltip>
        </div>
      </div>
      <div className="run-content">
        {!runData.run.starter ? (
          <div className="run-main-content">
            <div className="status-message">No starter selected yet</div>
            {starterOptions.length > 0 ? (
              <div className="starter-options">
                {starterOptions.map((pokemon) => (
                  <div 
                    key={pokemon} 
                    className="starter-option"
                    onClick={() => handleStarterClick(pokemon)}
                  >
                    <img 
                      src={lockeApi.getPokemonImageUrl(pokemon)}
                      alt={pokemon}
                      className="starter-image"
                      onError={(e) => {
                        const target = e.target as HTMLImageElement;
                        target.src = `https://placehold.co/120x120/1976d2/ffffff?text=${pokemon}`;
                      }}
                    />
                    <div className="starter-name">{pokemon}</div>
                  </div>
                ))}
              </div>
            ) : (
              <div>Loading starter options...</div>
            )}
            
            {/* Show supported Pokemon list when no starter is selected */}
            <SupportedPokemonList runId={runId!} />
          </div>
        ) : (
          <div className="run-content">
            {lockeType === "WedLocke" ? (
              <WedLockeParty 
                pokemons={getPartyPokemons()}
                onPokemonClick={handlePokemonClick}
              />
            ) : (
              <Party 
                pokemons={getPartyPokemons()}
                onPokemonClick={handlePokemonClick}
              />
            )}
            {lockeType !== "EeveeLocke" && (
              <Starter 
                starter={getStarterPokemon()}
                onPokemonClick={handlePokemonClick}
              />
            )}
            {lockeType !== "EeveeLocke" && lockeType !== "StarterLocke" && (
              <Encounters 
                encounters={runData.run.encounters} 
                runId={runId} 
                runData={runData}
                setRunData={setRunData}
                setSnackbar={setSnackbar}
              />
            )}
            <Tabs runId={runId} runData={runData} onPokemonClick={handlePokemonClick} onGymClick={handleGymClick} lockeType={lockeType} />
          </div>
        )}
      </div>
      {runData?.run?.starter && <Rules runData={runData} />}

      <Dialog
        open={isDialogOpen}
        onClose={handleDialogClose}
        aria-labelledby="starter-dialog-title"
      >
        <DialogTitle id="starter-dialog-title">
          Choose Starter
        </DialogTitle>
        <DialogContent>
          {selectedStarter && (
            <p>Choose {selectedStarter} as your starter?</p>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleDialogClose} color="primary">
            No
          </Button>
          <Button onClick={handleConfirmStarter} color="primary" variant="contained">
            Yes
          </Button>
        </DialogActions>
      </Dialog>

      <Dialog
        open={isGymDialogOpen}
        onClose={handleGymDialogClose}
        aria-labelledby="gym-dialog-title"
      >
        <DialogTitle id="gym-dialog-title">
          Confirm Gym Victory
        </DialogTitle>
        <DialogContent>
          {selectedGymLeader && (
            <p>Did you defeat {selectedGymLeader}?</p>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleGymDialogClose} color="primary">
            No
          </Button>
          <Button onClick={handleConfirmGymVictory} color="primary" variant="contained">
            Yes
          </Button>
        </DialogActions>
      </Dialog>

      <Dialog
        open={isPokemonActionsDialogOpen}
        onClose={handlePokemonActionsDialogClose}
        maxWidth="sm"
        fullWidth
      >
        <DialogTitle>
          Pokemon Actions
          {selectedPokemonId && runData?.pokemons[selectedPokemonId] && (
            <>
              <Typography variant="h6">
                {runData.pokemons[selectedPokemonId].name}
              </Typography>
              {runData.pokemons[selectedPokemonId].metadata.nickname && (
                <Typography variant="subtitle2" color="text.secondary">
                  "{runData.pokemons[selectedPokemonId].metadata.nickname}"
                </Typography>
              )}
            </>
          )}
        </DialogTitle>
        <DialogContent>
          {loadingPokemonActions ? (
            <Box sx={{ display: 'flex', justifyContent: 'center', p: 3 }}>
              <CircularProgress />
            </Box>
          ) : pokemonActions.length === 0 ? (
            <Typography sx={{ p: 2, textAlign: 'center', color: 'text.secondary' }}>
              No actions available for this Pokémon
            </Typography>
          ) : (
            <List>
              {pokemonActions.map((action, index) => (
                <ListItem 
                  key={index} 
                  button 
                  onClick={() => handleActionClick(action)}
                  sx={{ 
                    border: '1px solid #e0e0e0', 
                    borderRadius: 1, 
                    mb: 1,
                    '&:hover': {
                      backgroundColor: '#f5f5f5'
                    }
                  }}
                >
                  <ListItemText primary={action} />
                </ListItem>
              ))}
            </List>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={handlePokemonActionsDialogClose} color="primary">
            Close
          </Button>
        </DialogActions>
      </Dialog>

      <Dialog
        open={isActionInputDialogOpen}
        onClose={handleActionInputDialogClose}
        maxWidth="sm"
        fullWidth
      >
        <DialogTitle>
          {selectedAction}
          {selectedPokemonId && runData?.pokemons[selectedPokemonId] && (
            <Typography variant="subtitle2" color="text.secondary">
              for {runData.pokemons[selectedPokemonId].name}
            </Typography>
          )}
        </DialogTitle>
        <DialogContent>
          {loadingActionInfo ? (
            <Box sx={{ display: 'flex', justifyContent: 'center', p: 3 }}>
              <CircularProgress />
            </Box>
          ) : actionInputType === 'Free text' ? (
            <TextField
              autoFocus
              margin="dense"
              label="Enter text"
              type="text"
              fullWidth
              variant="outlined"
              value={actionInputText}
              onChange={(e) => setActionInputText(e.target.value)}
              sx={{ mt: 2 }}
            />
          ) : actionInputType === 'One of' ? (
            <Box sx={{ mt: 2 }}>
              <Typography variant="body2" sx={{ mb: 2 }}>
                Select a Pokemon:
              </Typography>
              <List>
                {actionInputOptions.map((pokemonId, index) => {
                  const pokemon = runData?.pokemons[pokemonId];
                  return (
                    <ListItem 
                      key={index} 
                      button 
                      onClick={() => setActionInputText(pokemonId)}
                      selected={actionInputText === pokemonId}
                      sx={{ 
                        border: '1px solid #e0e0e0', 
                        borderRadius: 1, 
                        mb: 1,
                        '&:hover': {
                          backgroundColor: '#f5f5f5'
                        },
                        '&.Mui-selected': {
                          backgroundColor: '#e3f2fd',
                          borderColor: '#1976d2'
                        }
                      }}
                    >
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, width: '100%' }}>
                        <img 
                          src={lockeApi.getPokemonImageUrl(pokemon?.name || pokemonId)}
                          alt={pokemon?.name || pokemonId}
                          style={{ 
                            width: '40px', 
                            height: '40px', 
                            objectFit: 'contain' 
                          }}
                          onError={(e) => {
                            const target = e.target as HTMLImageElement;
                            target.src = `https://placehold.co/40x40/1976d2/ffffff?text=${pokemon?.name || pokemonId}`;
                          }}
                        />
                        <ListItemText 
                          primary={pokemon?.name || pokemonId}
                          secondary={pokemon?.metadata?.nickname ? `"${pokemon.metadata.nickname}"` : undefined}
                        />
                      </Box>
                    </ListItem>
                  );
                })}
              </List>
            </Box>
          ) : null}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleActionInputDialogClose} color="primary">
            Cancel
          </Button>
          {(actionInputType === 'Free text' && actionInputText.trim()) || 
           (actionInputType === 'One of' && actionInputText) ? (
            <Button onClick={handleActionInputSubmit} color="primary" variant="contained">
              Submit
            </Button>
          ) : null}
        </DialogActions>
      </Dialog>

      <Dialog
        open={isBlackoutDialogOpen}
        onClose={handleBlackoutDialogClose}
        aria-labelledby="blackout-dialog-title"
      >
        <DialogTitle id="blackout-dialog-title">
          Blackout
        </DialogTitle>
        <DialogContent>
          <Typography>
            Blackout happened. You need to load from last save
          </Typography>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleBlackoutContinue} color="primary" variant="contained">
            Continue
          </Button>
        </DialogActions>
      </Dialog>

      <Snackbar 
        open={snackbar.open} 
        autoHideDuration={6000} 
        onClose={handleCloseSnackbar}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert 
          onClose={handleCloseSnackbar} 
          severity={snackbar.severity}
          sx={{ width: '100%' }}
        >
          {snackbar.message}
        </Alert>
      </Snackbar>
    </div>
  );
}

export default RunComponent;