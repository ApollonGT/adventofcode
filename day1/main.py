if __name__ == "__main__":
    i = 0
    cal = [0]
    with open('./input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if len(line) < 2:
                i += 1
                cal.append(0)
            else:
                cal[i] += int(line)

    # part 1
    print(max(cal))
    # part 2
    cal = sorted(cal, reverse=True)
    print(sum(cal[0:3]))


