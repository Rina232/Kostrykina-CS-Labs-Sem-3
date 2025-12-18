import sys
import os
from prototype import Flower, BouquetPrototype
from decorator import BasicOrder, WrappingDecorator, CardDecorator

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


@given('у меня есть базовый букет "{bouquet_name}" стоимостью {cost}₽')
def step_create_basic_bouquet(context, bouquet_name, cost):
    cost = cost.replace('₽', '')

    context.bouquet = BouquetPrototype(bouquet_name)
    flower = Flower("Цветок", "разноцветный", int(cost))
    context.bouquet.add_flower(flower)


@given('у меня есть базовый заказ с букетом')
def step_create_basic_order(context):
    context.order = BasicOrder(context.bouquet)


@given('у меня есть базовый заказ с букетом стоимостью {cost}₽')
def step_create_order_with_cost(context, cost):
    cost = cost.replace('₽', '')

    context.bouquet = BouquetPrototype("Букет")
    flower = Flower("Цветок", "любой", int(cost))
    context.bouquet.add_flower(flower)
    context.order = BasicOrder(context.bouquet)


@when('я добавляю стандартную упаковку')
def step_add_standard_wrapping(context):
    context.order = WrappingDecorator(context.order, "стандартная")


@when('я добавляю праздничную упаковку')
def step_add_premium_wrapping(context):
    context.order = WrappingDecorator(context.order, "праздничная")


@when('я добавляю открытку')
def step_add_card_without_message(context):
    context.order = CardDecorator(context.order)


@when('я добавляю открытку с текстом "{message}"')
def step_add_card_with_message(context, message):
    context.order = CardDecorator(context.order, message)


@when('я добавляю {service}')
def step_add_generic_service(context, service):
    if "стандартную упаковку" in service:
        context.order = WrappingDecorator(context.order, "стандартная")
    elif "праздничную упаковку" in service:
        context.order = WrappingDecorator(context.order, "праздничная")
    elif "открытку" in service and "с текстом" in service:
        import re
        match = re.search(r'"([^"]*)"', service)
        message = match.group(1) if match else ""
        context.order = CardDecorator(context.order, message)
    elif "открытку" in service:
        context.order = CardDecorator(context.order)


@then('общая стоимость заказа должна быть {expected_cost}₽')
def step_verify_total_cost(context, expected_cost):
    expected_cost = expected_cost.replace('₽', '')

    actual_cost = context.order.get_cost()
    expected = int(expected_cost)

    assert actual_cost == expected, \
        f"Ожидалось {expected}₽, получено {actual_cost}₽"


@then('описание должно содержать "{text}"')
def step_verify_description_contains(context, text):
    description = context.order.get_description()
    assert text in description, \
        f"Текст '{text}' не найден в описании: '{description}'"


@then('общая стоимость должна быть {expected_cost}₽')
def step_verify_outline_cost(context, expected_cost):
    expected_cost = expected_cost.replace('₽', '')

    actual = context.order.get_cost()
    expected = int(expected_cost)

    assert actual == expected, \
        f"Ожидалось {expected}₽, получено {actual}₽"  # python -m behave tests/features/decorator.feature
