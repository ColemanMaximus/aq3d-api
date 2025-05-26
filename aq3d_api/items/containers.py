from aq3d_api.updater.api_updater import APIUpdater


class Items(APIUpdater):
    api_url = "https://game.aq3d.com/api/Game/GetItems"
    param_key = "IDs"

    def __init__(self,
                 items = None,
                 fromapi: bool = False,
                 api_item_max: int = 0,
                 auto_update_fromapi: bool = False,
                 update_interval: int = 60
                 ):
        super().__init__(auto_update_fromapi, update_interval)

    def __fetch_fromapi(self) -> tuple | None:
        pass