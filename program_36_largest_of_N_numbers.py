# Program 36: Program to find the largest number in a series of N numbers entered by the user

n = int(input("Enter how many numbers: "))
largest = int(input("Enter number 1: "))
for i in range(2, n + 1):
    num = int(input("Enter number " + str(i) + ": "))
    if num > largest:
        largest = num
print("Largest number =", largest)
