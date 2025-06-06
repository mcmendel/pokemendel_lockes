import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import lockeApi from "../api/lockeApi";
import SaveIcon from '@mui/icons-material/Save';
import UploadIcon from '@mui/icons-material/Upload';
import FlagIcon from '@mui/icons-material/Flag';
import { Tooltip } from '@mui/material';
import './Run.css';

const Run: React.FC = () => {
  const { runId } = useParams<{ runId: string }>();
  const [run, setRun] = useState<{ id: string, run_name: string } | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!runId) return;
    
    (async () => {
      try {
        const data = await lockeApi.getRun(runId);
        setRun(data);
      } catch (e) {
        setError("Failed to fetch run.");
      }
    })();
  }, [runId]);

  const handleIconClick = (action: string) => {
    alert(`${action} clicked!`);
  };

  if (!runId) return <p>Error: No run ID provided</p>;
  if (error) return <p>Error: {error}</p>;
  if (!run) return <p>Loading…</p>;

  return (
    <div className="pokemendel-run-container">
      <div className="run-header">
        <h1 className="run-title">{run.run_name}</h1>
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
      <div className="run-id">Run ID: {run.id}</div>
      <div className="run-name">Run Name: {run.run_name}</div>
    </div>
  );
};

export default Run; 