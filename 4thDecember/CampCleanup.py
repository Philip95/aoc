with open('Example.txt') as file:
    lines = [i for i in file.read().strip().split("\n")]

result = 0

for entry in lines:
    first_pair = [int(x) for x in entry.split(",")[0].split("-")]
    second_pair = [int(x) for x in entry.split(",")[1].split("-")]

    print(first_pair)
    print(first_pair[1])
    print(second_pair)

print("Result: " + str(result))
