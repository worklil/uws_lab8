import pickle

the_list = [["a", 1], ["b", 2], ["c", 3]]



print(the_list)
pickle_demo = open("pickle_demo.pck", "wb")
pickle.dump(the_list, pickle_demo)
pickle_demo.close()

the_list.append("tony")
print(the_list)

pickle_demo = open("pickle_demo.pck", "wb")
pickle.dump(the_list, pickle_demo)
pickle_demo.close()