length = int(input("Nhap so phan tu trong mang :"))

arr = [int(input("Nhap so phan tu {} : ".format(i))) for i in range(length)]

dic = {}
for i in arr:
    dic[i] = 0
for i in arr:
    dic[i] = dic[i] + 1

print(dic)