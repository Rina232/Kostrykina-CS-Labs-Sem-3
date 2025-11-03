import sys
import math


def get_coef_sys(index):
    try:
        coef = float(sys.argv[index])
        return coef
    except IndexError:
        print("Введено недостаточное количество корней!")
        exit()
    except ValueError:
        print("Необходимо ввести действительное число!")
        exit()


def get_coef(prompt):
    while True:
        try:
            print(prompt)
            coef = float(input())
            return coef
        except ValueError:
            print("Необходимо ввести действительное число!")


def solve_equation(a, b, c):
    if a == 0:
        print("Первый коэффициент а не должен быть равен 0")
        exit()

    disc = b ** 2 - 4 * a * c
    roots = []

    if disc < 0:
        return roots
    elif disc == 0:
        t = -b / (2.0 * a)
        if t > 0:
            root1 = math.sqrt(t)
            root2 = -math.sqrt(t)
            roots += [root1, root2]
        elif t == 0:
            roots.append(0.0)
    else:
        t1 = (-b + math.sqrt(disc)) / (2.0 * a)
        t2 = (-b - math.sqrt(disc)) / (2.0 * a)

        if t1 > 0:
            root1 = math.sqrt(t1)
            root2 = -math.sqrt(t1)
            roots += [root1, root2]
        elif t1 == 0:
            roots.append(0.0)

        if t2 > 0:
            root1 = math.sqrt(t2)
            root2 = -math.sqrt(t2)
            roots += [root1, root2]
        elif t2 == 0:
            roots.append(0.0)

    roots = sorted(list(set(roots)))
    return roots


def main():
    if len(sys.argv) > 1:
        a = get_coef_sys(1)
        b = get_coef_sys(2)
        c = get_coef_sys(3)
    else:
        print("Биквадратное уравнение: a*x^4 + b*x^2 + c = 0")
        a = get_coef('Введите первый коэффициент a:')
        b = get_coef('Введите второй коэффициент b:')
        c = get_coef('Введите третий коэффициент c:')

    roots = solve_equation(a, b, c)

    eq = f"Решение уравнения: {a}*x^4 "
    if b > 0:
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

    len_roots = len(roots)
    if len_roots == 0:
        print('Действительных корней нет')
    elif len_roots == 1:
        print(f"Один действительный корень: {roots[0]:.4g}")
    elif len_roots == 2:
        print(f'Два действительных корня: {roots[0]:.4g} и {roots[1]:.4g}')
    elif len_roots == 3:
        print(f'Три действительных корня: {roots[0]:.4g}, {roots[1]:.4g} и {roots[2]:.4g}')
    else:
        print(f'Четыре действительных корня: {roots[0]:.4g}, {roots[1]:.4g}, {roots[2]:.4g} и {roots[3]:.4g}')


if __name__ == "__main__":
    main()
