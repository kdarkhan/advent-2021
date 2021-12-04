def print_board(board):
    print('---------------------------------')
    for l in board:
        print(l)
    print('---------------------------------')

def do_stuff():
    with open('day4.txt') as f:
        lines = f.readlines()

        nums = [int(x) for x in lines[0].strip().split(',')]

        boards = []

        idx = 0
        acc = []
        for line in lines[1:]:
            line = line.strip()
            if line:
                acc.append([int(x) for x in line.split()])
                idx += 1
                if idx == 5:
                    idx = 0
                    boards.append(acc)
                    acc = []

        for n in nums:
            for i in range(len(boards)):
                for j in range(5):
                    for k in range(5):
                        if boards[i][j][k] == n:
                            boards[i][j][k] = None

            for i, board in enumerate(boards):
                ans = board_sum(board)
                if ans:
                    return n * ans


def board_sum(board):
    for i in range(5):
        if list(set([x for x in board[i]])) == [None]:
            return sum([my_sum(board[i]) for i in range(5)])
        if list(set([board[x][i] for x in range(5)])) == [None]:
            return sum([my_sum(board[i]) for i in range(5)])
    return None

def my_sum(lst):
    res = 0
    for x in lst:
        if x:
            res += x
    return res

print(do_stuff())
