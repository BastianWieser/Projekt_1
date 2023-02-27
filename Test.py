f = open("testfile.txt", "w")
f.write("2+2=4")
f.close()

#open and read the file after the overwriting and creating:
f = open("testfile.txt", "r")
print(f.read())
