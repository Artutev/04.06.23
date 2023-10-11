def can_afford(s, p, m):
    total_cost = s + p
    return "Да" if m >= total_cost else "Нет"

s = float(input("Введите стоимость подписки на онлайн-кинотеатр: "))
p = float(input("Введите стоимость пиццы: "))
m = float(input("Введите заработок Васи: "))

result = can_afford(s, p, m)

print(result)
