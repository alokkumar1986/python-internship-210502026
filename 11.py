import csv

with open('D:/Aptech/Python/t20 worldcup 2024.csv') as f:
    content = csv.reader(f)
    for row in content:
        print(row)