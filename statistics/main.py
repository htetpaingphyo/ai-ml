import random
from descriptive.mmm import mean, median, mode
from descriptive.quartiles import outliers, q_one, q_three, iqr
from descriptive.stdv import (
    normal_distribution as nd,
    standard_deviation as sd,
)


def main():
    numbers = random.choices(range(10, 100), k=random.randint(29, 32))
    numbers.sort()
    n = random.choice(numbers)

    print(numbers)
    print("Mean:", mean(numbers).__round__(2))
    print("Median:", median(numbers).__round__(2))
    print("Mode:", mode(numbers))
    print("Standard Deviation:", sd(numbers).__round__(2))
    print(f"Normal Distribution of {n}: {nd(numbers,n).__round__(2)}")
    print(
        f"Q1: {q_one(numbers).__round__(2)}, Q3: {q_three(numbers).__round__(2)}, IQR: {iqr(numbers).__round__(2)}"
    )
    print(f"Outliers:", outliers(numbers))


if __name__ == "__main__":
    main()
