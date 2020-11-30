appetizers=['Wings','Cookies', 'Spring Rolls'] 

entrees= ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden' ]

desserts= ['Ice Cream', 'Cake', 'Pie']

drinks= ['Coffee', 'Tea', 'Unicorn Tears']

all_items = ['Wings','Cookies', 'Spring Rolls', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden', 'Ice Cream', 'Cake', 'Pie', 'Coffee', 'Tea', 'Unicorn Tears']

print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('** To get a summary any time, type "summary" **')
print('**')
print('** To quit at any time, type "quit" **')
print('**************************************')

print()




print('Appetizers')
print('----------')
for i in appetizers:
    print(i)


print()

print('Entrees')
print('----------')
for i in entrees:
    print(i)

print()


print('Desserts')
print('----------')
for i in desserts:
    print(i)

print()

print('Drinks')
print('----------')
for i in drinks:
    print(i)

print()


print('***********************************') 
print('** What would you like to order? **') 
print('***********************************') 

orders={}
# orders_without_duplication= []
# {
#     "Wings": 2,
#     "Coffee": 3,
#     "Ice Cream": 1
# }

while True:
    user_input = input('> ')
    if (user_input=='quit'):
        break
    elif (user_input == 'summary'): # Stretch goal
        if (len(orders)==0):
            print ('There is no order yet')
        else:
            for order in orders:
                print(f'** {orders[order]} orders of {order} **')
    else:
        if (user_input in all_items):
            if user_input in orders:
                orders[user_input] = orders[user_input] + 1
            else:
                orders[user_input] = 1
            print(f'** {orders[user_input]} orders of {user_input} have been added to your meal **')
        else: # Stretch goal
            print('Sorry your order is not found!!')