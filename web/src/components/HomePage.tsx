import React, { useEffect, useState } from 'react';
import LockeRunsTable from './LockeRunsTable';
import lockeApi from '../api/lockeApi';
import { ListRun } from '../api/lockeApi';
import { useNavigate } from 'react-router-dom';
import './HomePage.css';

const HomePage: React.FC = () => {
  const [runs, setRuns] = useState<ListRun[]>([]);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchRuns = async () => {
      try {
        const data = await lockeApi.getRuns();
        setRuns(data);
      } catch (err) {
        setError('Failed to fetch runs');
        console.error('Error fetching runs:', err);
      }
    };

    fetchRuns();
  }, []);

  const handleRowDoubleClick = (runId: string) => {
    navigate(`/locke_manager/run/${runId}`);
  };

  return (
    <div className="home-container">
      {error ? (
        <div className="error-message">{error}</div>
      ) : (
        <LockeRunsTable 
          runs={runs} 
          onRowDoubleClick={handleRowDoubleClick}
        />
      )}
    </div>
  );
};

export default HomePage; 