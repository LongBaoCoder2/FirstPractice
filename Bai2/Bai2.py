row = int(input("Nhap so hang : "))
col = int(input("Nhap so cot : "))
array = []

for i in range(row):
    sub_array = [int(input(f"Nhap hang {i} cot {j} :")) for j in range(col)]
    array.append(sub_array);

print(array)
new_list = [i for sub_array in array for i in sub_array]
print(new_list)

