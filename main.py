import sys


def get_coefficient(index, text):
    """ Получение коэффициентов из консоли """
    while True:
        if index < len(sys.argv):
            string_coefficient = sys.argv[index]
            try:
                coefficient = float(string_coefficient)
                return coefficient
            except ValueError:
                print("Необходимо ввести действительное число!")

        print(text)
        string_coefficient = input()

        try:
            coefficient = float(string_coefficient)
            return coefficient
        except ValueError:
            print("Необходимо ввести действительное число!")


def solve_equation(a, b, c):
    """ Функция решения биквадратного уравнения """
    if a == 0:
        print("Первый коэффициент а не должен быть равен 0")
        exit()

    disc = b ** 2 - 4 * a * c
    roots = []

    if disc < 0:
        return roots
    else:
        t1 = (-b + disc ** 0.5) / (2 * a)
        t2 = (-b - disc ** 0.5) / (2 * a)

        if t1 >= 0:
            roots.append(t1 ** 0.5)
            roots.append(- t1 ** 0.5)

        if t2 >= 0:
            roots.append(t2 ** 0.5)
            roots.append(- t2 ** 0.5)

    roots = sorted(list(set(roots)))
    return roots


def main():
    """ Основная функция программы """
    print("Биквадратное уравнение: a*x^4 + b*x^2 + c = 0")
    a = get_coefficient(1, 'Введите первый коэффициент a:')
    b = get_coefficient(2, 'Введите второй коэффициент b:')
    c = get_coefficient(3, 'Введите третий коэффициент c:')

    if a == 1:
        eq = f"Решение уравнения: x^4 "
    elif a == -1:
        eq = f"Решение уравнения: -x^4 "
    else:
        eq = f"Решение уравнения: {a}*x^4 "
    if b == 1:
        eq += f"+ x^2 "
    elif b == -1:
        eq += f"- x^2 "
    elif b > 0:
        eq += f"+ {b}*x^2 "
    elif b < 0:
        eq += f"- {abs(b)}*x^2 "
    if c > 0:
        eq += f"+ {c} = 0"
    elif c < 0:
        eq += f"- {abs(c)} = 0"
    else:
        eq += f"= 0"
    print(eq)

    roots = solve_equation(a, b, c)

    if len(roots) == 0:
        print('Действительных корней нет')
    elif len(roots) == 1:
        print(f"Один действительный корень: {roots[0]:.4g}")
    elif len(roots) == 2:
        print(f'Два действительных корня: {roots[0]:.4g} и {roots[1]:.4g}')
    elif len(roots) == 3:
        print(f'Три действительных корня: {roots[0]:.4g}, {roots[1]:.4g} и {roots[2]:.4g}')
    else:
        print(f'Четыре действительных корня: {roots[0]:.4g}, {roots[1]:.4g}, {roots[2]:.4g} и {roots[3]:.4g}')


if __name__ == "__main__":
    main()
