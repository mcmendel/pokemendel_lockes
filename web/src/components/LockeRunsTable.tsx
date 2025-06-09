import React, { useState } from 'react';
import { DataGrid, GridRenderCellParams } from '@mui/x-data-grid';
import { FormControlLabel, IconButton, Checkbox } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import { useNavigate } from 'react-router-dom';
import './LockeRunsTable.css';
import { ListRun } from '../api/lockeApi';

interface Props {
  runs: ListRun[];
  onDelete?: (runId: string) => void;
  onRowClick?: (runId: string) => void;
  onRowDoubleClick?: (runId: string) => void;
}

function daysPassed(dateString: string): string {
  const givenDate = new Date(dateString);
  const currentDate = new Date();
  
  // Reset time part to compare only dates
  givenDate.setHours(0, 0, 0, 0);
  currentDate.setHours(0, 0, 0, 0);
  
  const differenceInMilliseconds = currentDate.getTime() - givenDate.getTime();
  const millisecondsInOneDay = 1000 * 60 * 60 * 24;
  const daysPassed = Math.floor(differenceInMilliseconds / millisecondsInOneDay);
  
  if (daysPassed === 0) {
    return 'Today';
  } else if (daysPassed === 1) {
    return 'Yesterday';
  } else if (daysPassed < 0) {
    return 'Today'; // Handle future dates
  } else {
    return `${daysPassed} days ago`;
  }
}

export const LockeRunsTable: React.FC<Props> = ({ runs, onDelete, onRowClick, onRowDoubleClick }) => {
  const navigate = useNavigate();
  const [showOnlyFinished, setShowOnlyFinished] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');

  const filteredRuns = runs
    .filter(run => !showOnlyFinished || !run.finished)
    .filter(run => {
      const runName = run.run_name?.toLowerCase() || '';
      const query = searchQuery.toLowerCase();
      return runName.includes(query);
    })
    .map(run => ({
      id: run.run_id, // Required by DataGrid
      name: run.run_name || 'Unnamed Run',
      game: run.game_name || 'Unknown Game',
      locke: run.locke_name || 'Unknown Locke',
      starter: run.starter || 'Unknown Starter',
      num_badges: run.num_gyms || 0,
      num_deaths: run.num_deaths || 0,
      num_pokemons: run.num_pokemons || 0,
      num_restarts: run.num_restarts || 0,
      created_at: run.created_at || new Date().toISOString(),
      finished: run.finished,
      randomized: run.randomized,
    }));

  const columns = [
    { field: 'id', headerName: 'ID', width: 70, filterable: false, hide: true },
    {
      field: 'actions',
      headerName: 'Delete',
      width: 70,
      renderCell: (params: GridRenderCellParams) => (
        <IconButton
          color="secondary"
          onClick={() => onDelete?.(params.id as string)}
        >
          <DeleteIcon />
        </IconButton>
      ),
    },
    { 
      field: 'finished', 
      headerName: 'Status', 
      width: 120, 
      filterable: true,
      renderCell: (params: GridRenderCellParams) => (
        <span className={`status ${params.value ? 'finished' : 'in-progress'}`}>
          {params.value ? 'Finished' : 'In Progress'}
        </span>
      )
    },
    { field: 'name', headerName: 'Name', width: 170, filterable: false },
    { field: 'created_at', headerName: 'Created At', width: 130, renderCell: (params: GridRenderCellParams) => (
      <strong>
        {daysPassed(params.value as string)}
      </strong>
    )},
    { field: 'game', headerName: 'Game', width: 170, filterable: false },
    { field: 'locke', headerName: 'Locke', width: 170, filterable: false },
    { field: 'starter', headerName: 'Starter', width: 170, filterable: false },
    { field: 'num_badges', headerName: 'Badges', width: 100, filterable: false },
    { field: 'num_pokemons', headerName: 'Pokémon', width: 120, filterable: false },
    { field: 'num_deaths', headerName: 'Deaths', width: 100, filterable: false },
    { field: 'num_restarts', headerName: 'Restarts', width: 100, filterable: false },
  ];

  return (
    <div className="locke-runs-container">
      <div className="filter-controls">
        <div className="search-box">
          <input
            type="text"
            placeholder="Search runs..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
        </div>
        <div className="action-buttons">
          <button className="action-button new" onClick={() => navigate('/locke_manager/new')}>
            <span>New</span>
          </button>
          <button className="action-button load">
            <span>Load</span>
          </button>
        </div>
        <div className="filter-checkbox">
          <input
            type="checkbox"
            id="showFinished"
            checked={showOnlyFinished}
            onChange={(e) => setShowOnlyFinished(e.target.checked)}
          />
          <label htmlFor="showFinished">Show only finished runs</label>
        </div>
      </div>
      <DataGrid 
        rows={filteredRuns} 
        columns={columns} 
        pageSize={10}
        autoHeight
        disableColumnMenu
        initialState={{
          columns: {
            columnVisibilityModel: {
              id: false,
            },
          },
        }}
        onRowClick={(params) => onRowClick?.(params.id as string)}
        onRowDoubleClick={(params) => onRowDoubleClick?.(params.id as string)}
        className="locke-runs-table"
      />
    </div>
  );
};

export default LockeRunsTable; 