import React, { useEffect, useState } from 'react';
import lockeApi from '../api/lockeApi';
import './ShowdownGeneration.css';

const ShowdownGeneration: React.FC = () => {
  const [generations, setGenerations] = useState<number[]>([]);
  const [pokemons, setPokemons] = useState<string[]>([]);
  const [gen, setGen] = useState<number | ''>('');
  const [pokemonName, setPokemonName] = useState('');
  const [nickname, setNickname] = useState('');
  const [item, setItem] = useState('');
  const [result, setResult] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    lockeApi.getShowdownGenerations()
      .then(setGenerations)
      .catch(() => setError('Failed to load generations'));
  }, []);

  useEffect(() => {
    if (gen === '') {
      setPokemons([]);
      setPokemonName('');
      return;
    }
    setPokemonName('');
    lockeApi.getShowdownPokemons(gen)
      .then(setPokemons)
      .catch(() => setError('Failed to load Pokémon list'));
  }, [gen]);

  const handleGenerate = async () => {
    if (gen === '' || !pokemonName) return;
    setError(null);
    setLoading(true);
    try {
      const showdown = await lockeApi.generateShowdown(gen, pokemonName, nickname, item);
      setResult(showdown);
    } catch (err) {
      setError('Failed to generate Showdown format');
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = async () => {
    await navigator.clipboard.writeText(result);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="showdown-container">
      <h1>Showdown Generation</h1>
      {error && <div className="error-message">{error}</div>}
      <div className="showdown-form">
        <div className="form-group">
          <label htmlFor="gen">Generation</label>
          <select
            id="gen"
            value={gen}
            onChange={(e) => setGen(e.target.value ? Number(e.target.value) : '')}
          >
            <option value="">Select generation</option>
            {generations.map((g) => (
              <option key={g} value={g}>Gen {g}</option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="pokemon">Pokémon</label>
          <select
            id="pokemon"
            value={pokemonName}
            onChange={(e) => setPokemonName(e.target.value)}
            disabled={pokemons.length === 0}
          >
            <option value="">Select Pokémon</option>
            {pokemons.map((p) => (
              <option key={p} value={p}>{p}</option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="nickname">Nickname (optional)</label>
          <input
            id="nickname"
            type="text"
            value={nickname}
            onChange={(e) => setNickname(e.target.value)}
            placeholder="e.g. Carina"
          />
        </div>

        <div className="form-group">
          <label htmlFor="item">Item (optional)</label>
          <input
            id="item"
            type="text"
            value={item}
            onChange={(e) => setItem(e.target.value)}
            placeholder="e.g. Fire Stone"
          />
        </div>

        <button
          className="generate-button"
          onClick={handleGenerate}
          disabled={gen === '' || !pokemonName || loading}
        >
          {loading ? 'Generating...' : 'Generate'}
        </button>
      </div>

      {result && (
        <div className="showdown-result">
          <div className="result-header">
            <h2>Showdown Export</h2>
            <button className="copy-button" onClick={handleCopy}>
              {copied ? 'Copied!' : 'Copy'}
            </button>
          </div>
          <pre className="showdown-output">{result}</pre>
        </div>
      )}
    </div>
  );
};

export default ShowdownGeneration;
