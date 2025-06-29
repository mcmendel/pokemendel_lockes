import React from 'react';
import { Typography, Grid, Paper, Box } from '@mui/material';
import { RunResponse } from '../api/lockeApi';
import './Rules.css';

interface RulesProps {
  runData?: RunResponse;
}

function Rules({ runData }: RulesProps) {
  // Use actual rules from run data, fallback to empty array if not available
  const rules = runData?.run?.rules || [];

  return (
    <div className="rules-container">
      <div className="rules-header">Rules</div>
      <div className="rules-content">
        {rules.length > 0 ? (
          <Grid container spacing={2}>
            {rules.map((rule, index) => (
              <Grid item xs={12} key={index}>
                <Paper 
                  className="rule-sticker"
                  sx={{
                    p: 3,
                    height: '100%',
                    background: index % 2 === 0 
                      ? 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'  // Even rows - purple-blue
                      : 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)', // Odd rows - pink-red
                    color: 'white',
                    borderRadius: '16px',
                    boxShadow: '0 8px 32px rgba(0, 0, 0, 0.1)',
                    transition: 'all 0.3s ease',
                    cursor: 'pointer',
                    position: 'relative',
                    overflow: 'hidden',
                    '&:hover': {
                      transform: 'translateY(-4px)',
                      boxShadow: '0 12px 40px rgba(0, 0, 0, 0.15)',
                    },
                    '&::before': {
                      content: '""',
                      position: 'absolute',
                      top: 0,
                      left: 0,
                      right: 0,
                      bottom: 0,
                      background: 'linear-gradient(45deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%)',
                      pointerEvents: 'none',
                    }
                  }}
                >
                  <Box sx={{ position: 'relative', zIndex: 1 }}>
                    <Typography 
                      variant="h6" 
                      sx={{ 
                        mb: 1, 
                        fontWeight: 600,
                        textShadow: '0 2px 4px rgba(0,0,0,0.3)'
                      }}
                    >
                      Rule {index + 1}
                    </Typography>
                    <Typography 
                      variant="body1"
                      sx={{ 
                        lineHeight: 1.6,
                        textShadow: '0 1px 2px rgba(0,0,0,0.3)'
                      }}
                    >
                      {rule}
                    </Typography>
                  </Box>
                  <Box 
                    sx={{
                      position: 'absolute',
                      top: '8px',
                      right: '8px',
                      width: '24px',
                      height: '24px',
                      borderRadius: '50%',
                      background: 'rgba(255,255,255,0.2)',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontSize: '12px',
                      fontWeight: 'bold'
                    }}
                  >
                    {index + 1}
                  </Box>
                </Paper>
              </Grid>
            ))}
          </Grid>
        ) : (
          <Paper 
            sx={{ 
              p: 4, 
              textAlign: 'center',
              background: 'linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)',
              borderRadius: '12px'
            }}
          >
            <Typography 
              variant="h6" 
              sx={{ 
                color: '#666',
                mb: 1,
                fontWeight: 500
              }}
            >
              No Rules Available
            </Typography>
            <Typography 
              variant="body2" 
              sx={{ 
                color: '#888',
                fontStyle: 'italic'
              }}
            >
              This run doesn't have any specific rules defined.
            </Typography>
          </Paper>
        )}
      </div>
    </div>
  );
}

export default Rules; 