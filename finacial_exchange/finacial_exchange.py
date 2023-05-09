import sys


if __name__ == '__main__':
    sys.path.append("..")
    import utility
    input = utility.import_file('input.txt')
    result = []
    flag = 0
    text = None
    number = 0
    t, n = 0, 0
    lenth = len(input)
    buffer = []
    amount = 0

    for row_data in input:
        text = row_data.split()[0]
        number = float(row_data.split()[1])
        print(amount)
        if number > 0:
            buffer.append([text, number])
            continue

        if amount > 0:
            if amount+number >= 0:
                # print('{} {:.2f} {:.2f}'.format(text, -amount, 0))
                result.append('{} {:.2f} {:.2f}'.format(text, number, 0))
                amount = amount+number
                continue
            else:
                result.append('{} {:.2f} {:.2f}'.format(text, -amount, 0))
                amount = amount+number
        while len(buffer) > 0:
            t, n = buffer.pop(0)
            if n+number >= 0:
                # print('{} {:.2f} {:.2f}'.format(t, n, n))
                # print('{} {:.2f} {:.2f}'.format(
                #     text, amount, amount+n))
                result.append('{} {:.2f} {:.2f}'.format(t, n, n))
                result.append('{} {:.2f} {:.2f}'.format(
                    text, amount, amount+n))
                amount = amount+n
                break
            else:
                # print('{} {:.2f} {:.2f}'.format(t, n, n))
                # print('{} {:.2f} {:.2f}'.format(text, -n, 0))
                result.append('{} {:.2f} {:.2f}'.format(t, n, n))
                result.append('{} {:.2f} {:.2f}'.format(text, -n, 0))
                amount += n+number

    while len(buffer) > 0:
        t, n = buffer.pop(0)
        # print('{} {:.2f}'.format(t, n, n))
        result.append('{} {:.2f}'.format(t, n, n))

    result.append('amount '+str(round(amount, 2)))
    utility.export_file('result.txt', result)
