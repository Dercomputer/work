'''
Введите количество пространственных узлов, N: 5
Введите окончание по времени, t_end: 1.0
Введите толщину пластины, L: 0.1      (10 см)
Введите плотность материала пластины, ro: 8000  (сталь)
Введите теплоемкость материала пластины, c: 500
Введите начальную температуру в К, T0: 300  (комнатная)
Введите температуру в К на границе х=0, Th: 400  (нагретый край)
Введите температуру в К на границе х=L, Tc: 200  (охлаждаемый край)
iter.txt -
Время 0.0100: выполнено
Время 0.0200: выполнено
...
Время 1.0000: выполнено

res.txt -

Толщина пластины L = 0.1000
Число узлов по координате N = 5
Плотность материала пластины ro = 8000.0000
Теплоемкость материала пластины с = 500.0000
Начальная температура T0 = 300.0000
Температура на границе x = 0, Th = 400.0000
Температура на границе x = L, Tc = 200.0000
Результат получен с шагом по координате h = 0.0250
Результат получен с шагом по времени tau = 0.0100
Температурное поле в момент времени t = 1.0000

tempr.txt - распределение температуры (в °C) по координате:
 0.000  127.00000
 0.025   <значение>
 0.050   <значение>
 0.075   <значение>
 0.100  -73.00000
'''
def main():
    n: int = 500
    eps: float = 1e-5

    T: list = list(0.0 for _ in range(n))
    Ts: list = list(0.0 for _ in range(n))
    Tn: list = list(0.0 for _ in range(n))
    alfa: list = list(0.0 for _ in range(n))
    beta: list = list(0.0 for _ in range(n))

    coefficient_thermal = lambda x: 5500 / (560 + x) + 0.942 * 1e-10 * x * x ** 2

    ai: float
    bi: float
    ci: float
    fi: float
    max1: float
    max2: float
    s: int

    N: int = int(input("Введите количество пространственных узлов, N: "))
    t_end: float = float(input("Введите окончание по времени, t_end: "))
    L: float = float(input("Введите толщину пластины, L: "))
    ro: float = float(input("Введите плотность материала пластины, ro: "))
    c: float = float(input("Введите теплоемкость материала пластины, c: "))
    T0: float = float(input("Введите начальную температуру в К, T0: "))
    Th: float = float(input("Введите температуру в К на границе х=0, Th: "))
    Tc: float = float(input("Введите температуру в К на границе х=L, Tc: "))

    h: float = L / (N - 1)
    tau: float = t_end / 100
    # T[0] = Th
    for i in range(1, N - 1):
        T[i] = T0
    with (open("iter.txt", 'w', encoding="utf-8") as f1, open("res.txt", "w", encoding="utf-8") as f,
          open("tempr.txt", "w", encoding="utf-8") as g):
        time: float = 0.0
        s = 0
        while time < t_end:
            time += tau
            for i in range(0, N):
                Tn[i] = T[i]
            s += 1
            while True:
                for i in range(0, N):
                    Ts[i] = T[i]
                alfa[0] = 0.0
                beta[0] = Th
                for i in range(1, N - 1):
                    ai = 0.5 * (coefficient_thermal(T[i]) + coefficient_thermal(T[i + 1])) / h ** 2
                    ci = 0.5 * (coefficient_thermal(T[i - 1]) + coefficient_thermal(T[i])) / h ** 2
                    bi = ai + ci + ro * c / tau
                    fi = -ro * c * Tn[i] / tau
                    alfa[i] = ai / (bi - ci * alfa[i - 1])
                    beta[i] = (ci * beta[i - 1] - fi) / (bi - ci * alfa[i - 1])
                T[N - 1] = Tc
                for i in range(N - 2, 0, -1):
                    T[i] = alfa[i] * T[i + 1] + beta[i]
                max1 = abs(T[0] - Ts[0])
                for i in range(1, N):
                    if max1 < abs(T[i] - Ts[i]):
                        max1 = abs(T[i] - Ts[i])
                max2 = abs(T[0])
                for i in range(1, N):
                    if max2 < abs(T[i]):
                        max2 = abs(T[i])
                if max1 / max2 <= eps:
                    break
                f1.write(f'В момент времени {time:6.4f} проведено {s} итераций\n')

        f.write(f"Толщина пластины L = {L:6.4f}\n")
        f.write(f'Число узлов по координате N = {N}\n')
        f.write(f'Плотность материала пластины ro = {ro:6.4f}\n')
        f.write(f'Теплоемкость материала пластины с = {c:6.4f}\n')
        f.write(f'Начальная температура T0 = {T0:6.4f}\n')
        f.write(f'Температура на границе x = 0, Th = {Th:6.4f}\n')
        f.write(f'Температура на границе x = L, Tc = {Tc:6.4f}\n')
        f.write(f'Результат получен с шагом по координате h = {h:6.4f}\n')
        f.write(f'Результат получен с шагом по времени tau = {tau:6.4f}\n')
        f.write(f'Температурное поле в момент времени t = {t_end:6.4f}\n')

        for i in range(1, N + 1):
            g.write(f" {h * (i - 1):6.3f} {T[i] - 273:8.5f}\n")


if __name__ == "__main__":
    main()
