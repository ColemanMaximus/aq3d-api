from aq3d_api.items.containers import Items


def get_items(items_index_min: int, items_index_max: int):
    # Creates an Items instance which creates a bundle of items based on
    # the min and max index ranges.
    return Items(fromapi=True,
                 api_items_min=items_index_min,
                 api_items_max=items_index_max)


items = get_items(15000, 15500)
