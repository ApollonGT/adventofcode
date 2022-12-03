def outcome(elf, me):
    if elf == 'A':  # Rock
        if me == 'X':  # Rock
            return 3
        if me == 'Y':  # Paper
            return 6
        else:  # scissors
            return 0
    elif elf == 'B':  # Paper
        if me == 'X':  # Rock
            return 0
        if me == 'Y':  # Paper
            return 3
        else:  # scissors
            return 6
    else:  # scissors
        if me == 'X':  # Rock
            return 6
        if me == 'Y':  # Paper
            return 0
        else:  # scissors
            return 3


def new_outcome(elf, me):
    if elf == 'A':  # Rock
        if me == 'X':  # Need to loose
            return 0, 'Z'
        if me == 'Y':  # Need to draw
            return 3, 'X'
        else:  # Need to win
            return 6, 'Y'
    elif elf == 'B':  # Paper
        if me == 'X':  # Need to loose
            return 0, 'X'
        if me == 'Y':  # Need to draw
            return 3, 'Y'
        else:  # Need to win
            return 6, 'Z'
    else:  # scissors
        if me == 'X':  # Need to loose
            return 0, 'Y'
        if me == 'Y':  # Need to draw
            return 3, 'Z'
        else:  # Need to win
            return 6, 'X'


def selection_score(me):
    res = {'X': 1, 'Y': 2, 'Z': 3}
    return res.get(me, 0)


if __name__ == "__main__":
    i = 0
    game = []
    with open('./input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            game.append(line.split())

    # part 1
    total = 0
    new_total = 0
    for turn in game:
        elf = turn[0]
        me = turn[1]
        score = outcome(elf, me) + selection_score(me)
        new_score, me = new_outcome(elf, me)
        new_score += selection_score(me)
        total += score
        new_total += new_score

    print(total)
    # part 2
    print(new_total)
