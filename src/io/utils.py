def forceToPercent(force: float) -> int:
    # Clamp force between 0.0 and 10.0, then scale to 0-100
    return int(max(0.0, min(force, 10.0)) * 10)
