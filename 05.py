# f = open('demo.txt', 'w')
# f.write('Hello Guys, we are learning file handling in Python')
# f.close()

with open('demo.txt', 'w') as f:
    f.write('Hello Guys, we are learning file handling in Python.')
