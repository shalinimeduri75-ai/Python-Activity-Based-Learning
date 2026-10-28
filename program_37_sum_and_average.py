# Program 37: Program to find the sum and average of N numbers

n = int(input("Enter how many numbers: "))
total = 0
for i in range(1, n + 1):
    num = int(input("Enter number " + str(i) + ": "))
    total = total + num
average = total / n
print("Sum =", total)
print("Average =", average)
