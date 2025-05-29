import React, { useEffect, useState } from 'react';
import LockeRunsTable from './LockeRunsTable';
import lockeApi from '../api/lockeApi';
import { Run } from '../api/lockeApi';

const HomePage: React.FC = () => {
  const [runs, setRuns] = useState<Run[]>([]);
  const [error, setError] = useState<string | null>(null);

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

  return (
    <div>
      {error ? (
        <div className="error-message">{error}</div>
      ) : (
        <LockeRunsTable runs={runs} />
      )}
    </div>
  );
};

export default HomePage; 