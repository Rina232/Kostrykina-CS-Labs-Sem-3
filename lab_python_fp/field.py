def field(dict, *args):
    """ Генератор, возвращающий поля слловарей"""
    if len(args) == 1:
        key = args[0]
        for item in dict:
            if key in item and item[key] is not None:
                yield item[key]
                
    else:
        for item in dict:
            res = {}
            not_empty = False

            for key in args:
                if key in item and item[key] is not None:
                    res[key] = item[key]
                    not_empty = True

            if not_empty:
                yield res


if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]
    print(*(i for i in field(goods, 'title')))  # должен выдавать 'Ковер', 'Диван для отдыха'
    print()
    print(*(i for i in field(goods, 'title', 'price')))  # должен выдавать {'title': 'Ковер', 'price': 2000},
    # {'title': 'Диван для отдыха', 'price': 5300}
