# Exercise 1.19 - 1.20

symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symlist = symbols.split(",")

symlist[2] = 'AIG'

mysyms = []
mysyms.append('GOOG')
print(symlist)

symlist[-2:] = mysyms

print(symlist)