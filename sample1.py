
def view_list():
 count = 1
 print()
 print("Shopping List")
 print("-------------")
 if len(shopping_list) == 0:
  print("Your shopping list is currently empty")
 else:
  for item in shopping_list:
   print(count, ".\t", item.title())
   count += 1
 print()
def find_in_list(f_item):
 is_item_in_list = False
 for item in shopping_list:
  if f_item == item:
   is_item_in_list = True
   position = shopping_list.index(item) + 1
   print(item, "is number", position, "on the list")
 return is_item_in_list
def add_to_list(a_item):
 if find_in_list(a_item) is False:
  shopping_list.append(a_item)
def delete_from_list(d_item):
 index = shopping_list.index(d_item)
 del shopping_list[index]
def quit_shopping():
 print("Thank you for using the shopping list program.")
 print("Here is your shopping list")
 view_list()
def invalid_entry():
 print("Invalid - please select option 1, 2, 3, 4 or 5")
def menu():
 print()
 print("Please select one of the following options")
 print("1 ..... to ADD an item to the list")
 print("2 ..... to REMOVE an item from the list")
 print("3 ..... to FIND an item in the list")
 print("4 ..... to VIEW the whole list")
 print("5 ..... to QUIT")
 option = input("Option >>> ")
 print()
 return option
shopping_list = []
menu_option = menu()
while True:
 if menu_option == "1":
  new_item = input("Enter an item to ADD to the list > ")
  new_item = new_item.title()
  add_to_list(new_item)
  view_list()
 elif menu_option == "2":
  print("Which product do you want to remove?")
  remove_item = input("Enter the Name > ")
  remove_item = remove_item.title()
  if find_in_list(remove_item) is True:
   delete_from_list(remove_item)
  else:
   print(remove_item, "is not currently on the list")
   view_list()
 elif menu_option == "3":
  find_item = input("What do you want to check for > ")
  find_item = find_item.title()
  if find_in_list(find_item) is False:
   print(find_item, "is not currently on the list")
   print("Do you want to add", find_item, "to the list?")
   want_to_add = input("Press 1 for YES, or 2 for NO")
   if want_to_add == "1":
    add_to_list(find_item)
    view_list()
 elif menu_option == "4":
  view_list()
 elif menu_option == "5":
  quit_shopping()
  break
 else:
  invalid_entry()
 menu_option = menu()


 # create a stub to view the list
 def view_list():
  print("VIEW the list", shopping_list)


 # create a stub to add to the list
 def add_to_list():
  print("ADD to the list")


 # create a stub to find an item in the list
 def find_in_list():
  print("FIND in the list")


 # create a stub to remove an item from the list
 def delete_from_list():
  print("REMOVE from the list")


 # create a stub to quit
 def quit_shopping():
  print("QUIT")


 # create a stub for an invalid entry
 def invalid_entry():
  print("Invalid - please select option 1, 2, 3, 4 or 5")


 # the main menu
 def menu():
  print()
  print("Please select one of the following options")
  print("1 ..... to ADD an item to the list")
  print("2 ..... to REMOVE an item from the list")
  print("3 ..... to FIND an item in the list")
  print("4 ..... to VIEW the whole list")
  print("5 ..... to QUIT")
  option = input("Option >>> ")
  print()
  return option


 # ~~~~~ THE PROGRAM ~~~~~
 # create an empty shopping list
 shopping_list = []
 # prompt for and accept the chosen menu option
 menu_option = menu()
 # call relevant function
 while True:
  if menu_option == "1":
   add_to_list()
  elif menu_option == "2":
   delete_from_list()
  elif menu_option == "3":
   find_in_list()
  elif menu_option == "4":
   view_list()
  elif menu_option == "5":
   quit_shopping()
  else:
   invalid_entry()
  # prompt for and accept the chosen menu option again
  menu_option = menu()