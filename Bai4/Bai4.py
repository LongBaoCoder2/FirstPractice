path_file = input('Nhap ten file :')
try:
    open(path_file, 'r') 
except FileNotFoundError:
    print('File Not Found. Sellect defaults file "text.txt" ')
    path_file = 'text.txt'

with open(path_file, 'r') as reader:
    text = reader.read()
    print(text)
    