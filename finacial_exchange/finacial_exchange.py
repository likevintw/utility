

import sys
sys.path.append("..")
import utility

if __name__ == '__main__':
    input = utility.import_file('input.txt')
    result = []
    buffer = []
    amount = 0
    number = 0
    text = None
    for i in range(len(input)):
        row_data = input[i]
        text = row_data.split()[0]
        number = float(row_data.split()[1])

        if amount == 0:
            words = "{} {} {}".format(text, number, amount)
            result.append(words)
            amount = amount+number
            continue

        if number < 1:
            buffer.append([text, round(number, 2)])
            continue

        if number+amount > 0:
            buffer.append([text, round(number, 2)])
        else:
            words = "{} {:.2f} {:.2f}".format(text, -amount, amount)
            result.append(words)
            buffer.append([text, round(number-amount, 2)])

            while len(buffer) > 0:
                t, n = buffer.pop(0)
                words = "{} {:.2f} {:.2f}".format(text, n, amount)
                amount = amount+n
                t, n = buffer.pop(0)
                words = "{} {:.2f} {:.2f}".format(text, n, amount)
                amount = amount+n

    while len(buffer) > 0:
        t, n = buffer.pop(0)
        result.append(t+" "+str(round(n, 2)))
        amount = amount+n

    result.append('amount '+str(round(amount, 2)))
    utility.export_file('result.txt', result)
