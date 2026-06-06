
import os

if(os.path.exists('D:/Aptech/Python/demo.csv')):
    print('File already exists')
    
else:
    f = open('D:/Aptech/Python/demo.csv', 'x')
    f.close()