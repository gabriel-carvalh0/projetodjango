import os
from dados.env import environment

for key, value in environment:
    try:
        os.environ.setdefault(key, value)
    except:
        print('Error on key', key)