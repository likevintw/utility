import sys


if __name__ == '__main__':
    sys.path.append("..")
    import utility
    path = '/Users/kevin/Desktop/finacial_exchange/'
    path += 'input.txt'
    input = utility.import_file(path)
    '銀行8	19965.00'
    result = []
    text = None
    number = 0
    t, n = 0, 0
    buffer = []
    credit = 0

    for row_data in input:
        text = row_data.split()[0]
        number = float(row_data.split()[1])
        if number > 0:
            buffer.append([text, number])
        elif number < 0:
            credit = number
            while len(buffer) > 0:
                t, n = buffer.pop(0)
                if credit+n <= 0:
                    result.append('{} {:.2f} {:.2f}'.format(t, n, n))
                    result.append('{} {:.2f} {:.2f}'.format(text, -n, 0))
                    credit += n
                else:
                    buffer = [['x', credit+n]]+buffer
                    result.append('{} {:.2f} {:.2f}'.format(t, n, n))
                    result.append('{} {:.2f} {:.2f}'.format(
                        text, credit, credit+n))
                    credit += n
                    break
        else:
            result.append('{} {:.2f} {:.2f}'.format(text, number, number))

    if len(buffer) > 1:
        buffer.pop(0)

    while len(buffer) > 0:
        t, n = buffer.pop(0)
        credit += n
        result.append('{} {:.2f} {:.2f}'.format(t, n, credit))

    buffer = []
    for i in result:
        if i[0] == 'x':
            continue
        else:
            buffer.append(i)

    
    path = '/Users/kevin/Desktop/finacial_exchange/'
    path += 'result.txt'
    utility.export_file(path, buffer)
