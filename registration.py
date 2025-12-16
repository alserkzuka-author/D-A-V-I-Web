import random
from datetime import datetime, timedelta

# База пользователей
users = {}

# База товаров
products = {
    1: {"name": "Фитнес-браслет", "price": 2500},
    2: {"name": "Наушники", "price": 1800},
    3: {"name": "Умная лампа", "price": 1200}
}

# Список заказов
orders = []

# -----------------------
# Регистрация пользователя
# -----------------------
def register():
    print("\n=== Регистрация пользователя ===")
    name = input("Введите ваше имя: ")
    if name in users:
        print("⚠ Вы уже зарегистрированы!")
    else:
        users[name] = {"orders": [], "feedbacks": []}
        print(f"✔ {name}, вы успешно зарегистрированы!")
    return name

# -----------------------
# Просмотр товаров
# -----------------------
def view_products():
    print("\n=== Список товаров ===")
    for pid, p in products.items():
        print(f"{pid}. {p['name']} — {p['price']} руб.")

# -----------------------
# Оформление заказа с датой доставки
# -----------------------
def make_order(user):
    view_products()
    try:
        choice = int(input("Введите номер товара для покупки: "))
        if choice not in products:
            print("⚠ Неверный товар.")
            return
        quantity = int(input("Количество: "))
        total = products[choice]["price"] * quantity
        # Дата доставки через 3-7 дней
        delivery_days = random.randint(3, 7)
        delivery_date = datetime.now() + timedelta(days=delivery_days)
        delivery_str = delivery_date.strftime("%d.%m.%Y")
        order = {
            "user": user,
            "product": products[choice]["name"],
            "quantity": quantity,
            "total": total,
            "delivery_date": delivery_str,
            "status": "В обработке",
            "feedback": None
        }
        orders.append(order)
        users[user]["orders"].append(order)
        print(f"✔ Заказ оформлен! Сумма: {total} руб.")
        print(f"📦 Ожидаемая дата доставки: {delivery_str}")
    except:
        print("Введите корректные числа.")

# -----------------------
# Оставить отзыв после доставки
# -----------------------
def leave_feedback(user):
    user_orders = users[user]["orders"]
    if not user_orders:
        print("У вас пока нет заказов.")
        return
    print("\n=== Ваши заказы ===")
    for i, o in enumerate(user_orders, 1):
        status = "Есть отзыв" if o["feedback"] else "Нет отзыва"
        print(f"{i}. {o['product']} x{o['quantity']} — {o['status']} — {status} (Доставка: {o['delivery_date']})")
    try:
        choice = int(input("Выберите заказ для отзыва: ")) - 1
        if 0 <= choice < len(user_orders):
            if user_orders[choice]["feedback"]:
                print("Вы уже оставили отзыв на этот заказ.")
            else:
                fb = input("Введите отзыв: ")
                user_orders[choice]["feedback"] = fb
                user_orders[choice]["status"] = "Доставлено"
                print("✔ Отзыв добавлен! Заказ помечен как доставленный.")
        else:
            print("Неверный выбор.")
    except:
        print("Введите корректный номер.")

# -----------------------
# Просмотр всех заказов пользователя
# -----------------------
def view_orders(user):
    user_orders = users[user]["orders"]
    if not user_orders:
        print("У вас пока нет заказов.")
        return
    print("\n=== Ваши заказы ===")
    for o in user_orders:
        print(f"{o['product']} x{o['quantity']} — {o['status']} — Доставка: {o['delivery_date']} — Отзыв: {o['feedback'] or 'Нет'} — Сумма: {o['total']} руб.")

# -----------------------
# Главный цикл
# -----------------------
current_user = None
while True:
    print("\n=== Мини-магазин с датой доставки ===")
    print("1. Регистрация/Вход")
    print("2. Просмотреть товары")
    print("3. Оформить заказ")
    print("4. Просмотреть свои заказы")
    print("5. Оставить отзыв на заказ")
    print("6. Выход")
    choice = input("Выберите пункт: ")
    if choice == "1":
        current_user = register()
    elif choice == "2":
        view_products()
    elif choice == "3":
        if current_user:
            make_order(current_user)
        else:
            print("⚠ Сначала зарегистрируйтесь!")
    elif choice == "4":
        if current_user:
            view_orders(current_user)
        else:
            print("⚠ Сначала зарегистрируйтесь!")
    elif choice == "5":
        if current_user:
            leave_feedback(current_user)
        else:
            print("⚠ Сначала зарегистрируйтесь!")
    elif choice == "6":
        print("Выход.")
        break
    else:
        print("Неизвестная команда.")