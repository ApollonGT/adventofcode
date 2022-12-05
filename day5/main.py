def read_cargo_plan():
    cargo = []
    plan = []
    with open('./input', 'r') as f:
        i = 0
        lines = f.readlines()
        for idx, line in enumerate(lines):  # Cargo
            if line == '\n':
                i = idx
                break
            cargo.append([line[1], line[5], line[9],
                          line[13], line[17], line[21],
                          line[25], line[29], line[33]])
    cg = [[] for i in range(9)]
    cargo.reverse()
    for idx, r in enumerate(cargo):
        if idx == 0:
            continue
        for cidx, c in enumerate(r):
            if c != ' ':
                cg[cidx].append(c)

    with open('./input', 'r') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):  # Plan
            if idx > i:
                msg = line.split()
                plan.append([int(msg[1]), int(msg[3]) - 1, int(msg[5]) - 1])
    return cg, plan


if __name__ == '__main__':
    # Part 1
    cargo, plan = read_cargo_plan()
    for idx,p in enumerate(plan):
        cargo[p[2]] += list(reversed(cargo[p[1]][-p[0]:]))
        cargo[p[1]] = cargo[p[1]][:len(cargo[p[1]]) - p[0]]

    res = []
    for c in cargo:
        res.append(c[-1])
    print(''.join(res))

    # Part 2
    cargo, plan = read_cargo_plan()
    for idx,p in enumerate(plan):
        cargo[p[2]] += cargo[p[1]][-p[0]:]
        cargo[p[1]] = cargo[p[1]][:len(cargo[p[1]]) - p[0]]

    res = []
    for c in cargo:
        res.append(c[-1])
    print(''.join(res))
