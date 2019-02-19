def read_voc():
    result = dict()  # result = {}
    with open('vocabulary', 'r') as f:
        voc = f.readlines()
        for line in voc:
            l = [i.strip() for i in line.split('|')]
            word = l[0]
            values = l[1:]
            result[word] = values
    return result


def add_word():
    word = input('Add your word: ')
    values = []
    while True:
        values += [input('Add you value or values: ')]
        if values[-1] == 'всё':
            break

    string = word
    for value in values[:-1]:
        string += ' | ' + value

    string += '\n'
    with open('vocabulary', 'a') as f:
        f.write(string)

def mega_print():
    x = read_voc()
    for word in sorted(x):
        print(word)
        for value in x[word]:
            print(" "*len(word) + value)
        print()


if __name__ == '__main__':
    while True:
        what = input('What do you want to do, Human? ')
        if what == 'читать':
             mega_print()
        elif what == 'писать':
            add_word()
        elif what == 'выход':
            break
        else:
            print('Please enter "exit", "read" or "write"')



