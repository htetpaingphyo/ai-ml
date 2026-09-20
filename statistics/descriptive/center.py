def is_even(n: int) -> bool:
    return n % 2 == 0


def range(l: list) -> int:
    return max(l) - min(l)


def mean(l: list) -> float:
    return sum(l) / len(l)


def median(l: list) -> float:
    n = len(l) // 2
    m = 0

    if is_even(len(l)):
        m = (l[n - 1] + l[n]) / 2
    else:
        m = l[n]

    return m


def mode(l: list) -> int:
    freq: dict[int, int] = {}
    for i in l:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return max(freq, key=freq.get) if max(freq.values()) > 1 else None
