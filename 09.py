import os

if(os.path.exists('demo.csv')):
    os.remove('demo.csv')
else:
    print('The file does not exist')