data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == "__main__":
    result = sorted(data, key=abs, reverse=True)  # без lambda-функции
    print(result)

    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)  # с lambda-функцией
    print(result_with_lambda)
