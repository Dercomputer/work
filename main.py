import math


def main():
    n: int = 500
    eps: float = 1e-5
    vector: list = list(0.0 for _ in range(n))

    coefficient_thermal = lambda x: 5500 / (560 + x) + 0.942 * 1e-10 * x * math.sqrt(x)

    N: int = int(input("Введите количество пространственных узлов, N"))
    t_end: float = float(input("Введите окончание по времени, t_end"))
    L: float = float(input("Введите толщину пластины, L"))
    ro: float = float(input("Введите плотность материала пластины, ro"))
    c: float = float(input("Введите теплоемкость материала пластины, c"))



if __name__ == "__main__":
    main()
