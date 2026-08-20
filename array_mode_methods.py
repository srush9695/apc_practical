from array import array

# append
a = array('b', [10, 20, 30])
a.append(40)
print("1. append() :", a)


# buffer_info
a = array('B', [10, 20, 30])
print("2. buffer_info() :", a.buffer_info())


# byteswap
a = array('h', [10, 20, 30])
a.byteswap()
print("3. byteswap() :", a)


# count
a = array('H', [10, 20, 10, 30, 10])
print("4. count() :", a.count(10))


# extend
a = array('i', [10, 20, 30])
a.extend(array('i', [40, 50, 60]))
print("5. extend() :", a)


# frombytes
a = array('I', [10, 20])
b = array('I', [30, 40])
a.frombytes(b.tobytes())
print("6. frombytes() :", a)


# fromfile
a = array('l', [10, 20, 30])

f = open("data.txt", "wb")
a.tofile(f)
f.close()

b = array('l')

f = open("data.txt", "rb")
b.fromfile(f, 3)
f.close()

print("7. fromfile() :", b)


# fromlist
a = array('L')
a.fromlist([10, 20, 30, 40])
print("8. fromlist() :", a)


# index
a = array('q', [10, 20, 30, 40])
print("9. index() :", a.index(30))


# insert
a = array('Q', [10, 20, 30])
a.insert(1, 15)
print("10. insert() :", a)


# pop
a = array('f', [10.5, 20.5, 30.5])
a.pop()
print("11. pop() :", a)


# remove
a = array('d', [10.5, 20.5, 30.5])
a.remove(20.5)
print("12. remove() :", a)


# reverse
a = array('b', [10, 20, 30, 40])
a.reverse()
print("13. reverse() :", a)


# tobytes
a = array('B', [10, 20, 30])
b = a.tobytes()
print("14. tobytes() :", b)


# tofile
a = array('h', [10, 20, 30])

f = open("output.txt", "wb")
a.tofile(f)
f.close()

print("15. tofile() : data written to file")


# tolist
a = array('H', [10, 20, 30])
b = a.tolist()
print("16. tolist() :", b)
