"""An example of sharing memory with multiprocessing.

In the other multiprocessing example, the results array wasn't visible
outside of the process. This example uses shared memory to fix that.
"""
import multiprocessing


def calc_square(ns, result, v):
    """This example uses a `result` arg rather than a global var."""
    print('incoming v is {}'.format(v.value))
    v.value = 12  # changing the shared variable here \˚ㄥ˚\
    for idx, n in enumerate(ns):
        result[idx] = round(n * n, 2)

    # See below for why this prints strange output
    print('inside process: {}'.format(result))


if __name__ == '__main__':
    nums = [round(pow(1.27, n+1), 2) for n in range(10)]

    # This `result` is shared memory.
    # Example: `i` for integer or `d` for double
    # `10` because the size of the array is 10
    result = multiprocessing.Array('d', 10)

    # Send another variable into the process (`i` for int)
    v = multiprocessing.Value('i', 11)

    # Pass the shared memory into the `args` tuple here:
    p = multiprocessing.Process(target=calc_square, args=(nums, result, v))

    p.start()
    p.join()

    # The `[:]` syntax is to print the elements of the array. If
    # left off, it will print something more like <SynchronizedArray
    # wrapper for <multiprocessing.sharedctypes.c_double_Array_10 object at
    # 0x7f5dbf62c730>>
    print('outside process: {}'.format(result[:]))

    print('the shared var `v` is now {}'.format(v.value))
