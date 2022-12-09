str = input("Nhap chuoi : ")
str = str.strip()

arr = str.split(" ")
# print(arr)

dic = {}
for item in arr:
    dic[item] = arr.count(item)
    
print(dic)