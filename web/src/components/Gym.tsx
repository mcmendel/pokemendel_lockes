import React from 'react';
import { Box, Checkbox, Typography, Button } from '@mui/material';
import { BattleResponse } from '../api/lockeApi';
import lockeApi from '../api/lockeApi';
import './Gym.css';

interface GymProps {
  gym: BattleResponse;
  gameName: string;
  onGymClick: (leader: string) => void;
}

function Gym({ gym, gameName, onGymClick }: GymProps) {
  const handleCheckboxChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.checked && !gym.won) {
      // Only trigger if we're checking an unchecked gym
      onGymClick(gym.leader);
    }
  };

  return (
    <div className="gym-container">
      <Box sx={{ 
        display: 'flex', 
        flexDirection: 'column', 
        alignItems: 'center',
        p: 2,
        border: '1px solid #e0e0e0',
        borderRadius: 2,
        backgroundColor: gym.won ? '#e8f5e8' : '#f9f9f9',
        minHeight: '150px',
        width: '100%'
      }}>
        <img 
          src={lockeApi.getGymLeaderImageUrl(gameName, gym.leader)}
          alt={gym.leader}
          style={{ 
            width: '80px', 
            height: '80px', 
            objectFit: 'contain',
            marginBottom: '12px'
          }}
          onError={(e) => {
            const target = e.target as HTMLImageElement;
            target.src = `https://placehold.co/80x80/1976d2/ffffff?text=${gym.leader}`;
          }}
        />
        <Typography variant="h6" sx={{ textAlign: 'center', fontWeight: 500, marginBottom: '8px' }}>
          {gym.leader}
        </Typography>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
          <Checkbox
            checked={gym.won}
            onChange={handleCheckboxChange}
            disabled={gym.won}
            sx={{
              color: '#666',
              '&.Mui-checked': {
                color: '#2e7d32',
              },
            }}
          />
          <Typography variant="body2" sx={{ color: gym.won ? '#2e7d32' : '#666' }}>
            {gym.won ? 'Defeated' : 'Not defeated'}
          </Typography>
        </Box>
      </Box>
    </div>
  );
}

export default Gym; 