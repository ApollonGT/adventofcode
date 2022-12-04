## DAY 4

if __name__ == '__main__':
    c = 0
    fc = 0

    with open('./input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            pair = line.split(',')

            left = pair[0].split('-')
            l_left = [i for i in range(int(left[0]), int(left[1]) + 1)]
            left = [f"'{str(i)}'" for i in l_left]
            left = ''.join(left)

            right = pair[1].split('-')
            l_right = [i for i in range(int(right[0]), int(right[1]) + 1)]
            right = [f"'{str(i)}'" for i in l_right]
            right = ''.join(right)

            if len(left) < len(right):
                if left in right:
                    fc += 1
            elif right in left:
                fc += 1

            if len(set(l_left).intersection(l_right)) > 0:
                c += 1
    # Part 1
    print(fc)
    # Part 2
    print(c)
