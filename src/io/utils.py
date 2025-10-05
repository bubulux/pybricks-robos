def forceToPercent(force: float) -> int:
    # Clamp force between 0.0 and 10.0, then scale to 0-100
    return int(max(0.0, min(force, 10.0)) * 10)


class Mutex:
    """Simple mutex implementation for custom event loop environments."""

    def __init__(self):
        self._locked = False

    def isLocked(self) -> bool:
        """Check if the mutex is currently locked."""
        return self._locked

    def lock(self) -> bool:
        """Acquire the lock. Returns True if acquired, False if already locked."""
        if self._locked:
            return False
        self._locked = True
        return True

    def unlock(self):
        """Release the lock."""
        self._locked = False

    def tryLockIfUnlocked(self) -> bool:
        """Try to acquire lock only if unlocked. Returns True if acquired."""
        if not self._locked:
            self._locked = True
            return True
        return False
