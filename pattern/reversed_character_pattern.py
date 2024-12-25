"""
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
1. so there is 5 row and column is run upto row at most.
2. 65 --> A, 66 --> B and so on.....
4. 97 --> a, 98 --> b and so on........
5. start from most number of row require (Here 5 row)
let start.
"""

for i in range(5, 0, -1):  # outer loop, row and range(starting, ending, step)
    for j in range(i):  # inner loop, column
        print(chr(j + 97), end=" ")
    print()
