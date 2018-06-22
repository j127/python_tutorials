import time
from multiprocessing import Pool


def f(nums=1000):
    total = 0
    for n in range(nums):
        total += n * n
    return total


if __name__ == '__main__':
    # arr = [round(pow(1.27, n+1), 2) for n in range(1000)]

    t1 = time.time()

    # Tip: you can set the number of processes like this: Pool(processes=3)
    p = Pool()

    # Divide the work among available CPUs on the machine
    result = p.map(f, range(10000))

    p.close()
    p.join()

    print('pool took: {}'.format(time.time()-t1))

    t2 = time.time()
    result = []
    for n in range(10000):
        result.append(f(n))

    print('serial processing took: {}'.format(time.time()-t2))

    print('the more computationally intensive, the better Pool should perform')
