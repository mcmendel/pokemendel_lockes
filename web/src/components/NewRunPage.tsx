import React from 'react';
import { useNavigate } from 'react-router-dom';
import './NewRunPage.css';

const NewRunPage: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="new-run-container">
      <h1>Create New Run</h1>
      <button onClick={() => navigate('/locke_manager')}>Back to Runs</button>
    </div>
  );
};

export default NewRunPage; 