from string import ascii_letters

with open('RucksackInput.txt') as file:
    lines = [i for i in file.read().strip().split("\n")]


def split_strings(read_lines):
    total = 0
    for line in read_lines:
        s_length = int(len(line) / 2)
        first_part = line[:s_length]
        last_part = line[s_length:]

        for prio, char in enumerate(ascii_letters):
            if char in first_part and char in last_part:
                total += prio + 1

    return total


print(str(split_strings(lines)))

totalSum = 0
j = 3
for i in range(0, len(lines), 3):
    entry = lines[i:j]
    j += 3

    for value, character in enumerate(ascii_letters):
        if character in entry[0] and character in entry[1] and character in entry[2]:
            totalSum += value + 1


print("Answer to part 2: ", totalSum)
# %%
