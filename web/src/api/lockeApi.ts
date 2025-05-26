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

    // Add more API methods here as needed
};

export default lockeApi; 