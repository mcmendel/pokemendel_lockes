import React from 'react';
import { useParams } from 'react-router-dom';
import './Run.css';

const Run: React.FC = () => {
  const { runId } = useParams<{ runId: string }>();

  return (
    <div className="run-container">
      <h1 className="run-title">Run Details</h1>
      <div className="run-id">Run ID: {runId}</div>
    </div>
  );
};

export default Run; 