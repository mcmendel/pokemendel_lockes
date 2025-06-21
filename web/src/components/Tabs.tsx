import React, { useState, useEffect } from 'react';
import { Tabs as MuiTabs, Tab, Box, Typography, Grid, TextField, CircularProgress } from '@mui/material';
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
  runId?: string; // Add runId prop to access the API
}

function Tabs({ runId }: TabsProps) {
  const [value, setValue] = useState(0);
  const [searchTerm, setSearchTerm] = useState('');
  const [supportedSearchTerm, setSupportedSearchTerm] = useState('');
  const [supportedPokemons, setSupportedPokemons] = useState<string[]>([]);
  const [loadingSupported, setLoadingSupported] = useState(false);
  const [errorSupported, setErrorSupported] = useState<string | null>(null);
  const [encounters, setEncounters] = useState<string[]>([]);
  const [loadingEncounters, setLoadingEncounters] = useState(false);
  const [errorEncounters, setErrorEncounters] = useState<string | null>(null);

  // Fetch supported pokemons when component mounts or runId changes
  useEffect(() => {
    if (runId) {
      setLoadingSupported(true);
      setErrorSupported(null);
      lockeApi.getPotentialPokemons(runId)
        .then(data => {
          setSupportedPokemons(data);
          setLoadingSupported(false);
        })
        .catch(error => {
          console.error('Error fetching supported pokemons:', error);
          setErrorSupported('Failed to load supported pokemons');
          setLoadingSupported(false);
        });
    }
  }, [runId]);

  // Fetch encounters when component mounts or runId changes
  useEffect(() => {
    if (runId) {
      setLoadingEncounters(true);
      setErrorEncounters(null);
      lockeApi.getEncounters(runId)
        .then(data => {
          setEncounters(data);
          setLoadingEncounters(false);
        })
        .catch(error => {
          console.error('Error fetching encounters:', error);
          setErrorEncounters('Failed to load encounters');
          setLoadingEncounters(false);
        });
    }
  }, [runId]);

  // Filter Pokemon based on search term
  const filteredEncounters = encounters.filter(pokemon =>
    pokemon.toLowerCase().includes(searchTerm.toLowerCase())
  );
  
  // Filter Supported Pokemon based on search term
  const filteredSupportedPokemons = supportedPokemons.filter(pokemon =>
    pokemon.toLowerCase().includes(supportedSearchTerm.toLowerCase())
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
            <TextField
              fullWidth
              variant="outlined"
              placeholder="Search Supported Pokemon..."
              value={supportedSearchTerm}
              onChange={(e) => setSupportedSearchTerm(e.target.value)}
              sx={{ mb: 2, mt: 1 }}
            />
            {loadingSupported ? (
              <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
                <CircularProgress />
              </Box>
            ) : errorSupported ? (
              <Typography sx={{ textAlign: 'center', mt: 2, color: '#d32f2f' }}>
                {errorSupported}
              </Typography>
            ) : (
              <>
                <Grid container spacing={2}>
                  {filteredSupportedPokemons.map((pokemon, index) => (
                    <Grid item xs={6} sm={4} md={3} key={index}>
                      <Box sx={{ 
                        display: 'flex', 
                        flexDirection: 'column', 
                        alignItems: 'center',
                        p: 2,
                        border: '1px solid #e0e0e0',
                        borderRadius: 2,
                        backgroundColor: '#f0f8ff'
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
                {filteredSupportedPokemons.length === 0 && supportedPokemons.length > 0 && (
                  <Typography sx={{ textAlign: 'center', mt: 2, color: '#666' }}>
                    No supported Pokemon found matching "{supportedSearchTerm}"
                  </Typography>
                )}
              </>
            )}
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
            {loadingEncounters ? (
              <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
                <CircularProgress />
              </Box>
            ) : errorEncounters ? (
              <Typography sx={{ textAlign: 'center', mt: 2, color: '#d32f2f' }}>
                {errorEncounters}
              </Typography>
            ) : (
              <>
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
                {filteredEncounters.length === 0 && encounters.length > 0 && (
                  <Typography sx={{ textAlign: 'center', mt: 2, color: '#666' }}>
                    No Pokemon found matching "{searchTerm}"
                  </Typography>
                )}
              </>
            )}
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