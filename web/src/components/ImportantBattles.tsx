import React from 'react';
import { Typography, List, ListItem, ListItemText, Paper, ListItemIcon } from '@mui/material';
import SportsEsportsIcon from '@mui/icons-material/SportsEsports';
import { RunResponse } from '../api/lockeApi';
import './ImportantBattles.css';

interface ImportantBattlesProps {
  runData: RunResponse;
}

function ImportantBattles({ runData }: ImportantBattlesProps) {
  // Get battles from runData.run.main_battles, fallback to empty array
  const battles = runData.run.main_battles || [];

  return (
    <div className="important-battles-container">
      <div className="important-battles-header">Important Battles</div>
      <div className="important-battles-content">
        <Paper sx={{ p: 2 }}>
          <List>
            {battles.map((battle: string, index: number) => (
              <ListItem key={index} sx={{ py: 1 }}>
                <ListItemIcon>
                  <SportsEsportsIcon sx={{ color: '#1976d2' }} />
                </ListItemIcon>
                <ListItemText 
                  primary={battle}
                  sx={{
                    '& .MuiListItemText-primary': {
                      fontSize: '16px',
                      fontWeight: 500,
                      color: '#333'
                    }
                  }}
                />
              </ListItem>
            ))}
          </List>
        </Paper>
      </div>
    </div>
  );
}

export default ImportantBattles; 