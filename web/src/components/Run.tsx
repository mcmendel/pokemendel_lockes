import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import lockeApi, { RunResponse, Pokemon, StatusResponse } from "../api/lockeApi";
import SaveIcon from '@mui/icons-material/Save';
import UploadIcon from '@mui/icons-material/Upload';
import FlagIcon from '@mui/icons-material/Flag';
import Party from './Party';
import Encounters from './Encounters';
import Tabs from './Tabs';
import { 
    Tooltip, 
    Snackbar, 
    Alert, 
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    Button
} from '@mui/material';
import './Run.css';

function RunComponent() {
  const { runId } = useParams<{ runId: string }>();
  const [runData, setRunData] = useState<RunResponse | null>(null);
  const [starterOptions, setStarterOptions] = useState<string[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [selectedStarter, setSelectedStarter] = useState<string | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
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

  const handlePokemonClick = (pokemonId: string) => {
    alert(`Clicked Pokemon ID: ${pokemonId}`);
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
          </div>
        ) : (
          <>
            <div className="run-content">
              <Party 
                pokemons={getPartyPokemons()}
                onPokemonClick={handlePokemonClick}
              />
              <Encounters encounters={runData.run.encounters} runId={runId} />
              <Tabs runId={runId} />
            </div>
          </>
        )}
      </div>

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