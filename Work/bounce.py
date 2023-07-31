# bounce.py
#
# Exercise 1.5

Height = 100
Loop = 10
i = 1

while (i <= 10):
    Height = Height/5*3
    print(f"{i} {round(Height, 4)}")
    i += 1