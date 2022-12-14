with open('Example.txt') as file:
    lines = [i for i in file.read().strip().split("\n")]

result = 0

for entry in lines:
    print("Entry: " + str(entry.split(",")))

    first_entry = entry.split(",")[0]
    second_entry = entry.split(",")[1]

    print("First entry: " + first_entry)
    print("Second entry: " + second_entry)

    
