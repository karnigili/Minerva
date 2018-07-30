from create_db import *
from insert_data import *
import sys

def init(n):
    create_schema()
    insert_data(n=n)

if __name__ == "__main__":
    try:
        n = sys.argv[1]
        n = int(n)

    except:
        n = 5

    
    init(n)
    