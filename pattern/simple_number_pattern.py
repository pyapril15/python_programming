"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

for this we use row and column concept for all pattern.
we use two for loop to print this pattern.
1. outer loop --> iteration loop --> for no of row.
2. inner loop --> for no of column.

// this core logic of this pattern.
so there is 5 row and column is run upto row at most.
let start.
"""

for i in range(1, 6): # outer loop, row
    for j in range(1, i + 1): # inner loop, column
        print(j, end=" ")
    print()
