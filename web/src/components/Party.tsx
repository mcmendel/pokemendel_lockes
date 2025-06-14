import React from 'react';
import './Party.css';

interface PartyProps {
  pokemonCount: number;
}

function Party({ pokemonCount }: PartyProps) {
  const partyItems = Array.from({ length: 6 }, (_, i) => i + 1);

  return (
    <div className="party-container">
      <div className="party-header">Party</div>
      <div className="party-content">
        {partyItems.map((itemNumber) => (
          <div key={itemNumber} className="party-item">
            Item {itemNumber} in party
          </div>
        ))}
      </div>
    </div>
  );
}

export default Party; 