from aq3d_api.items.containers import Items

items = Items(fromapi=True,
              api_items_min=15000,
              api_items_max=15500,
              auto_update_fromapi=True,
              update_interval=80000)
