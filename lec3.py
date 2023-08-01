fruits = ["banana", "apple", "grape"]

def print_fruits():
    print()
    print("fruits =", fruits)
    print("The first element of fruits is", fruits[0])
    print("The last element of fruits is", fruits[-1])
    print()

print_fruits()

#******INSERT*****
fruits.insert(1, "orange")
print("After INSERTING")
print_fruits()

#******APPEND*****
fruits.append("raspberry")
print("After APPENDING")
print_fruits()

#******DELETE*****
del fruits[2]
print("After DELETING")
print_fruits()

#******FINDING****
print("FINDING")
print("The index of grape is", fruits.index("grape"))