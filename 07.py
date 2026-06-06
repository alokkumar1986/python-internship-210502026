# f = open('demo.txt')
# content = f.read()
# print(content)
# f.close()

# f = open('demo.txt')
# content = f.readline()
# content = f.readline()
# content = f.readline()
# print(content)
# f.close()

f = open('demo.txt')
content = f.readlines()[3]
print(content)
f.close()