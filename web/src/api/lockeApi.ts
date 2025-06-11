import axios from 'axios';

const API_BASE_URL = 'http://localhost:5222/locke_manager';

// Types
export interface ListRun {
    run_id: string;
    run_name: string;
    created_at: string;
    finished: boolean;
    game_name: string;
    locke_name: string;
    num_deaths: number;
    num_gyms: number;
    num_pokemons: number;
    num_restarts: number;
    randomized: boolean;
    starter: string;
}

export interface Run {
    id: string;
    run_name: string;
    created_at: string;
    finished: boolean;
    game_name: string;
    locke_name: string;
    num_deaths: number;
    num_gyms: number;
    num_pokemons: number;
    num_restarts: number;
    randomized: boolean;
    starter: string | null;
}

export interface RunUpdateResponse {
    next_key: string;
    potential_values: string[];
    finished: boolean;
    id: string | null;
}

export interface CreateRunRequest {
    run_name: string;
    locke_type: string;
    duplicate_clause: boolean;
    is_randomized: boolean;
}

export interface ContinueRunRequest {
    run_name: string;
    key?: string;
    val?: string;
}

export interface Locke {
    name: string;
    description: string;
    min_gen: number;
}

// API Client
const lockeApi = {
    // Get all runs
    getRuns: async (): Promise<ListRun[]> => {
        try {
            const response = await axios.get<ListRun[]>(`${API_BASE_URL}/runs`);
            return response.data;
        } catch (error) {
            console.error('Error fetching runs:', error);
            throw error;
        }
    },

    // Create a new run
    createRun: async (request: CreateRunRequest): Promise<string[]> => {
        try {
            const response = await axios.put<string[]>(`${API_BASE_URL}/run`, request);
            return response.data;
        } catch (error) {
            console.error('Error creating run:', error);
            throw error;
        }
    },

    // Get all available locke types
    getLockes: async (): Promise<string[]> => {
        try {
            const response = await axios.get<string[]>(`${API_BASE_URL}/lockes`);
            return response.data;
        } catch (error) {
            console.error('Error fetching locke types:', error);
            throw error;
        }
    },

    // Continue run creation
    continueRunCreation: async (request: ContinueRunRequest): Promise<RunUpdateResponse> => {
        try {
            const response = await axios.post<RunUpdateResponse>(`${API_BASE_URL}/run`, request);
            return response.data;
        } catch (error) {
            console.error('Error continuing run creation:', error);
            throw error;
        }
    },

    // Add more API methods here as needed

    async getRun(runId: string): Promise<Run> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}`, { method: "GET" });
        if (!response.ok) {
            throw new Error("Failed to fetch run");
        }
        return response.json();
    },

    async saveRun(runId: string): Promise<{ status: string }> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}/save`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`Failed to save run: ${response.statusText}`);
        }

        return response.json();
    },

    async loadRun(runId: string): Promise<Run> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}/load`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`Failed to load run: ${response.statusText}`);
        }

        return response.json();
    },

    async finishRun(runId: string): Promise<Run> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}/finish`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`Failed to finish run: ${response.statusText}`);
        }

        return response.json();
    },

    async getStarterOptions(runId: string): Promise<string[]> {
        try {
            const response = await fetch(`${API_BASE_URL}/run/${runId}/starter_options`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching starter options:', error);
            throw error;
        }
    },

    getPokemonImageUrl(pokemonName: string): string {
        return `${API_BASE_URL}/resources/pokemon/${pokemonName.toLowerCase()}.png`;
    }
};

export default lockeApi; 