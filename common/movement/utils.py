def convertPercentToDegreesPerSecond(speed: int) -> int:
    base = 1000
    percentile = base / 100
    return int(speed * percentile)
