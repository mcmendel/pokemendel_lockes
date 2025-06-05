import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import lockeApi from "../api/lockeApi";
import './Run.css';

const Run: React.FC = () => {
  const { runId } = useParams<{ runId: string }>();
  const [run, setRun] = useState<{ id: string, run_name: string } | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!runId) return;
    
    (async () => {
      try {
        const data = await lockeApi.getRun(runId);
        setRun(data);
      } catch (e) {
        setError("Failed to fetch run.");
      }
    })();
  }, [runId]);

  if (!runId) return <p>Error: No run ID provided</p>;
  if (error) return <p>Error: {error}</p>;
  if (!run) return <p>Loading…</p>;

  return (
    <div className="run-container">
      <h1 className="run-title">Run Details</h1>
      <div className="run-id">Run ID: {run.id}</div>
      <div className="run-name">Run Name: {run.run_name}</div>
    </div>
  );
};

export default Run; 