import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import lockeApi from '../api/lockeApi';
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
        <p>Next generation selected successfully</p>
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
  const [gameOptions, setGameOptions] = useState<string[]>([]);
  const [selectedGame, setSelectedGame] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [showSuccess, setShowSuccess] = useState(false);

  useEffect(() => {
    const getNextGenOptions = async () => {
      if (!runId) {
        navigate('/locke_manager');
        return;
      }

      try {
        const response = await lockeApi.nextGen(runId);
        
        if (response.finished) {
          // If the next generation is finished, call getRun API and then redirect to the run page
          await lockeApi.getRun(runId);
          navigate(`/locke_manager/run/${runId}`);
        } else {
          setGameOptions(response.options);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to get next generation options');
      } finally {
        setIsLoading(false);
      }
    };

    getNextGenOptions();
  }, [runId, navigate]);

  const handleGameSelect = async (game: string) => {
    if (!runId) return;
    setSelectedGame(game);
  };

  const handleNext = async () => {
    if (!runId || !selectedGame) return;

    try {
      const response = await lockeApi.nextGen(runId, selectedGame);
      
      if (response.finished) {
        setShowSuccess(true);
      } else {
        // If not finished, update the options (though this shouldn't happen in normal flow)
        setGameOptions(response.options);
        setSelectedGame(null);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to select next generation');
    }
  };

  const handleRandomSelect = () => {
    if (gameOptions.length === 0) return;
    const randomIndex = Math.floor(Math.random() * gameOptions.length);
    setSelectedGame(gameOptions[randomIndex]);
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
        <div className="continue-run-loading">Loading next generation options...</div>
      </div>
    );
  }

  return (
    <div className="continue-run-container">
      {showSuccess && runId && (
        <SuccessPopup runId={runId} onClose={handleSuccessClose} />
      )}
      <h1 className="continue-run-title">Select Next Generation:</h1>
      <h1 className="continue-run-id">Run ID: {runId}</h1>
      {error && <div className="continue-run-error">{error}</div>}
      {gameOptions.length > 0 && (
        <div className="continue-run-step">
          <h2>Choose your next game:</h2>
          <div className="continue-run-values">
            {gameOptions.map((game) => (
              <button
                key={game}
                onClick={() => handleGameSelect(game)}
                className={`continue-run-value-button ${selectedGame === game ? 'selected' : ''}`}
              >
                {game}
              </button>
            ))}
          </div>
          <div className="continue-run-button-group">
            <button 
              className="continue-run-next-button"
              onClick={handleNext}
              disabled={!selectedGame}
            >
              Continue to Next Generation
            </button>
            <button 
              className="continue-run-refresh-button"
              onClick={handleRandomSelect}
              title="Randomly select a game"
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
              Randomized
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ContinueRun;
