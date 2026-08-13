from array import array

a = array('i', [10, 20, 30, 40, 50])

print("Original Array:", a)

print("\n1. Accessing Elements")
print("First element:", a[0])
print("Third element:", a[2])
print("Last element:", a[-1])

print("\n2. Append Element")
a.append(60)
print("After append:", a)

print("\n3. Insert Element")
a.insert(2, 25)
print("After insert:", a)

print("\n4. Remove Element")
a.remove(25)
print("After remove:", a)

print("\n5. Sort Array")
a = array('i', sorted(a))
print("After sorting:", a)

print("\n6. Reverse Array")
a.reverse()
print("After reverse:", a)

print("\n7. Length of Array")
print("Length:", len(a))

print("\n8. Search Element")
n = int(input("Enter element to search: "))

if n in a:
    print("Element found")
else:
    print("Element not found")

print("\n9. Maximum Element")
print("Maximum:", max(a))

print("\n10. Minimum Element")
print("Minimum:", min(a))

print("\n11. Sum of Elements")
print("Sum:", sum(a))

print("\n12. Display Elements Using Loop")
for i in a:
    print(i)

print("\n13. Copy Array")
b = array('i', a)
print("Original Array:", a)
print("Copied Array:", b)
