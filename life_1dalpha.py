print("---Life---")
print("alpha-v.1d")
print("Please input straight's length . . .")
straight_length = input()
while not straight_length.isdigit():
    print("Please, input one number . . .")
    straight_length = input()

straight_length = int(straight_length)
world = ["♡"] * straight_length

print("Input one string. Space = dead cell, other symbols = alive cell.")
world_input = input()
while len(world_input) != len(world):
    print("Input length and straight length must be same.")
    world_input = input()

for i in range(straight_length):
    if world_input[i] == " ":
        world[i] = " "

print("Please, input number of generations . . .")
generations = input()
while not generations.isdigit():
    print("Please, input number . . .")
    generations = input()
generations = int(generations)

for i in world:
    print(i, end="")
print()
world.append(world[0])
world1 = world
world = world1[:-1]

for i in range(generations):
    for j in range(straight_length):
        ncount = 0
        if world[j - 1] == "♡":
            ncount += 1
        if world1[j + 1] == "♡":
            ncount += 1
        if world1[j] == "♡":
            if ncount != 1:
                world1[j] = " "
        else:
            if ncount == 1:
                world1[j] = "♡"
    world = world1[:-1]
    world1[-1] = world1[0]
    for j in world:
        print(j, end="")
    print()