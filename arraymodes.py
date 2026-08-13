from array import array

# Signed char
a1 = array('b', [-10, 0, 10])
print(a1, "Item size:", a1.itemsize)

# Unsigned char
a2 = array('B', [0, 10, 255])
print(a2, "Item size:", a2.itemsize)

# Unicode character
a3 = array('u', 'ABC')
print(a3, "Item size:", a3.itemsize)

# Signed short
a4 = array('h', [-1000, 0, 1000])
print(a4, "Item size:", a4.itemsize)

# Unsigned short
a5 = array('H', [0, 1000, 65535])
print(a5, "Item size:", a5.itemsize)

# Signed integer
a6 = array('i', [-10000, 0, 10000])
print(a6, "Item size:", a6.itemsize)

# Unsigned integer
a7 = array('I', [0, 10000, 50000])
print(a7, "Item size:", a7.itemsize)

# Signed long
a8 = array('l', [-100000, 0, 100000])
print(a8, "Item size:", a8.itemsize)

# Unsigned long
a9 = array('L', [0, 100000, 200000])
print(a9, "Item size:", a9.itemsize)

# Signed long long
a10 = array('q', [-1000000000, 0, 1000000000])
print(a10, "Item size:", a10.itemsize)

# Unsigned long long
a11 = array('Q', [0, 1000000000, 2000000000])
print(a11, "Item size:", a11.itemsize)

# Float
a12 = array('f', [10.5, 20.5, 30.5])
print(a12, "Item size:", a12.itemsize)

# Double
a13 = array('d', [10.123, 20.456, 30.789])
print(a13, "Item size:", a13.itemsize)
