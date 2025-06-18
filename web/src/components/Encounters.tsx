import React from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import lockeApi from '../api/lockeApi';
import './Encounters.css';

interface Encounter {
  pokemon: string | null;
  route: string;
  status: string;
}

interface EncountersProps {
  encounters: Encounter[];
}

function Encounters({ encounters }: EncountersProps) {
  return (
    <div className="encounters-container">
      <div className="encounters-header">Encounters</div>
      <div className="encounters-content">
        <TableContainer component={Paper} sx={{ backgroundColor: 'transparent', boxShadow: 'none' }}>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell sx={{ color: '#222', fontWeight: 'bold', borderBottom: '1px solid #ccc' }}>
                  Route
                </TableCell>
                <TableCell sx={{ color: '#222', fontWeight: 'bold', borderBottom: '1px solid #ccc' }}>
                  Encounter
                </TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {encounters.map((encounter, index) => {
                // Determine row styling based on status
                let rowStyle = {};
                let cellStyle = { color: '#444', borderBottom: '1px solid #eee' };
                
                if (encounter.status === 'Killed' || encounter.status === 'Ran') {
                  rowStyle = { backgroundColor: '#ffebee' }; // Light red
                } else if (encounter.status === 'Met') {
                  rowStyle = { backgroundColor: '#424242' }; // Dark gray
                  cellStyle = { color: 'white', borderBottom: '1px solid #666' };
                }
                
                return (
                  <TableRow key={index} sx={{ 
                    '&:hover': { backgroundColor: encounter.status === 'Met' ? '#616161' : 'rgba(0,0,0,0.03)' },
                    ...rowStyle
                  }}>
                    <TableCell sx={cellStyle}>
                      {encounter.route}
                    </TableCell>
                    <TableCell sx={cellStyle}>
                      {encounter.pokemon ? (
                        <img 
                          src={lockeApi.getPokemonImageUrl(encounter.pokemon)}
                          alt={encounter.pokemon}
                          style={{ 
                            width: '40px', 
                            height: '40px', 
                            objectFit: 'contain',
                            borderRadius: '4px'
                          }}
                          onError={(e) => {
                            const target = e.target as HTMLImageElement;
                            target.src = `https://placehold.co/40x40/1976d2/ffffff?text=${encounter.pokemon}`;
                          }}
                        />
                      ) : (
                        <div style={{ 
                          width: '40px', 
                          height: '40px', 
                          backgroundColor: encounter.status === 'Met' ? '#666' : '#f0f0f0',
                          borderRadius: '4px',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          color: encounter.status === 'Met' ? 'white' : '#888',
                          fontSize: '12px'
                        }}>
                          ?
                        </div>
                      )}
                    </TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </TableContainer>
      </div>
    </div>
  );
}

export default Encounters; 