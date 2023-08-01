import pickle

string1 = "Creosote"
number1 = 37
list1 = [12, "Monkeys"]

demo_pck_file = open("pck_file.pck", "wb")

pickle.dump(string1, demo_pck_file)
pickle.dump(number1, demo_pck_file)
pickle.dump(list1, demo_pck_file)
pickle.dump("Quite an assortement", demo_pck_file)


demo_pck_file.close()


demo_pck_file = open("pck_file.pck", "rb")

for counter in range(4):
    item[counter] = pickle.load(demo_pck_file)


for i in range(4):
    print("The first item is", item[i])
'''
print(item1, "is a", type(item1))
print(item2, "is a", type(item2))
print(item3, "is a", type(item3))
print(item4, "is a", type(item4))
'''