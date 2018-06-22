"""Bad multiprocessing, without lock.

The total might be different on different runs.
"""
import time
import multiprocessing


def deposit(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value + 1


def withdraw(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value - 1


if __name__ == '__main__':
    NUM_RUNS = 20
    profit_values = []
    currency = 'gold bars'
    print('The output should always be 200 {}, but sometimes it will be wrong.'.format(currency))
    print('The program will now run {} times...'.format(NUM_RUNS))
    for _ in range(NUM_RUNS):
        balance = multiprocessing.Value('i', 200)
        d = multiprocessing.Process(target=deposit, args=(balance,))
        w = multiprocessing.Process(target=withdraw, args=(balance,))

        d.start()
        w.start()

        d.join()
        w.join()

        if balance.value == 200:
            print('balance value is {}'.format(balance.value))
        else:
            off_by = balance.value-200
            profit_values.append(off_by)
            print('balance value is {} (ERROR: your bank account is off by {} {})'.format(balance.value, off_by, currency))
    profit = sum(profit_values)
    print('your bank account is now off by {} {}.'.format(profit, currency))
