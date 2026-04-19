# Name and Roll No
print("Name: Mangesh Mahajan")
print("Roll No: FIB48")

V = float(input("Enter voltage (V): "))
R1 = float(input("Enter resistance R1 (ohms): "))
R2 = float(input("Enter resistance R2 (ohms): "))

I = V / (R1 + R2)

print("Current in the circuit =", I, "A")