"""
        A
      A B
    A B C
  A B C D
A B C D E
  A B C D
    A B C
      A B
        A


for this we use row and column concept for all pattern.
we use two for loop to print this pattern.
1. outer loop --> iteration loop --> for no of row.
2. inner loop --> for no of column.

// this core logic of this pattern.
1. we make upper part of the diamond.
2. then make lower part of the diamond.
3. 65-->A, 66-->B and so on.....
let start.
"""

# upper part of the diamond
# 1. there is 5 iteration
n = 5
for i in range(1, n+1): # outer loop run to 1 + of number of times(5)
    print(" "*(n-i), end="") # space are multiply(total number of iteration - current iteration
    for j in range(i): # every iteration for i
        print(chr(65 + j), end="")
    print()

# lower part of the diamond
# 1. there is 4 iteration
for i in range(n-1, 0, -1): # iteration start from 4 and goes to 0
    print(" " * (n - i), end="")  # space are multiply(total number of iteration - current iteration
    for j in range(i):  # every iteration for i
        print(chr(65 + j), end="")
    print()