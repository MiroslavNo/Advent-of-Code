import requests
SESSIONID = '53616c7465645f5fa7ba7039f2dd45b2505a1f333d0ae59fd1d47b46210b10bf45bbc74688b6d706bbfd58cf8989b14df1e29f17abb60aa01f2bc7399f3124bb'


def is_unique(s, x):
    for i in range(x):
        for ii in range(x):
            if ii <= i:
                continue
            if s[i] == s[ii]:
                return False
    return True


def solve_puzzle(input_str):
    r = dict()
    line_counter = 0
    ls = False
    curr_size = 0
    curr_position = 'root'

    for line in input_str.split('\n'):
        line_counter += 1

        if line_counter == 1:
            if line != '$ cd /':
                print('ERR: First line not as expected: {}'.format(line))
                break
            else:
                continue
        if line_counter == 2:
            if line != '$ ls':
                print('ERR: Second line not as expected: {}'.format(line))
                break

        if line == '$ ls':
            print('line {} - activate ls'.format(line_counter))
            ls = True
            curr_size = 0
            continue

        if ls:
            if line.startswith('$'):
                print('line {} - deactivate ls'.format(line_counter))
                ls = False
                print('setting size {} to {}'.format(curr_size, curr_position))
                r[curr_position] = curr_size

            elif line.startswith('dir'):
                pass
            elif line == '':
                continue
            else:
                curr_size += int(line.split(' ')[0])

        if not ls:
            if line.startswith('$ cd'):
                if line == '$ cd ..':
                    curr_position = curr_position.rsplit('/', 1)[0]
                    print('line {} - setting curr_position to {}'.format(line_counter, curr_position))
                else:
                    curr_position = curr_position + '/' + line[5:]
                    print('line {} - setting curr_position to {}'.format(line_counter, curr_position))

            if line == '$ ls':
                print('ERR: not expected - user called $ ls on line {} twice in a row'.format(line_counter))
                break

    # TODO set curr_size into dict
    print('setting size {} to {}'.format(curr_size, curr_position))
    r[curr_position] = curr_size
    print(r)

    sum = dict()
    for path, size in r.items():
        path_array = path.split('/')
        curr_path = ''
        for folder in path_array:
            curr_path = curr_path + '/' + folder
            curr_size = sum.get(curr_path, 0)
            sum[curr_path] = curr_size + size

    print(sum)
    result_size = 0
    for folder, size in sum.items():
        if size < 100000:
            result_size += size

    print(result_size)

    #PART TWO
    total_size = sum['/root']
    unused_space = 70000000 - total_size
    required_space = 30000000 - unused_space

    min_delete = 30000000
    for folder, size in sum.items():
        if size > required_space:
            if size < min_delete:
                min_delete = size

    print(min_delete)


day = 7
puzzle_str = requests.get('http://adventofcode.com/2022/day/{day}/input'.format(day=day), cookies={'session': SESSIONID}).text

# puzzle_str = '$ cd /\n' \
#             '$ ls\n' \
#             'dir a\n' \
#             '14848514 b.txt\n' \
#             '8504156 c.dat\n' \
#             'dir d\n' \
#             '$ cd a\n' \
#             '$ ls\n' \
#             'dir e\n' \
#             '29116 f\n' \
#             '2557 g\n' \
#             '62596 h.lst\n' \
#             '$ cd e\n' \
#             '$ ls\n' \
#             '584 i\n' \
#             '$ cd ..\n' \
#             '$ cd ..\n' \
#             '$ cd d\n' \
#             '$ ls\n' \
#             '4060174 j\n' \
#             '8033020 d.log\n' \
#             '5626152 d.ext\n' \
#             '7214296 k'

solve_puzzle(puzzle_str)
