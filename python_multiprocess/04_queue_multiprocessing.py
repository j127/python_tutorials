"""An example of `multiprocessing.Queue`.

There is also a `queue` module for in-process memory. It's for sharing
data between threads.
"""
import multiprocessing


def calc_square(ns, q):
    """The child process."""
    for n in ns:
        # `q` is a queue (FIFO).
        q.put(round(n * n, 2))


if __name__ == '__main__':
    nums = [round(pow(1.27, n+1), 2) for n in range(10)]

    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(nums, q))

    p.start()
    p.join()

    while q.empty() is False:
        # Get items from the queue
        print(q.get())
