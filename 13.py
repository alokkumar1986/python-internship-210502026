import json
f = open('demo.json', 'w')
f.write('{"name": "Alice", "age": 30, "city": "New York"}')
f.close()


f = open('demo.json', 'r')
content = f.read()
data = json.loads(content)
print(data.keys())

f.close()