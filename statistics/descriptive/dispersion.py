from .center import mean, median


# Variance and Standard Deviation
def variance(l: list) -> float:
    m = mean(l)
    x = sum((i - m) ** 2 for i in l)
    return x / len(l)


def standard_deviation(l: list) -> float:
    # SD may be 68%, 95% or 99.7% of the data, according to the empirical rule.
    return variance(l) ** 0.5


# Normal Distribution
def normal_distribution(l: list, n: int) -> float:
    # For standard normal distribution, Mean must be 0 and SD must be 1.
    m = mean(l)
    sd = standard_deviation(l)
    return (n - m) / sd


# Quartiles and Outliers
def q_one(l: list) -> float:
    # Q1 is the 0~25% of data set and is equal to the lower half of Median
    n = len(l) // 2
    return median(l[:n])


def q_three(l: list) -> float:
    # Q3 is the 75~100% of data set and is equal to the upper half of Median
    n = len(l) // 2
    return median(l[-n:])


def iqr(l: list) -> float:
    return q_three(l) - q_one(l)


def outliers(l: list) -> tuple:
    q1 = q_one(l)
    q3 = q_three(l)
    iqrv = iqr(l)

    lower = q1 - 1.5 * iqrv
    upper = q3 + 1.5 * iqrv

    ol = [x for x in l if x < lower or x > upper]
    return (lower, upper, ol)


# Coefficient of Variation
def coefficient_of_variation(l: list) -> float:
    m = mean(l)
    sd = standard_deviation(l)
    return sd / m


# Quartile Coefficient of Variation
def quartile_coefficient_of_variation(l: list) -> float:
    iqrv = iqr(l)
    q1 = q_one(l)
    q3 = q_three(l)
    midhinge = (q3 + q1) / 2

    return 1 / 2 * iqrv / midhinge
