# Program 38: Program to print Fibonacci series up to N terms

n = int(input("Enter number of terms: "))
a = 0
b = 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    next_term = a + b
    a = b
    b = next_term
print()
