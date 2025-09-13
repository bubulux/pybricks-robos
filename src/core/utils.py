def speedConverter(speed: int) -> int:
    base = 2000
    percentile = base / 100
    return int(speed * percentile)
