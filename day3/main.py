def get_common(s1, s2, s3=None):
    sa = set(s1)
    sb = set(s2)
    if s3 is not None:
        sc = set(s3)
        return sa.intersection(sb.intersection(sc))
    return sa.intersection(sb)


def get_priority(i):
    return ord(i) - 96 if i.islower() else ord(i) - 38

def get_total_priority(l):
    return sum([get_priority(i) for i in l])


if __name__ == "__main__":
    rucksacks = []

    with open("./input", "r") as f:
        lines = f.readlines()
        groups = []
        group = []
        for line in lines:
            li = line.rstrip('\n')
            l = len(li) // 2
            c1 = li[0:l]
            c2 = li[l:]
            rucksacks.append((c1, c2))
            group.append(li)
            if len(group) == 3:
                groups.append(group)
                group = []

    # Part 1
    total = 0
    for a, b in rucksacks:
        c = get_common(a, b)
        total += get_total_priority(c)
    print(total)

    # Part 2
    total = 0
    for g in groups:
        c = get_common(g[0], g[1], g[2])
        total += get_total_priority(c)
    print(total)
