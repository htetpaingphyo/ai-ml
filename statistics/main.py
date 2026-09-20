import random
from descriptive.center import mean, median, mode
from descriptive.dispersion import (
    outliers,
    q_one,
    q_three,
    iqr,
    normal_distribution as nd,
    standard_deviation as sd,
    coefficient_of_variation as cv,
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
    print(f"First Quartile: {q_one(numbers).__round__(2)}")
    print(f"Third Quartile: {q_three(numbers).__round__(2)}")
    print(f"IQR: {iqr(numbers).__round__(2)}")
    print(f"Outliers:", outliers(numbers))
    print(f"Coefficient of Variation: {cv(numbers).__round__(2)}")


if __name__ == "__main__":
    main()
