f = open("data.txt","r+")
#to read entire file
data = f.read()
print(data)
# d1 = f.readline()
# print(d1)
# f.close()
f.write("\nThis is a new line")
f.close()
