"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

for this we use row and column concept for all pattern.
we use two for loop to print this pattern.
1. outer loop --> iteration loop --> for no of row.
2. inner loop --> for no of column.

// this core logic of this pattern.
1. so there is 5 row and column is run upto row at most.
2. start from most number of row require (Here 5 row)
3. now check column is always start from 1 and decreasing the column iteration as row is increasing.
let start.
"""

for i in range(5, 0, -1):  # outer loop, row and range(starting, ending, step)
    for j in range(1, i + 1):  # inner loop, column
        print(j, end=" ")
    print()
