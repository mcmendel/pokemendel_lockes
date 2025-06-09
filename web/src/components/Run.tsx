import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import lockeApi from "../api/lockeApi";
import type { Run } from "../api/lockeApi";
import SaveIcon from '@mui/icons-material/Save';
import UploadIcon from '@mui/icons-material/Upload';
import FlagIcon from '@mui/icons-material/Flag';
import { Tooltip, Snackbar, Alert } from '@mui/material';
import './Run.css';

function RunComponent() {
  const { runId } = useParams<{ runId: string }>();
  const [run, setRun] = useState<Run | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [snackbar, setSnackbar] = useState<{ open: boolean; message: string; severity: 'success' | 'error' }>({
    open: false,
    message: '',
    severity: 'success'
  });

  useEffect(() => {
    if (!runId) return;
    
    (async () => {
      try {
        const data = await lockeApi.getRun(runId);
        console.log('Run data:', data);
        setRun(data);
      } catch (e) {
        setError("Failed to fetch run.");
      }
    })();
  }, [runId]);

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
      setRun(loadedRun);
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
          setRun(updatedRun);
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

  if (!runId) return <p>Error: No run ID provided</p>;
  if (error) return <p>Error: {error}</p>;
  if (!run) return <p>Loading…</p>;

  return (
    <div className="pokemendel-run-container">
      <div className="run-header">
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
      <div className="run-info">
        <div className="run-name">Run Name: {run.run_name}</div>
        <div className="run-id">Run ID: {run.id}</div>
      </div>

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