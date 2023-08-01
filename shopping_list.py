'''
Question 1
Create a program to produce a supermarket shopping list.
The list should be saved to a pickled file so that it can be amended later.
Create a menu to allow users to add items, delete items and view the whole list.
'''

the_list = []
def create_list():
    import pickle
    the_list1 = input()
    the_list.append(the_list1)
    shopping_list = open("pck_file.pck", "wb")
    pickle.dump(the_list, shopping_list) #dump() function to store the object data to the file
    shopping_list.close()
    print(the_list)
count = 1
if len(the_list) == 0:
    print("Your shopping list is currently empty")
else:
    print(the_list)


print("Please create your shopping list")
print(create_list())

def add_to_list():
    import pickle
    the_list2 = input()
    the_list.append(the_list2)
    print(the_list)
    shopping_list = open("pck_file.pck", "wb")
    pickle.dump(the_list, shopping_list)
    shopping_list.close()
    print()

def delete_from_list():
    import pickle
    shopping_list = open("pck_file.pck", "wb")
    print("what do you want to delete(number of your product from the list)?")
    element = input()
    index = the_list.index(element)
    del the_list[index] #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print(the_list)
    pickle.dump(the_list, shopping_list)
    shopping_list.close()
    print(the_list)

def view_list():
    shopping_list = open("demo.text", "r")
    contents_of_file = shopping_list.read()
    print(contents_of_file)

def find_in_list(f_item):
    shopping_list = open("demo.text", "r")
    f_item = input("Please enter the product you wish to find")
    is_item_in_list = False
    for item in the_list:
        if f_item == item:
            is_item_in_list = True
            position = the_list.index(item) + 1
            print(item, "is number", position, "on the list")
    return is_item_in_list

def quit_shopping():
    print("Thank you, we hope to see you again '^_^'")
    print("Grab your shopping list here")
    view_list()

def invalid_entry():
 print("Invalid - please select option A, S, F, V, Q")

def menu():
    print('Please select one of the following:')
    print('Type A if you want to ADD an item to the list')
    print('Type D if you want to DELETE an item from your shopping list')
    print('Type F if you want to FIND an item in the list')
    print('Type V if you want to VIEW the whole list')
    print('Type Q if you want to QUIT')
    choice = input("Choose >>> ")
    print()
    return choice

menu_choice = menu()

if menu_choice == 'A' or menu_choice == 'a':
    add_to_list()
elif menu_choice == 'D' or menu_choice == 'd':
    delete_from_list()
elif menu_choice == 'F' or menu_choice == 'f':
    find_in_list()
elif menu_choice == 'V' or menu_choice == 'v':
    view_list()
elif menu_choice == 'Q' or menu_choice == 'q':
    quit_shopping()
else:
    invalid_entry()
