# AQ3D API Wrapper for Python

A Python package providing a comprehensive, object-oriented interface to the AdventureQuest 3D (AQ3D) game API. This library allows you to fetch, filter, and manage data for servers, items, maps, and dialogs from AQ3D.

_This package is under development which means it's not in a usable state.
Technically you can use it, but without future implementation of async processes,
it's not going to be ideal._

### API Coverage

- **Servers**
  - Retrieve server statistics (player counts, status, etc.)
  - Capture timestamped server snapshots for logging or analytics.

- **Items (Supports Ranges)**
  - Fetch items by ID range from the API
  - Filter items by type, equip type, rarity, or attribute key

- **Maps (Supports Ranges)**
  - Fetch maps/dungeons by ID range
  - Filter maps by attribute key

- **Dialogs (Supports Ranges)**
  - Fetch dialogs by ID range
  - Access dialog frames and actors (NPCs)

- **Auto-Update Support**
  - Containers can auto-refresh their data from the API at configurable intervals


Save data CSV and JSON files with a single method either
`to_csv(Path)` or `to_json_file(Path)` on the container objects.


## TODOs

- Refactor all HTTP requests to use async for non-blocking operations.
- API for more types
  - **NPCs**
  - **Dialog Image Generator**
  - **Class Skills**
  - **Spells & Skills**
  - **Loot Box Items**
  - **Character Info (Name, Level, Class, Badges)**
  - **Daily Map**
- Filter Items by category.
- Create a wiki on here to explain how to use the package.


## How To Use

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ColemanMaximus/aq3d-api.git
    cd aq3d-api
    ```

2. Install dependencies:
    Using Pipenv:
    ```sh
    pipenv install
    ```

### Example Usages

#### Example: Fetching and Exporting Items
```python
from pathlib import Path
from aq3d_api.containers.items import Items
from aq3d_api.enums.item_rarity import ItemRarity
from aq3d_api import utils

# Fetch items with IDs 300-600 from the API
items = Items({
    "min-index": 1,
    "max-index": 150,
    "auto-update": True,
    "update-interval": 1000 # 1000 Seconds
})

# Export all items to CSV and JSON
items.to_csv(Path("items.csv"))
items.to_json_file(Path("items.json"))

# Filter for legendary items and export to JSON
legendary_items = items.by_type(ItemRarity.LEGENDARY)
utils.to_json_file(list(legendary_items), Path("legendary.json"))
```

#### Example: Fetching server data and creating snapshots of all servers.
```python
from aq3d_api.containers.servers import Servers

servers = Servers({
    "auto-update": True,
    "update-interval": 60 # 60 Seconds
})
server_snapshots = servers.create_snapshots()
```

---

_This project is intended for learning and research purposes.
Please use fairly and respect the terms and conditions of
Artix Entertainment._
