string1 = ("John")
string2 = ("Paul")
string3 = ("George")
string4 = ("Ringo")

demo_file = open("demo.text", "w")
#if we open a file ("deemo.text")  we create a file
#The open_ function has 3 parameters - the name (and maybe the path) of the file, and a "w" because we plan to write to the file

demo_file.write(string1)
demo_file.write(string2)
demo_file.write(string3)
demo_file.write(string4)
demo_file.write("Fab")
demo_file.write("4")

demo_file.close()

demo_file = open("demo.text", "rb")
contents_of_file = demo_file.read()
print(contents_of_file)
