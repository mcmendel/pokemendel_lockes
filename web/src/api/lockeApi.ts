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

export interface BattleResponse {
    leader: string;
    won: boolean;
}

export interface EncounterResponse {
    route: string;
    pokemon: string | null;
    status: string;
}

export interface Run {
    id: string;
    run_name: string;
    creation_date: string;
    party: string[];
    box: string[];
    gyms: BattleResponse[];
    elite4: BattleResponse[];
    encounters: EncounterResponse[];
    starter: string | null;
    restarts: number;
    finished: boolean;
    rules: string[];
    main_battles: string[];
}

export interface PokemonMetadata {
    id: string;
    nickname: string | null;
    caught_index: number | null;
    starlocke_type: string | null;
    gender: string | null;
    paired: string | null;
}

export interface Pokemon {
    name: string;
    metadata: PokemonMetadata;
    status: string;
    gen: number;
    types: number[];
    categories: string[];
    colors: string[];
    evolves_to: string[];
    num_legs: number;
    stats: any | null;  // TODO: Define proper stats type if needed
    supported_genders: string[];
}

export interface RunResponse {
    run: Run;
    pokemons: Record<string, Pokemon>;
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

export interface StatusResponse {
    status: string;
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

    async getRun(runId: string): Promise<RunResponse> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}`, { method: "GET" });
        if (!response.ok) {
            throw new Error("Failed to fetch run");
        }
        const data: RunResponse = await response.json();
        console.log('Run response:', data);
        return data;
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

    async loadRun(runId: string): Promise<RunResponse> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}/load`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`Failed to load run: ${response.statusText}`);
        }

        const data: RunResponse = await response.json();
        console.log('Load run response:', data);
        return data;
    },

    async finishRun(runId: string): Promise<RunResponse> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}/finish`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`Failed to finish run: ${response.statusText}`);
        }

        const data: RunResponse = await response.json();
        console.log('Finish run response:', data);
        return data;
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
    },

    getGymLeaderImageUrl(gameName: string, gymName: string): string {
        return `${API_BASE_URL}/resources/game/${gameName}/gyms/${gymName}`;
    },

    async setStarter(runId: string, pokemonName: string): Promise<StatusResponse> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}/starter`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ pokemon_name: pokemonName })
        });

        if (!response.ok) {
            throw new Error(`Failed to set starter: ${response.statusText}`);
        }

        const data: StatusResponse = await response.json();
        console.log('Set starter response:', data);
        return data;
    },

    async getPotentialPokemons(runId: string): Promise<string[]> {
        try {
            const response = await fetch(`${API_BASE_URL}/run/${runId}/potential_pokemons`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching potential pokemons:', error);
            throw error;
        }
    },

    async getEncounters(runId: string, route?: string): Promise<string[]> {
        try {
            const url = new URL(`${API_BASE_URL}/run/${runId}/encounters`);
            if (route) {
                url.searchParams.append('route', route);
            }
            
            const response = await fetch(url.toString());
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching encounters:', error);
            throw error;
        }
    },

    async setEncounter(runId: string, route: string, pokemonName: string): Promise<StatusResponse> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}/encounter/${route}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ pokemon_name: pokemonName })
        });

        if (!response.ok) {
            throw new Error(`Failed to set encounter: ${response.statusText}`);
        }

        const data: StatusResponse = await response.json();
        console.log('Set encounter response:', data);
        return data;
    },

    async updateEncounterStatus(runId: string, route: string, encounterStatus: string): Promise<StatusResponse> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}/encounter/${route}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ encounter_status: encounterStatus })
        });

        if (!response.ok) {
            throw new Error(`Failed to update encounter status: ${response.statusText}`);
        }

        const data: StatusResponse = await response.json();
        console.log('Update encounter status response:', data);
        return data;
    },

    async markGymWon(runId: string, leader: string): Promise<StatusResponse> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}/battle/${leader}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`Failed to mark gym victory: ${response.statusText}`);
        }

        const data: StatusResponse = await response.json();
        console.log('Mark gym won response:', data);
        return data;
    },

    async getPokemonActions(runId: string, pokemonId: string): Promise<string[]> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}/pokemon/${pokemonId}/actions`);

        if (!response.ok) {
            throw new Error(`Failed to fetch pokemon actions: ${response.statusText}`);
        }

        const data: string[] = await response.json();
        console.log('Pokemon actions response:', data);
        return data;
    },

    async getPokemonActionInfo(runId: string, pokemonId: string, actionName: string): Promise<{input_type: string, input_options: string[]}> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}/pokemon/${pokemonId}/action?action=${encodeURIComponent(actionName)}`);

        if (!response.ok) {
            throw new Error(`Failed to fetch pokemon action info: ${response.statusText}`);
        }

        const data: {input_type: string, input_options: string[]} = await response.json();
        console.log('Pokemon action info response:', data);
        return data;
    },

    async executePokemonAction(runId: string, pokemonId: string, action: string, value: string): Promise<StatusResponse> {
        const response = await fetch(`${API_BASE_URL}/run/${runId}/pokemon/${pokemonId}/action`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ action, value })
        });

        if (!response.ok) {
            const error = new Error(`Failed to execute pokemon action: ${response.statusText}`);
            (error as any).status = response.status;
            throw error;
        }

        const data: StatusResponse = await response.json();
        console.log('Execute pokemon action response:', data);
        return data;
    },
};

export default lockeApi; 