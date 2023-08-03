# Exercise 1.21: Membership tests
print("Exercise 1.21: Membership tests")

symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symlist = symbols.split(",")
print("symlist:", symlist)

print("Is 'AIG' IN the `symlist`?", ("AIG" in symlist))

print("Is 'AA' IN the `symlist`?", ("AA" in symlist))

print("Is 'CAT' NOT IN the `symlist`?", ("CAT" not in symlist))

# Exercise 1.22: Appending, inserting, and deleting items
print("Exercise 1.22: Appending, inserting, and deleting items")

symlist.append("RHT")
print("symlist after append RHT:", symlist)

symlist.insert(1,"AA")
print("symlist after intert AA:", symlist)

symlist.remove("MSFT")
print("symlist after remove MSFT:", symlist)

symlist.append("YHOO")
print("symlist after append YHOO:", symlist)

print(symlist.index("YHOO"))
print("symlist[4]:", symlist[4])

print("how many YHOO in symlist:", symlist.count("YHOO"))

symlist.remove("YHOO")
print("symlist after remove first occurance YHOO:", symlist)

# Exercise 1.23: Sorting
print("Exercise 1.23: Sorting")

symlist.sort()
print("symlist after sort:", symlist)

symlist.sort(reverse=True)
print("symlist after sort in reverse order:", symlist)

# Exercise 1.24: Putting it all back together
print("Exercise 1.24: Putting it all back together")

a = ",".join(symlist)
print("join symlist with ',' :", a)

b = ":".join(symlist)
print("join symlist with ':' :", b)

c = "".join(symlist)
print("join symlist with '' :", c)

# Exercise 1.25: Lists of anything
print("Exercise 1.25: Lists of anything")

nums = [101, 102, 103]
items = ['spam', symlist, nums]
print("list in list:", items)