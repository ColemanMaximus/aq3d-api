from time import time
from abc import abstractmethod

class APIUpdater:
    def __init__(self, auto_update_fromapi: bool, update_interval: int):
        self._auto_update = auto_update_fromapi
        self._update_interval = update_interval
        self._last_updated = time()

    @property
    def __needs_updating(self) -> bool:
        if (time() - self._last_updated) < self._update_interval:
            return False

        return True

    def _update_fromapi(self) -> tuple | None:
        if not self.__needs_updating:
            return None

        self._last_updated = time()
        return self.__fetch_fromapi()

    @abstractmethod
    def __fetch_fromapi(self) -> tuple | None:
        pass