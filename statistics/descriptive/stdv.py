from .mmm import mean


def variance(l: list) -> float:
    m = mean(l)
    x = sum((i - m) ** 2 for i in l)
    return x / len(l)


def standard_deviation(l: list) -> float:
    # SD may be 68%, 95% or 99.7% of the data, according to the empirical rule.
    return variance(l) ** 0.5


def normal_distribution(l: list, n: int) -> float:
    # For standard normal distribution, Mean must be 0 and SD must be 1.
    m = mean(l)
    sd = standard_deviation(l)
    return (n - m) / sd
