str = input("Nhap chuoi : ").strip()

arr = str.split(" ")
# print(arr)

dic = {}
for item in arr:
    dic[item] = arr.count(item)
    
print(dic)
