import React from 'react';
import { Grid, Typography, Box } from '@mui/material';
import { RunResponse } from '../api/lockeApi';
import Gym from './Gym';
import './Gyms.css';

interface GymsProps {
  runData: RunResponse;
  onGymClick: (leader: string) => void;
}

function Gyms({ runData, onGymClick }: GymsProps) {
  const gyms = runData.run.gyms || [];
  const gameName = runData.run.run_name.split(' - ')[1] || 'unknown'; // Extract game name from run name

  return (
    <div className="gyms-container">
      <div className="gyms-header">Gyms</div>
      <div className="gyms-content">
        {gyms.length === 0 ? (
          <Box sx={{ 
            display: 'flex', 
            justifyContent: 'center', 
            alignItems: 'center', 
            height: '200px',
            color: '#666'
          }}>
            <Typography variant="body1">No gym battles available</Typography>
          </Box>
        ) : (
          <Grid container spacing={3}>
            {gyms.map((gym, index) => (
              <Grid item xs={12} sm={6} md={4} lg={3} key={index}>
                <Gym 
                  gym={gym} 
                  gameName={gameName}
                  onGymClick={onGymClick}
                />
              </Grid>
            ))}
          </Grid>
        )}
      </div>
    </div>
  );
}

export default Gyms; 