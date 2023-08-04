# pcost.py
#
# Exercise 1.27: Reading a data file
import gzip

with open('Work/Data/portfolio.csv', 'rt') as f:
    next(f)
    cost = 0.0
    for line in f:
        item = line.split(',')
        cost += int(item[1]) * float(item[2])
    print('Total cost:', cost)
    
# Exercise 1.28: Other kinds of "files"

with gzip.open('Work/Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end = '')