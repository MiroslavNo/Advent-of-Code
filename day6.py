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


def solve_puzzle(input_str, unique_seq_length):
    for i in range(len(input_str)-(unique_seq_length-1)):
        if is_unique(input_str[i:i+unique_seq_length], unique_seq_length):
            print(i+unique_seq_length)
            break


day = 6
puzzle_str = requests.get('http://adventofcode.com/2022/day/{day}/input'.format(day=day), cookies={'session': SESSIONID}).text

solve_puzzle(puzzle_str, 4)
solve_puzzle(puzzle_str, 14)
