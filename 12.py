f = open('demo.txt', 'w')
f.write('Hello World')
f.close()

f = open('demo.txt', 'r')
content = f.read()
print(len(content.split()))
f.close()