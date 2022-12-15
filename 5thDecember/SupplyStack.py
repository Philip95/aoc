# Open file:
with open('Input.txt') as file:
    ten_lines = [next(file) for x in range(8)]
    lines = [i for i in file.read().strip().split("\n")]

# Building queue
queue_list = [[], [], [], [], [], [], [], [], []]

# Create and fill
for idx, line in enumerate(ten_lines):
    entry = line.replace("\n", "").split("\t")
    for counter in range(9):
        if entry[counter] != "":
            queue_list[counter].append(entry[counter])

print("Filled queue: ", queue_list)

for idx, move_command in enumerate(lines):
    if idx != 0 and move_command != "":
        split_string = move_command.split("\t")
        # print("Split String", split_string)

        number_of_blocks_to_be_moved = int(split_string[1])
        moving_from = int(split_string[3]) - 1
        moving_to = int(split_string[5]) - 1

        print("Number of blocks: ", number_of_blocks_to_be_moved, "Moving to: ", moving_to, "Moving from: ", moving_from)
        print(queue_list[moving_from])

        for move in range(1, number_of_blocks_to_be_moved + 1):
            print(move)

            # get highest element from queue
            element_to_be_moved = queue_list[moving_from][0]
            print("To be popped", element_to_be_moved)
            queue_list[moving_from].pop(0)
            queue_list[moving_to].append(element_to_be_moved)
res = ""
for first_char in queue_list:
    res += first_char[0]
print("Result", res)
