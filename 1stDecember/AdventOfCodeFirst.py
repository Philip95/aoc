import operator


def get_top_three_values_as_list(elves_list):
    return dict(sorted(elves_list.items(), key=operator.itemgetter(1), reverse=True)[:3])


def add_sum_in_list(elves_list):
    res = 0
    for key in elves_list:
        res += elves_list[key]
    return res


def build_list():
    f = open("Input.txt", "r")

    counter = 0
    elves_list = {}
    added_calories = 0

    for line in f:
        if not line.strip():
            elves_list[counter] = added_calories
            added_calories = 0
            counter = counter + 1
        else:
            added_calories = int(added_calories) + int(line)
    return elves_list


elves_list = build_list()
print("Most calories: " + str(elves_list[max(elves_list, key=elves_list.get, default=None)]))
print("Get top three values: " + str(add_sum_in_list(get_top_three_values_as_list(elves_list))))
