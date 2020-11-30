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


def start_orders():

    all_user_orders = []

    while True:
        user_order = input(">")
        all_user_orders.append(user_order)

        count = all_user_orders.count(user_order)

        if user_order in menu['Appetizers']:
            print(
                f'** {count} order of {user_order} have been added to your Appetizers **')
        elif user_order in menu['Entrees']:
            print(
                f'** {count} order of {user_order} have been added to your Entrees **')
        elif user_order in menu['Desserts']:
            print(
                f'** {count} order of {user_order} have been added to your Desserts **')
        elif user_order in menu['Drinks']:
            print(
                f'** {count} order of {user_order} have been added to your Drinks **')
        elif user_order == 'quit':
            break
        else:
            print('sorry .. we don\'t have that order right now !, try another one')


if __name__ == "__main__":
    show_menu()
    ask_customer()
    start_orders()
