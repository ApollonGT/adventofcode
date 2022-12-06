def read_streams():
    streams = []
    with open('./input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            streams.append(line)
    return streams


if __name__ == '__main__':
    streams = read_streams()

    for s in streams:
        length = len(s)
        # Part 1
        for i in range(length - 4):
            vals = list(s[i:i+4])
            if (len(vals) == len(set(vals))):
                print(i + 4)
                break

        # Part 2
        for i in range(length - 14):
            vals = list(s[i:i+14])
            if (len(vals) == len(set(vals))):
                print(i + 14)
                break
