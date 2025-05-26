from models.run import list_runs
from responses.list_runs import ListRuns

def list_runs_api() -> list[ListRuns]:
    """Get a list of all runs from the database.
    
    Returns:
        A list of ListRuns response objects containing run information.
        
    Raises:
        Exception: If there's an error fetching runs from the database.
    """
    runs = list_runs()
    return [ListRuns.from_run(run) for run in runs]
