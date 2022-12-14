file = open("RockPaperScissors.txt", "r")
lines = [line.rstrip('\n') for line in file.readlines() if line.strip() != '']

opponent = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissor'
}

score_for_shape = {
    'Rock': 1,
    'Paper': 2,
    'Scissor': 3
}


def rock_paper_scissors_part_one(score_for_shape, lines):
    player = {
        'X': 'Rock',
        'Y': 'Paper',
        'Z': 'Scissor'
    }
    turn_combinations = {
        'AX': 3,
        'AY': 6,
        'AZ': 0,
        'BX': 0,
        'BY': 3,
        'BZ': 6,
        'CX': 6,
        'CY': 0,
        'CZ': 3
    }
    total_score = 0

    for line in lines:
        combination = line.replace(" ", "")
        total_score += turn_combinations[combination] + score_for_shape[player[combination[1]]]
    return total_score


def rock_paper_scissors_part_two(opponent, score_for_shape, lines):
    shape_counter = 0
    turn_score = 0
    total_score = 0

    for line in lines:
        combination = line.replace(" ", "")
        needed_result = combination[1]

        if needed_result == 'Y':
            turn_score = 3
            shape_counter = score_for_shape[opponent[combination[0]]]
        if needed_result == 'X':
            turn_score = 0
            if combination[0] == 'A':
                shape_counter = score_for_shape["Scissor"]
            if combination[0] == 'B':
                shape_counter = score_for_shape["Rock"]
            if combination[0] == 'C':
                shape_counter = score_for_shape["Paper"]
        if needed_result == 'Z':
            turn_score = 6
            if combination[0] == 'A':
                shape_counter = score_for_shape["Paper"]
            if combination[0] == 'B':
                shape_counter = score_for_shape["Scissor"]
            if combination[0] == 'C':
                shape_counter = score_for_shape["Rock"]

        total_score += turn_score + shape_counter
    return total_score


print("Total Score Part One: " + str(rock_paper_scissors_part_one(score_for_shape, lines)))
print("Total Score Part Two: " + str(rock_paper_scissors_part_two(opponent, score_for_shape, lines)))
