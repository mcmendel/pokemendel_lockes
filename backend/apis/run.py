from typing import List
from models.run import fetch_run
from games import get_game
from core.lockes import LOCKE_INSTANCES
from core.run import convert_db_run_to_core_run
from core.run_manager import RunManager


def _get_run_manager(run_id: str) -> RunManager:
    db_run = fetch_run(run_id)
    run = convert_db_run_to_core_run(db_run, run_id)
    game = get_game(db_run.game)
    locke = LOCKE_INSTANCES[db_run.locke]
    run_manager = RunManager(
        run=run,
        locke=locke,
        game=game,
        duplicate_clause=db_run.duplicate_clause,
        randomized=db_run.randomized,
    )
    return run_manager


def get_starter_options(run_id: str) -> List[str]:
    run_manager = _get_run_manager(run_id)
    return run_manager.get_starter_options()
