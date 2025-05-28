import sys
sys.path.append(".")

from pathlib import Path

from aq3d_api import utils
from aq3d_api.containers.maps import Maps


def get_maps(min_index: int = 1, max_index: int = 1, bulk_max: int = 200):
    # Creates a Maps instance which creates a bundle of maps based on
    # the min and max index ranges.
    return Maps(fromapi = True,
                api_maps_min = min_index,
                api_maps_max = max_index)


if __name__ == "__main__":
    # Create a Maps object with map IDs between 1 and 300.
    maps = get_maps(1, 300)

    # Save maps to either a CSV file or JSON file.
    maps.to_csv(Path("maps.csv"))
    maps.to_json_file(Path("maps.json"))

    # All items which are cosmetic.
    dungeons = maps.maps_by_keypair("dungeon", True)

    # Save all those dungeons to a json file.
    utils.to_json_file(list(dungeons), Path("dungeons.json"))
