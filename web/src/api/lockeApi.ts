import axios from 'axios';

const API_BASE_URL = 'http://localhost:5222/locke_manager';

// Types
export interface Run {
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

export interface RunUpdateResponse {
    next_key: string;
    potential_values: string[];
    finished: boolean;
    run_id: string | null;
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
    getRuns: async (): Promise<Run[]> => {
        try {
            const response = await axios.get<Run[]>(`${API_BASE_URL}/runs`);
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
};

export default lockeApi; 