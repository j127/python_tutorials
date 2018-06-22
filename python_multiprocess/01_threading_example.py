import time
import threading

square_result = []
print('threading version')


def calc_square(numbers):
    global square_result
    for n in numbers:
        print('square {}'.format(n * n))
        time.sleep(0.99)
        square_result.append(n * n)
    print('visible here too: {}'.format(square_result))


def calc_cube(numbers):
    for n in numbers:
        time.sleep(1.27)
        print('cube {}'.format(n * n * n))


if __name__ == '__main__':
    arr = [pow(2, n) for n in range(10)]
    p1 = threading.Thread(target=calc_square, args=(arr,))
    p2 = threading.Thread(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('result: {}'.format(square_result))
    print('done')
