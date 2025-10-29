from definitions import Pokemon
from definitions.runs.steps_interface import ExecutionReturnValue, StepInterface
from definitions.runs.inputs_options import InputOptions
from pokemendel_core.utils.definitions.genders import Genders
from models.run_pokemons_options import list_runs_options_by_query
from core.lockes.chess.utils import ChessRoles
from core.run import Run
from typing import Tuple, List, Optional, Dict, Set
from collections import defaultdict


class SetChessRoleStep(StepInterface):
    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        has_role = bool(pokemon.metadata.chesslocke_role)
        is_pawn = pokemon.metadata.chesslocke_role == ChessRoles.PAWN
        promoted_pawn = bool(
            pokemon.metadata.chesslocke_role_og == ChessRoles.PAWN and
            self._is_promoted_pawn(pokemon)
        )
        return (
            not has_role or all([is_pawn, not promoted_pawn])
        ) and pokemon.metadata.gender

    def step_options(self, run: Run, pokemon: Pokemon, is_randomized: bool) -> Tuple[InputOptions, List[str]]:
        if pokemon.compare_pokemon(run.starter):
            return InputOptions.ONE_OF, [ChessRoles.KING]

        open_roles = (
            {
                role for role in self._roles_quotas()
                if role != ChessRoles.PAWN
            }
            if pokemon.metadata.chesslocke_role_og == ChessRoles.PAWN
            else self._get_open_roles(run)
        )
        if pokemon.metadata.gender != Genders.FEMALE and ChessRoles.QUEEN in open_roles:
            open_roles.remove(ChessRoles.QUEEN)
        if ChessRoles.PAWN in open_roles:
            base_pokemon = list_runs_options_by_query(run_id=run.id, query={'pokemon_name': pokemon.name})[0].base_pokemon
            if base_pokemon != pokemon.name:
                open_roles.remove(ChessRoles.PAWN)
        return InputOptions.ONE_OF, list(open_roles)

    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        pokemon.metadata.chesslocke_role = value
        if not pokemon.metadata.chesslocke_role_og:
            pokemon.metadata.chesslocke_role_og = value
        return ExecutionReturnValue(pokemons_to_update=[pokemon.metadata.id])

    def _is_promoted_pawn(self, pokemon: Pokemon) -> bool:
        return (
            pokemon.metadata.chesslocke_role_og == ChessRoles.PAWN and
            pokemon.metadata.chesslocke_role != ChessRoles.PAWN
        )

    def _get_open_roles(self, run: Run) -> Set[str]:
        current_roles_mapping = self._map_current_roles(run)
        roles_quotas = self._roles_quotas()
        return {
            role for role in roles_quotas.keys()
            if roles_quotas[role] - current_roles_mapping[role] > 0
        }

    def _map_current_roles(self, run: Run) -> Dict[str, int]:
        roles_mapping = defaultdict(int)
        for pokemon in run.box.pokemons:
            if pokemon.metadata.chesslocke_role_og:
                roles_mapping[pokemon.metadata.chesslocke_role_og] += 1
        return roles_mapping

    def _roles_quotas(self) -> Dict[str, int]:
        return {
            ChessRoles.QUEEN: 1,
            ChessRoles.BISHOP: 2,
            ChessRoles.KNIGHT: 2,
            ChessRoles.ROOK: 2,
            ChessRoles.PAWN: 8,
        }


