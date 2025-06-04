import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import lockeApi from '../api/lockeApi';
import './NewRunPage.css';

const NewRunPage: React.FC = () => {
  const navigate = useNavigate();
  const [runName, setRunName] = useState('');
  const [lockeType, setLockeType] = useState('');
  const [duplicateClause, setDuplicateClause] = useState(false);
  const [isRandomized, setIsRandomized] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [validationErrors, setValidationErrors] = useState<{
    runName?: string;
    lockeType?: string;
  }>({});
  const [lockes, setLockes] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchLockes = async () => {
      try {
        const lockeTypes = await lockeApi.getLockes();
        setLockes(lockeTypes);
      } catch (err) {
        setError('Failed to load locke types. Please try again later.');
      } finally {
        setIsLoading(false);
      }
    };

    fetchLockes();
  }, []);

  const validateForm = (): boolean => {
    const errors: { runName?: string; lockeType?: string } = {};
    let isValid = true;

    if (!runName.trim()) {
      errors.runName = 'Run name is required';
      isValid = false;
    }

    if (!lockeType) {
      errors.lockeType = 'Please select a Locke type';
      isValid = false;
    }

    setValidationErrors(errors);
    return isValid;
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setError(null);
    setValidationErrors({});

    if (!validateForm()) {
      return;
    }

    try {
      await lockeApi.createRun({
        run_name: runName.trim(),
        locke_type: lockeType,
        duplicate_clause: duplicateClause,
        is_randomized: isRandomized
      });

      // Navigate to the continue creation page
      navigate(`/new/${runName.trim()}`);
    } catch (err: unknown) {
      const error = err as { response?: { status?: number } };
      if (error.response?.status === 409) {
        // Run already exists, navigate to continue creation
        navigate(`/new/${runName.trim()}`);
      } else {
        setError(err instanceof Error ? err.message : 'Failed to create run');
      }
    }
  };

  const handleRefresh = () => {
    if (lockes.length === 0) return;
    const randomIndex = Math.floor(Math.random() * lockes.length);
    setLockeType(lockes[randomIndex]);
    if (validationErrors.lockeType) {
      setValidationErrors(prev => ({ ...prev, lockeType: undefined }));
    }
  };

  return (
    <div className="new-run-container">
      <h1>Create New Run</h1>
      {error && <div className="error-message">{error}</div>}
      <form onSubmit={handleSubmit} noValidate>
        <div>
          <label htmlFor="runName">Run Name:</label>
          <input
            type="text"
            id="runName"
            value={runName}
            onChange={(e) => {
              setRunName(e.target.value);
              if (validationErrors.runName) {
                setValidationErrors(prev => ({ ...prev, runName: undefined }));
              }
            }}
            className={validationErrors.runName ? 'error' : ''}
          />
          {validationErrors.runName && (
            <div className="validation-error">{validationErrors.runName}</div>
          )}
        </div>
        <div>
          <label htmlFor="lockeType">Choose Locke:</label>
          <div className="locke-select-container">
            <button 
              type="button" 
              onClick={handleRefresh} 
              className="refresh-button" 
              title="Randomize"
              disabled={isLoading || lockes.length === 0}
            >
              🔄
            </button>
            <select
              id="lockeType"
              value={lockeType}
              onChange={(e) => {
                setLockeType(e.target.value);
                if (validationErrors.lockeType) {
                  setValidationErrors(prev => ({ ...prev, lockeType: undefined }));
                }
              }}
              className={validationErrors.lockeType ? 'error' : ''}
              disabled={isLoading}
            >
              <option value="">Select a Locke</option>
              {lockes.map((lockeName) => (
                <option key={`locke-${lockeName}`} value={lockeName}>
                  {lockeName}
                </option>
              ))}
            </select>
          </div>
          {validationErrors.lockeType && (
            <div className="validation-error">{validationErrors.lockeType}</div>
          )}
          {isLoading && <div className="loading-message">Loading locke types...</div>}
        </div>
        <div className="checkbox-group">
          <div>
            <label htmlFor="duplicateClause">
              <input
                type="checkbox"
                id="duplicateClause"
                checked={duplicateClause}
                onChange={(e) => setDuplicateClause(e.target.checked)}
              />
              Duplicate Clause
            </label>
          </div>
          <div>
            <label htmlFor="isRandomized">
              <input
                type="checkbox"
                id="isRandomized"
                checked={isRandomized}
                onChange={(e) => setIsRandomized(e.target.checked)}
              />
              Randomized Run
            </label>
          </div>
        </div>
        <button type="submit" disabled={isLoading}>Start Run Creation</button>
      </form>
    </div>
  );
};

export default NewRunPage; 