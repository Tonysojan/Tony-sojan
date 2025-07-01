x = int(input("Enter a number: "))
limit = x if x % 2 != 0 else x - 1
for i in range(1, limit + 1, 2):
    print(i, end=", ")
