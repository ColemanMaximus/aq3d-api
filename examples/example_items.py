import sys
sys.path.append(".")

from pathlib import Path

from aq3d_api import utils
from aq3d_api.enums.item_rarity import ItemRarity
from aq3d_api.containers.items import Items
from aq3d_api.enums.item_type import ItemType


def get_items(min_index: int = 1, max_index: int = 1):
    # Creates an Items instance which creates a bundle of items based on
    # the min and max index ranges.
    return Items({
        "min-index": min_index,
        "max-index": max_index
    })


if __name__ == "__main__":
    # Create an Items object with item IDs between 300 and 600.
    items = get_items(1, 150)
    # Update the items container at least once to gather the API data.
    items.update()

    # Save items to either a CSV file or JSON file.
    items.to_csv(Path("items.csv"))
    items.to_json_file(Path("items.json"))

    # All legendary items.
    legendary_items = items.by_type(ItemRarity.LEGENDARY)

    # Save all those legendary items to a json file.
    utils.to_json_file(list(legendary_items), Path("legendary.json"))

    # All items which are cosmetic.
    cosmetic_items = items.by_keypair("cosmetic", True)

    # Maybe all house items.
    house_items = items.by_type(ItemType.HOUSE_ITEM)
