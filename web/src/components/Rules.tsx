import React from 'react';
import { Typography, List, ListItem, ListItemText, Paper } from '@mui/material';
import { RunResponse } from '../api/lockeApi';
import './Rules.css';

interface RulesProps {
  runData: RunResponse;
}

function Rules({ runData }: RulesProps) {
  const rules = runData.run.rules || [];

  return (
    <div className="rules-container">
      <div className="rules-header">Rules</div>
      <div className="rules-content">
        <Paper sx={{ p: 2 }}>
          <List>
            {rules.map((rule, index) => (
              <ListItem key={index} sx={{ py: 1 }}>
                <ListItemText 
                  primary={rule}
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

export default Rules; 