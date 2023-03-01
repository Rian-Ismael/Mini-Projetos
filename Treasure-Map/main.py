         #1   #2   #3
row1 = ["⬜️","⬜️","⬜️"]  #1
row2 = ["⬜️","⬜️","⬜️"]  #2
row3 = ["⬜️","⬜️","⬜️"]  #3
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

####################

vertical = position[0]
horizontal = position[1]

map[int(horizontal) - 1][int(vertical) - 1] = "X"

#####################

print(f"\n{row1}\n{row2}\n{row3}")