import pickle

demo_of_pickle = open("pickle_demo.pck", "rb")
my_list = pickle.load(demo_of_pickle)
demo_of_pickle.close()

print("Original version of the file")
print(my_list)

print("*****after APPEND******")
my_list.append(["e", 5])
print(my_list)

print("*****after INSERT******")
my_list.insert(3, ["d", 4])
print(my_list)

#*********write the new version of list to pickled file
demo_of_pickle = open("pickle_demo.pck", "wb")
pickle.dump(my_list, demo_of_pickle)
demo_of_pickle.close()