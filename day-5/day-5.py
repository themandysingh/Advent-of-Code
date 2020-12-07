# --- Day 5: Binary Boarding ---
# You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

# You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.

# Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

# For example, consider just the first seven characters of FBFBBFFRLR:

# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
# The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

# For example, consider just the last 3 characters of FBFBBFFRLR:

# Start by considering the whole range, columns 0 through 7.
# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# The final R keeps the upper of the two, column 5.
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

# Here are some other boarding passes:

# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?


# --- Part Two ---
# Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

# It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

# What is the ID of your seat?

input_file = open("day-5.txt", "r")

def find_row(row):
    front = 0
    back = 127
    total = 128
    for char in row:
        total = total / 2
        if char == 'F':
            back = back - total
        else:
            front = front + total
        
    return int(front)
            

def find_col(col):
    left = 0
    right = 7
    total = 8
    for char in col:
        total = total / 2
        if char == 'L':
            right = right - total
        else:
            left = left + total
    return int(left)

max_seat_id = -1
seats = set()
for boarding_pass in input_file:
    boarding_pass = boarding_pass.strip()
    row = find_row(boarding_pass[:7])
    column = find_col(boarding_pass[7:])
    seat_id = row * 8 + column
    seats.add(seat_id)
    if seat_id > max_seat_id:
        max_seat_id = seat_id

print(max_seat_id)

for seat in seats:
    if seat+2 in seats and seat+1 not in seats:
        print(seat + 1)






