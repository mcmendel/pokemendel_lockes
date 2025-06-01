import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './NewRunPage.css';

const NewRunPage: React.FC = () => {
  const navigate = useNavigate();
  const [runName, setRunName] = useState('');
  const [lockeType, setLockeType] = useState('');

  const lockeTypes = ['Base', 'Nuz'];

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    // TODO: Implement API call to create a new run
    console.log({ runName, lockeType });
    navigate('/locke_manager');
  };

  const handleRefresh = () => {
    const randomIndex = Math.floor(Math.random() * lockeTypes.length);
    setLockeType(lockeTypes[randomIndex]);
  };


  return (
    <div className="new-run-container">
      <h1>Create New Run</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="runName">Run Name:</label>
          <input
            type="text"
            id="runName"
            value={runName}
            onChange={(e) => setRunName(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="lockeType">Choose Locke:</label>
          <div className="locke-select-container">
            <button type="button" onClick={handleRefresh} className="refresh-button" title="Randomize">
              🔄
            </button>
            <select
              id="lockeType"
              value={lockeType}
              onChange={(e) => setLockeType(e.target.value)}
              required
            >
              <option value="">Select a Locke</option>
              {lockeTypes.map((type) => (
                <option key={type} value={type}>
                  {type}
                </option>
              ))}
            </select>
          </div>
        </div>
        <button type="submit">Create Run</button>
      </form>
    </div>
  );
};

export default NewRunPage; 