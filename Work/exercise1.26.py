# Exercise 1.26: File Preliminaries
print("Exercise 1.26: File Preliminaries")

with open('Work/Data/portfolio.csv', 'rt') as f:
    data = f.read()
    print(data)
    

with open('Work/Data/portfolio.csv', 'rt') as f:
    for line in f:
        print(line, end='')

with open('Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    print(headers)
    for line in f:
        row = line.split(',')
        print(row)