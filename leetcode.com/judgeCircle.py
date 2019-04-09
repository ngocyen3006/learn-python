# https://leetcode.com/problems/robot-return-to-origin/

def judgeCircle(moves):
    move_dic = {'U': 0,
                'D': 0,
                'R': 0,
                'L': 0}
    for m in moves:
        move_dic[m] += 1
    move = [move_dic['R'] - move_dic['L'], move_dic['U'] - move_dic['D']]
    return move == origin


if __name__ == '__main__':
    testcase = {'UD': True,
                'LL': False}

    for k in testcase.keys():
        print(judgeCircle(k) == testcase[k])
        print('-' * 10)
