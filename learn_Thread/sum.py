import threading
import random


class SumThread(threading.Thread):
    def __init__(self, lo, hi, l):
        threading.Thread.__init__(self)
        self.lo = lo
        self.hi = hi
        self.l = l
        self.sum = 0

    def run(self):
        self.set_sum()

    def set_sum(self):
        for i in range(self.lo, self.hi):
            self.sum += self.l[i]
        return

    def get_num(self):
        return self.sum

    def print_list(self):
        str_list = ""
        for i in range(self.lo, self.hi):
            str_list += str(self.l[i]) + "; "
        return str_list


def sum(num, n_threads):
    sum = 0
    length = len(num)
    list_thread = []

    i = 0
    while i < n_threads:
        lo = int((i * length) / n_threads)
        hi = int((i + 1) * length / n_threads)
        thread = SumThread(lo, hi, num)
        list_thread.append(thread)
        list_thread[i].start()
        i += 1

    j = 0
    while j < n_threads:
        list_thread[j].join()
        sum += list_thread[j].get_num()
        print(f"Thread {j + 1}: {list_thread[j].print_list()}")
        j += 1
    return sum


if __name__ == '__main__':
    num = []
    n = int(input('Input n: '))
    for i in range(n):
        num.append(random.randint(0, 10))
    print(f"List: {num}")
    n_thread = int(input('Input number of thread: '))
    sum = sum(num, n_thread)
    print(f"Sum: {sum}")
