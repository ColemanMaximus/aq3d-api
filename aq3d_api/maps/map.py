class Map:
    def __init__(self,
                 id: int,
                 name: str,
                 description: str = "",
                 max_players: int = 1,
                 min_level: int = 1,
                 level_restriction: int = 1,
                 scaled: bool = False,
                 seasonal: bool = False,
                 dungeon: bool = False,
                 challenge: bool = False,
                 active: bool = False
                 ):
        self.id = id
        self.name = name
        self.description = description
        self.max_players = max_players
        self.min_level = min_level
        self.level_restriction = level_restriction
        self.scaled = scaled
        self.seasonal = seasonal
        self.dungeon = dungeon
        self.challenge = challenge
        self.active = active

    @classmethod
    def create_raw(cls, raw: dict):
        map = raw["map"]

        return cls(
            id = map.get("ID"),
            name = map.get("DisplayName"),
            description = map.get("Description", ""),
            max_players = map.get("MaxUsers", 1),
            min_level = map.get("MinLevel", 1),
            level_restriction = map.get("levelRestriction", 1),
            scaled = map.get("IsScaled", False),
            seasonal = map.get("IsSeasonal", False),
            dungeon = map.get("IsDungeon", False),
            challenge = map.get("IsChallenge", False),
            active = map.get("bActive", False)
        )