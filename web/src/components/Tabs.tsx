import React, { useState } from 'react';
import { Tabs as MuiTabs, Tab, Box, Typography, Grid, TextField } from '@mui/material';
import lockeApi from '../api/lockeApi';
import './Tabs.css';

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

function a11yProps(index: number) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

interface TabsProps {
  // Add props here when needed
}

function Tabs({}: TabsProps) {
  const [value, setValue] = useState(0);
  const [searchTerm, setSearchTerm] = useState('');

  // Static data for Potential Encounters
  const potentialEncounters = ["Pikachu", "Squirtle", "Mewtwo", "Rattata"];

  // Filter Pokemon based on search term
  const filteredEncounters = potentialEncounters.filter(pokemon =>
    pokemon.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  return (
    <div className="tabs-container">
      <div className="tabs-header">Tabs</div>
      <div className="tabs-content">
        <Box sx={{ width: '100%' }}>
          <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
            <MuiTabs value={value} onChange={handleChange} aria-label="basic tabs example" variant="scrollable" scrollButtons="auto">
              <Tab label="Statistics" {...a11yProps(0)} />
              <Tab label="Box" {...a11yProps(1)} />
              <Tab label="Graveyard" {...a11yProps(2)} />
              <Tab label="Gyms" {...a11yProps(3)} />
              <Tab label="Supported Pokemons" {...a11yProps(4)} />
              <Tab label="Potential Encounters" {...a11yProps(5)} />
              <Tab label="Important Battles" {...a11yProps(6)} />
            </MuiTabs>
          </Box>
          <TabPanel value={value} index={0}>
            <Typography variant="h6">Statistics</Typography>
            <Typography>Run statistics and general information will be displayed here.</Typography>
          </TabPanel>
          <TabPanel value={value} index={1}>
            <Typography variant="h6">Box</Typography>
            <Typography>Pokemon box management and storage will be available here.</Typography>
          </TabPanel>
          <TabPanel value={value} index={2}>
            <Typography variant="h6">Graveyard</Typography>
            <Typography>Fallen Pokemon and death information will be shown here.</Typography>
          </TabPanel>
          <TabPanel value={value} index={3}>
            <Typography variant="h6">Gyms</Typography>
            <Typography>Gym battle information and progress will be displayed here.</Typography>
          </TabPanel>
          <TabPanel value={value} index={4}>
            <Typography variant="h6">Supported Pokemons</Typography>
            <Typography>List of supported Pokemon and their details will be shown here.</Typography>
          </TabPanel>
          <TabPanel value={value} index={5}>
            <Typography variant="h6">Potential Encounters</Typography>
            <TextField
              fullWidth
              variant="outlined"
              placeholder="Search Pokemon..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              sx={{ mb: 2, mt: 1 }}
            />
            <Grid container spacing={2}>
              {filteredEncounters.map((pokemon, index) => (
                <Grid item xs={6} sm={4} md={3} key={index}>
                  <Box sx={{ 
                    display: 'flex', 
                    flexDirection: 'column', 
                    alignItems: 'center',
                    p: 2,
                    border: '1px solid #e0e0e0',
                    borderRadius: 2,
                    backgroundColor: '#f9f9f9'
                  }}>
                    <img 
                      src={lockeApi.getPokemonImageUrl(pokemon)}
                      alt={pokemon}
                      style={{ 
                        width: '80px', 
                        height: '80px', 
                        objectFit: 'contain',
                        marginBottom: '8px'
                      }}
                      onError={(e) => {
                        const target = e.target as HTMLImageElement;
                        target.src = `https://placehold.co/80x80/1976d2/ffffff?text=${pokemon}`;
                      }}
                    />
                    <Typography variant="body2" sx={{ textAlign: 'center', fontWeight: 500 }}>
                      {pokemon}
                    </Typography>
                  </Box>
                </Grid>
              ))}
            </Grid>
          </TabPanel>
          <TabPanel value={value} index={6}>
            <Typography variant="h6">Important Battles</Typography>
            <Typography>Important battle information and strategies will be available here.</Typography>
          </TabPanel>
        </Box>
      </div>
    </div>
  );
}

export default Tabs; 