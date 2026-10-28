# Program 42: Program to count the number of digits in a number

num = int(input("Enter a number: "))
count = 0
temp = num
while temp > 0:
    count = count + 1
    temp = temp // 10
print("Number of digits =", count)
