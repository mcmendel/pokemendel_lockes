# MongoDB Sync Script

This script syncs all Pokemon Locke Manager collections between local and remote MongoDB.

## Collections Synced

- `runs` - Main run data
- `runs_save` - Run save states
- `pokemons` - Pokemon data
- `pokemons_save` - Pokemon save states
- `run_creation` - Run creation/configuration data
- `runs_pokemons_options` - Pokemon options for runs
- `runs_reports` - Run reports/statistics

## Usage

### Basic sync (all collections):
```bash
python backend/scripts/sync_mongodb.py
```

### Dry run (see what would be synced without actually syncing):
```bash
python backend/scripts/sync_mongodb.py --dry-run
```

### Sync specific collections:
### Sync from remote to local:
```bash
python backend/scripts/sync_mongodb.py --reverse
```

### Sync from remote to local (dry run):
```bash
python backend/scripts/sync_mongodb.py --reverse --dry-run
``````bash
python backend/scripts/sync_mongodb.py --collections runs,pokemons
```

### Provide password via command line:
```bash
python backend/scripts/sync_mongodb.py --password your_password
```

### Provide password via environment variable:
```bash
export MONGODB_PASSWORD=your_password
python backend/scripts/sync_mongodb.py
```

## Configuration

- **Local MongoDB**: `mongodb://localhost:27017/`
- **Remote MongoDB**: `mongodb+srv://mcmendel_db_user:<password>@mcmendel-locke-manager.3ynuh71.mongodb.net/`
- **Database**: `locke_manager`

## Important Notes

⚠️ **WARNING**: This script will **completely replace** the data in the remote collections with the data from local collections. Make sure you have backups if needed.

The script will:
1. Connect to both local and remote MongoDB instances
2. Clear the target collections on remote
3. Copy all documents from local to remote
4. Provide detailed logging and statistics

## Logging

The script creates a log file `mongodb_sync.log` with detailed information about the sync process.
