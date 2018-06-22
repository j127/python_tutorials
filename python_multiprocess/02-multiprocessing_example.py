import time
import threading
import multiprocessing

square_result = []
print('multiprocessing version')


def calc_square(numbers):
    global square_result
    for n in numbers:
        print('square {}'.format(n * n))
        time.sleep(0.99)
        square_result.append(n * n)

    # In the `if __name__ == '__main__'` section, it can't see
    # `square_result` that holds the data, because this is running in
    # another process. It's visible here though.
    print('within a process, the result is: {}'.format(square_result))


def calc_cube(numbers):
    for n in numbers:
        time.sleep(1.27)
        print('cube {}'.format(n * n * n))


if __name__ == '__main__':
    arr = [pow(2, n) for n in range(10)]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # This is the main process, so it can't see the `square_result`
    # running in the process.
    print('result: {}'.format(square_result))
    print('done')
