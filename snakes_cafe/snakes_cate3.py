def show_menu():
    print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************


Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

""")


def ask_customer():
    print("""
***********************************
** What would you like to order? **
***********************************
    """)


menu = {
    'Appetizers': [
        'Wings',
        'Cookies',
        'Spring Rolls'
    ],

    'Entrees': [
        'Salmon',
        'Steak',
        'Meat Tornado',
        'A Literal Garden'
    ],

    'Desserts': [
        'Ice Cream',
        'Cake',
        'Pie'
    ],
    'Drinks': [
        'Coffee',
        'Tea',
        'Unicorn Tears'
    ]

}

orders={}

def start_orders():
    all_user_orders = []

    while True:
        user_order = input("> ").title()
        if (user_order=='quit'):
            break

        not_in = True
        if user_order == 'Summary':
            not_in = False
            if not orders:
                print ('There is no order yet')
            else:
                for order in orders:
                    print(f'** {orders[order]} orders of {order} **')
        all_user_orders.append(user_order)

        count = all_user_orders.count(user_order)
        for order_menu in menu:
            for order in menu[order_menu]:
                if order == user_order:
                    print(f'** {count} order of {order} have been added to your {order_menu} **')
                    if order in orders:
                        orders[order] = orders[order] + 1
                        not_in = False
                        break
                    else:
                         orders[order] = 1
                         not_in = False
                         break
            else:
                continue
            break
        if not_in :
            print('sorry .. we don\'t have that order right now !, pick another one')
            not_in = False
            


if __name__ == "__main__":
    show_menu()
    ask_customer()
    start_orders()
