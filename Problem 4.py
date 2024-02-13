number = 51
for i in range(1, number):
    if i % 3:
        print("Divisible by 3")
    if i % 5 == 0:
        print("Divisible by 5")
    if (i % 3) & (i % 5):
        print("Divisible by both")
