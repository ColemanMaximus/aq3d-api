import sys
sys.path.append(".")

from pathlib import Path

from aq3d_api import utils
from aq3d_api.enums.item_rarity import ItemRarity
from aq3d_api.containers.items import Items
from aq3d_api.enums.item_type import ItemType


def get_items(min_index: int, max_index: int):
    # Creates an Items instance which creates a bundle of items based on
    # the min and max index ranges.
    return Items(fromapi = True,
                 api_items_min = min_index,
                 api_items_max = max_index)


if __name__ == "__main__":
    # Create an Items object with item IDs between 300 and 600.
    items = get_items(300, 600)

    # Save items to either a CSV file or JSON file.
    items.to_csv(Path("items.csv"))
    items.to_json_file(Path("items.json"))

    # All legendary items.
    legendary_items = items.items_by_type(ItemRarity.LEGENDARY)

    # Save all those legendary items to a json file.
    utils.to_json_file(list(legendary_items), Path("legendary.json"))

    # All items which are cosmetic.
    cosmetic_items = items.items_by_keypair("cosmetic", True)

    # Maybe all house items.
    house_items = items.items_by_type(ItemType.HOUSE_ITEM)
