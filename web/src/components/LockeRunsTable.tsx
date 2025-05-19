import React, { useState } from 'react';
import { DataGrid, GridRenderCellParams } from '@mui/x-data-grid';
import { FormControlLabel, IconButton, Checkbox } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import './LockeRunsTable.css';

interface LockeRun {
  created_at: string;
  finished: boolean;
  game: string;
  id: string;
  locke: string;
  name: string;
  num_badges: number;
  num_deaths: number;
  num_pokemons: number;
  num_restarts: number;
  randomized: boolean;
  starter: string;
}

interface Props {
  runs: LockeRun[];
  onDelete?: (runId: string) => void;
  onRowClick?: (runId: string) => void;
}

function daysPassed(dateString: string): number {
  const givenDate = new Date(dateString);
  const currentDate = new Date();
  const differenceInMilliseconds = currentDate.getTime() - givenDate.getTime();
  const millisecondsInOneDay = 1000 * 60 * 60 * 24;
  const daysPassed = Math.floor(differenceInMilliseconds / millisecondsInOneDay);
  return daysPassed;
}

const LockeRunsTable: React.FC<Props> = ({ runs, onDelete, onRowClick }) => {
  const [showOnlyFinished, setShowOnlyFinished] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');

  const filteredRuns = runs
    .filter(run => !showOnlyFinished || !run.finished)
    .filter(run => run.name.toLowerCase().includes(searchQuery.toLowerCase()));

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
        {daysPassed(params.value as string)} days ago
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
            placeholder="Search by name..."
            value={searchQuery}
            onChange={(e: React.ChangeEvent<HTMLInputElement>) => setSearchQuery(e.target.value)}
          />
        </div>
        <FormControlLabel 
          control={
            <Checkbox
              checked={showOnlyFinished}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => setShowOnlyFinished(e.target.checked)}
            />
          }
          label="Filter finished runs"
        />
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
        className="locke-runs-table"
      />
    </div>
  );
};

export default LockeRunsTable; 