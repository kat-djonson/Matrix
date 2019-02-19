#!/usr/bin/python

def gen_table(n):
    result = []
    inner_list = [0]*n
    for elem in range(n):
        result += [inner_list[:]]
    return result


def print_table(table):
    for spisok in table:
        for element in spisok:
            print(element, end=' ')
        print(' ')


def get_steps(table, pos_x, pos_y):
    da = []
    da += [[pos_x-2, pos_y+1]]
    da += [[pos_x-2, pos_y-1]]
    da += [[pos_x-1, pos_y-2]]
    da += [[pos_x+1, pos_y-2]]
    da += [[pos_x+2, pos_y-1]]
    da += [[pos_x+2, pos_y+1]]
    da += [[pos_x+1, pos_y+2]]
    da += [[pos_x-1, pos_y+2]]
    tada = []
    for elem in da:
        if 0 <= elem[0] <= len(table)-1 and \
           0 <= elem[1] <= len(table)-1 and \
           table[elem[0]][elem[1]] == 0:
            tada += [elem]
    return tada


def make_step(t, pos_x, pos_y):
    step = get_steps(t, pos_x, pos_y)
    weights = []
    for elem in step:
        weights += [len(get_steps(t, elem[0], elem[1]))]
    min_min = min(weights)
    go_coord = step[weights.index(min_min)]
    t[go_coord[0]][go_coord[1]] = t[pos_x][pos_y] + 1
    return go_coord


t = gen_table(5)
t[1][2] = 1
print_table(t)
print(make_step(t, 1, 2))
print_table(t)
