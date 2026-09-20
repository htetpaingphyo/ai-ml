from .mmm import median


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
