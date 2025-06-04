import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import lockeApi, { RunUpdateResponse } from '../api/lockeApi';
import './RunConfiguration.css';

const RunConfiguration: React.FC = () => {
  const navigate = useNavigate();
  const { runName } = useParams<{ runName: string }>();
  const [error, setError] = useState<string | null>(null);
  const [nextKey, setNextKey] = useState<string | null>(null);
  const [potentialValues, setPotentialValues] = useState<string[]>([]);
  const [selectedValue, setSelectedValue] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const continueCreation = async () => {
      if (!runName) {
        navigate('/locke_manager');
        return;
      }

      try {
        const response = await lockeApi.continueRunCreation({
          run_name: runName
        });
        
        if (response.finished) {
          navigate('/locke_manager');
        } else {
          setNextKey(response.next_key);
          setPotentialValues(response.potential_values);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to continue run creation');
      } finally {
        setIsLoading(false);
      }
    };

    continueCreation();
  }, [runName, navigate]);

  const handleValueSelect = async (value: string) => {
    if (!runName || !nextKey) return;
    setSelectedValue(value);
  };

  const handleNext = async () => {
    if (!runName || !nextKey || !selectedValue) return;

    try {
      const response = await lockeApi.continueRunCreation({
        run_name: runName,
        key: nextKey,
        val: selectedValue
      });
      
      if (response.finished) {
        navigate('/locke_manager');
      } else {
        setNextKey(response.next_key);
        setPotentialValues(response.potential_values);
        setSelectedValue(null);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to continue run creation');
    }
  };

  const handleRandomSelect = () => {
    if (potentialValues.length === 0) return;
    const randomIndex = Math.floor(Math.random() * potentialValues.length);
    setSelectedValue(potentialValues[randomIndex]);
  };

  if (isLoading) {
    return (
      <div className="run-configuration-container">
        <div className="run-configuration-loading">Loading run configuration...</div>
      </div>
    );
  }

  return (
    <div className="run-configuration-container">
      <h1 className="run-configuration-title">Configure Run:</h1>
      <h1 className="run-configuration-name">{runName}</h1>
      {error && <div className="run-configuration-error">{error}</div>}
      {nextKey && (
        <div className="run-configuration-step">
          <h2>Next Step: {nextKey}</h2>
          <div className="run-configuration-values">
            {potentialValues.map((value) => (
              <button
                key={value}
                onClick={() => handleValueSelect(value)}
                className={`run-configuration-value-button ${selectedValue === value ? 'selected' : ''}`}
              >
                {value}
              </button>
            ))}
          </div>
          <div className="run-configuration-button-group">
            <button 
              className="run-configuration-next-button"
              onClick={handleNext}
              disabled={!selectedValue}
            >
              Next
            </button>
            <button 
              className="run-configuration-refresh-button"
              onClick={handleRandomSelect}
              title="Randomly select an option"
            >
              <svg 
                xmlns="http://www.w3.org/2000/svg" 
                width="24" 
                height="24" 
                viewBox="0 0 24 24" 
                fill="none" 
                stroke="currentColor" 
                strokeWidth="2" 
                strokeLinecap="round" 
                strokeLinejoin="round"
              >
                <path d="M23 4v6h-6"/>
                <path d="M1 20v-6h6"/>
                <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/>
              </svg>
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default RunConfiguration; 