import multiprocessing

result = []


def calc_square(ns):
    global result
    for n in ns:
        r = round(n * n, 2)
        result.append(r)
    print('inside process: {}'.format(result))


if __name__ == '__main__':
    nums = [round(pow(1.27, n+1), 2) for n in range(10)]
    p = multiprocessing.Process(target=calc_square, args=(nums,))

    p.start()
    p.join()

    print('outside process: {}'.format(result))


