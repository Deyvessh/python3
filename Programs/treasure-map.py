row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","️⬜️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

# first digit position will be horizontal
# second digit postiion will be vertical

# put 'X' in the position

horizontal = int(position[0])
vertical = int(position[1])


# [vertical - 1] is why, cause if the vertical position is 3 but index goes to only 2, so (n - 1)

vertical_mark = map[vertical - 1]

vertical_mark[horizontal - 1] = 'X'





print(f"{row1}\n{row2}\n{row3}")

