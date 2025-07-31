import React from 'react';
import Pokemon from './Pokemon';
import { Pokemon as PokemonType } from '../api/lockeApi';
import './ChessLockeBox.css';

interface ChessLockeBoxProps {
  pokemons: Array<PokemonType | null>;
  onPokemonClick: (id: string) => void;
}

interface ChessPosition {
  row: number;
  col: number;
  pokemon: PokemonType | null;
  isBlackSquare: boolean;
}

function ChessLockeBox({ pokemons, onPokemonClick }: ChessLockeBoxProps) {
  // Standard chess piece positions (assuming white pieces at bottom, black at top)
  const getChessPosition = (role: string): { row: number; col: number } | null => {
    switch (role) {
      case 'King':
        return { row: 0, col: 4 }; // e1 position
      case 'Queen':
        return { row: 0, col: 3 }; // d1 position
      case 'Rook':
        // Find first available rook position
        return { row: 0, col: 0 }; // a1 position (will handle second rook in logic)
      case 'Knight':
        return { row: 0, col: 1 }; // b1 position (will handle second knight in logic)
      case 'Bishop':
        return { row: 0, col: 2 }; // c1 position (will handle second bishop in logic)
      case 'Pawn':
        return { row: 1, col: 0 }; // a2 position (will handle other pawns in logic)
      default:
        return null;
    }
  };

  // Create chess board layout
  const createChessBoard = (): ChessPosition[][] => {
    const board: ChessPosition[][] = [];
    
    // Initialize empty board
    for (let row = 0; row < 2; row++) {
      board[row] = [];
      for (let col = 0; col < 8; col++) {
        const isBlackSquare = (row + col) % 2 === 1;
        board[row][col] = {
          row,
          col,
          pokemon: null,
          isBlackSquare
        };
      }
    }

    // Group pokemons by role
    const pokemonsByRole: { [key: string]: PokemonType[] } = {};
    const unassignedPokemons: PokemonType[] = [];

    pokemons.forEach((pokemon) => {
      if (!pokemon) return;
      
      const role = pokemon.metadata.chesslocke_role_og;
      if (role && role !== 'null') {
        if (!pokemonsByRole[role]) {
          pokemonsByRole[role] = [];
        }
        pokemonsByRole[role].push(pokemon);
      } else {
        unassignedPokemons.push(pokemon);
      }
    });

    // Place pieces on board
    Object.entries(pokemonsByRole).forEach(([role, pokemonList]) => {
      pokemonList.forEach((pokemon, index) => {
        let position = getChessPosition(role);
        
        if (position) {
          // Handle multiple pieces of same type
          if (role === 'Rook') {
            position = index === 0 ? { row: 0, col: 0 } : { row: 0, col: 7 };
          } else if (role === 'Knight') {
            position = index === 0 ? { row: 0, col: 1 } : { row: 0, col: 6 };
          } else if (role === 'Bishop') {
            position = index === 0 ? { row: 0, col: 2 } : { row: 0, col: 5 };
          } else if (role === 'Pawn') {
            position = { row: 1, col: index };
          }
          
          if (position.row < 2 && position.col < 8) {
            board[position.row][position.col].pokemon = pokemon;
          }
        }
      });
    });

    return board;
  };

  const chessBoard = createChessBoard();
  const unassignedPokemons = pokemons.filter(pokemon => 
    pokemon && (!pokemon.metadata.chesslocke_role_og || pokemon.metadata.chesslocke_role_og === 'null')
  ) as PokemonType[];

  return (
    <div className="chesslocke-box-container">
      <div className="chesslocke-box-header">
        <span className="chess-icon">♔</span>
        Chess Board
        <span className="chess-icon">♔</span>
      </div>
      
      <div className="chess-board">
        {chessBoard.map((row, rowIndex) => (
          <div key={rowIndex} className="chess-row">
            {row.map((position, colIndex) => (
              <div 
                key={`${rowIndex}-${colIndex}`}
                className={`chess-square ${position.isBlackSquare ? 'black' : 'white'}`}
              >
                {position.pokemon ? (
                  <div className="chess-pokemon-wrapper">
                    <Pokemon 
                      pokemon={position.pokemon}
                      onClick={onPokemonClick}
                      height={120}
                    />
                    <div className="chess-role">
                      {position.pokemon.metadata.chesslocke_role_og}
                    </div>
                  </div>
                ) : (
                  <div className="chess-empty-slot">
                    <span className="chess-piece-placeholder">
                      {position.isBlackSquare ? '⬛' : '⬜'}
                    </span>
                  </div>
                )}
              </div>
            ))}
          </div>
        ))}
      </div>

      {unassignedPokemons.length > 0 && (
        <div className="unassigned-section">
          <div className="unassigned-header">
            <span className="chess-icon">♟️</span>
            Unassigned Pieces
            <span className="chess-icon">♟️</span>
          </div>
          <div className="unassigned-grid">
            {unassignedPokemons.map((pokemon, index) => (
              <div key={index} className="unassigned-pokemon">
                <Pokemon 
                  pokemon={pokemon}
                  onClick={onPokemonClick}
                  height={80}
                />
                <div className="unassigned-label">Unassigned</div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default ChessLockeBox; 