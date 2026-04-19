print("Name: Mangesh Mahajan")
print("Roll No: FIB48")

with open("file1.txt", "r") as f1:
    data = f1.read()
    print("data in the file:\n",data)
data = data.replace('.', ',')
data = data.swapcase()
data = data.title()
with open("file2.txt", "w") as f2:
    f2.write(data)

print("File copied successfully with required modifications.")