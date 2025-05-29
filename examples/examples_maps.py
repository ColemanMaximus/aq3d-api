import sys
sys.path.append(".")

from pathlib import Path

from aq3d_api import utils
from aq3d_api.containers.maps import Maps


def get_maps(min_index: int = 1, max_index: int = 1, bulk_max: int = 200):
    # Creates a Maps instance which creates a bundle of maps based on
    # the min and max index ranges.
    return Maps({
        "min-index": min_index,
        "max-index": max_index
    })


if __name__ == "__main__":
    # Create a Maps object with map IDs between 1 and 300.
    maps = get_maps(1, 50)
    # Update the maps container at least once to gather the API data.
    maps.update()

    # Save maps to either a CSV file or JSON file.
    maps.to_csv(Path("./examples/maps.csv"))
    maps.to_json_file(Path("./examples/maps.json"))

    # All items which are cosmetic.
    dungeons = maps.maps_by_keypair("dungeon", True)

    # Save all those dungeons to a json file.
    utils.to_json_file(list(dungeons), Path("dungeons.json"))
