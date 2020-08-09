"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8

"""

def row_sum_odd_numbers(n):
    count = 0
    odd = 1

    # Find the first number of the last row (n-1)
    while count != n:
        odd += count * 2
        count += 1

    print("First element of the n-th row:" + str(odd))

    for i in range(n):
        odd += odd + 2

    print("Sum:" + str(odd))


row_sum_odd_numbers(1)
row_sum_odd_numbers(2)
row_sum_odd_numbers(3)
row_sum_odd_numbers(4)
row_sum_odd_numbers(5)
# row_sum_odd_numbers(13)
# row_sum_odd_numbers(19)
# row_sum_odd_numbers(41)
