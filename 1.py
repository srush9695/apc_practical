def rectangle(l,b):
    area=l*b
    peri=2*(l+b)
    return area,peri
length=int(input("Enter length"))
breadth=int(input("Enter breadth"))
area,peri=rectangle(length,breadth)
print("Area=",area)
print("peri=",peri)
