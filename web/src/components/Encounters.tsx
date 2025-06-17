import React from 'react';
import './Encounters.css';

interface EncountersProps {
  // Add props here when needed
}

function Encounters({}: EncountersProps) {
  return (
    <div className="encounters-container">
      <div className="encounters-header">Encounters</div>
      <div className="encounters-content">
        {/* Content will go here */}
      </div>
    </div>
  );
}

export default Encounters; 