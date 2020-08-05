"""
Convert column names (A, B, C, ... AA, AB, ..) to ids.
A = 1
B = 2
...

"""

def spreadsheet_encode_column(col_str):
    num = 0
    count = len(col_str) - 1
    for c in col_str:
        num += 26**count * (ord(c) - ord('A') + 1)
        count -= 1
    return num


# Tests
print(spreadsheet_encode_column("A"))
print(spreadsheet_encode_column("B"))
print(spreadsheet_encode_column("AA"))
print(spreadsheet_encode_column("ZZ"))
