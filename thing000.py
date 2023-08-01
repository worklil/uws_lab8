'''
Question 1
Create a program to produce a supermarket shopping list.
The list should be saved to a pickled file so that it can be amended later.
Create a menu to allow users to add items, delete items and view the whole list.

'''
import pickle

things_counter = int(input("how many things you want to buy:"))
print()

demo_pck_file = open("pck_file.pck", "wb")
for counter in range(things_counter):
    num = input()
    str = [counter + 1, num]
    pickle.dump(str, demo_pck_file)
    print(counter + 1, num)
print()
demo_pck_file.close()

demo_pck_file = open("pck_file.pck", "rb")

for counter in range(things_counter):
    item1 = pickle.load(demo_pck_file)
    print(item1)


add_answ = input("Do you want to add something:")
if add_answ == "Yes" or add_answ == "yes":
    add_num = int(input("how many things you want to add"))
    for count_num in range(add_num):
        print("what do you want to add")
        new = input()
        item1.append(new)
        print("After APPENDING")
        print(item1)

    else:
        print()

'''
shopping_list = open("pck_file.pck", "wb")
pickle.dump(the_list, shopping_list)
shopping_list.close()
print(type(the_list))
shopping_list = open("pck_file.pck", "wb")
the_list.append()
print(the_list)


print('Please select one of the following:')
print('Type A if you want to APPENDING')
print('Type D if you want to DELETE')
menu_choice = input(">> ")

if menu_choice == 'D' or menu_choice == 'd':
    dn = int(input("What do you want to delete?(number)"))
    the_list[dn] = pickle.load(shopping_list)
    del shopping_list[dn+1]
    print("After DELETING")
    print(the_list)
else:
    print('...')
'''