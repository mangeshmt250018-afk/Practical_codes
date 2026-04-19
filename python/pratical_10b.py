import math

print("Name: Mangesh Mahajan")
print("Roll No: FIB48")

Q = 1000  
z = 4    

r1 = 0
sigma1 = (3 * Q) / (2 * math.pi * z**2)

r2 = 3
sigma2 = (3 * Q) / (2 * math.pi * z**2) * (1 / (1 + (r2/z)**2)**(5/2))

print("Vertical pressure directly below load =", sigma1, "kN/m^2")
print("Vertical pressure at 3m distance =", sigma2, "kN/m^2")