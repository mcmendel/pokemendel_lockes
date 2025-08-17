import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import lockeApi, { RunUpdateResponse } from '../api/lockeApi';
import './ContinueRun.css';

interface SuccessPopupProps {
  runId: string;
  onClose: () => void;
}

const SuccessPopup: React.FC<SuccessPopupProps> = ({ runId, onClose }) => {
  return (
    <div className="continue-run-popup-overlay">
      <div className="continue-run-popup">
        <h2>Success!</h2>
        <p>Run continued successfully</p>
        <button 
          className="continue-run-popup-button"
          onClick={onClose}
        >
          OK
        </button>
      </div>
    </div>
  );
};

const ContinueRun: React.FC = () => {
  const navigate = useNavigate();
  const { runId } = useParams<{ runId: string }>();
  const [error, setError] = useState<string | null>(null);
  const [nextKey, setNextKey] = useState<string | null>(null);
  const [potentialValues, setPotentialValues] = useState<string[]>([]);
  const [selectedValue, setSelectedValue] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [showSuccess, setShowSuccess] = useState(false);

  useEffect(() => {
    const continueRun = async () => {
      if (!runId) {
        navigate('/locke_manager');
        return;
      }

      try {
        const response = await lockeApi.continueRun(runId);
        
        if (response.finished) {
          // If the run is finished, redirect to the run page
          navigate(`/locke_manager/run/${runId}`);
        } else {
          setNextKey(response.next_key);
          setPotentialValues(response.potential_values);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to continue run');
      } finally {
        setIsLoading(false);
      }
    };

    continueRun();
  }, [runId, navigate]);

  const handleValueSelect = async (value: string) => {
    if (!runId || !nextKey) return;
    setSelectedValue(value);
  };

  const handleNext = async () => {
    if (!runId || !nextKey || !selectedValue) return;

    try {
      const response = await lockeApi.continueRun(runId, {
        key: nextKey,
        val: selectedValue
      });
      
      if (response.finished) {
        setShowSuccess(true);
      } else {
        setNextKey(response.next_key);
        setPotentialValues(response.potential_values);
        setSelectedValue(null);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to continue run');
    }
  };

  const handleRandomSelect = () => {
    if (potentialValues.length === 0) return;
    const randomIndex = Math.floor(Math.random() * potentialValues.length);
    setSelectedValue(potentialValues[randomIndex]);
  };

  const handleSuccessClose = () => {
    setShowSuccess(false);
    if (runId) {
      navigate(`/locke_manager/run/${runId}`);
    }
  };

  if (isLoading) {
    return (
      <div className="continue-run-container">
        <div className="continue-run-loading">Loading run continuation...</div>
      </div>
    );
  }

  return (
    <div className="continue-run-container">
      {showSuccess && runId && (
        <SuccessPopup runId={runId} onClose={handleSuccessClose} />
      )}
      <h1 className="continue-run-title">Continue Run:</h1>
      <h1 className="continue-run-id">Run ID: {runId}</h1>
      {error && <div className="continue-run-error">{error}</div>}
      {nextKey && (
        <div className="continue-run-step">
          <h2>Next Step: {nextKey}</h2>
          <div className="continue-run-values">
            {potentialValues.map((value) => (
              <button
                key={value}
                onClick={() => handleValueSelect(value)}
                className={`continue-run-value-button ${selectedValue === value ? 'selected' : ''}`}
              >
                {value}
              </button>
            ))}
          </div>
          <div className="continue-run-button-group">
            <button 
              className="continue-run-next-button"
              onClick={handleNext}
              disabled={!selectedValue}
            >
              Next
            </button>
            <button 
              className="continue-run-refresh-button"
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

export default ContinueRun; 