import random as rd

try:
    a = int(input("Nhap gia tri a: "))
    b = int(input("Nhap gia tri b: "))
    numRand = rd.randint(a,b)
    print(numRand)
except:
    print("Loi nhap gia tri, vui long nhap gia tri a <= b !")


