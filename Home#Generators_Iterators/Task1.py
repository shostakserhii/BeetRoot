import itertools


def with_index(iterable, start = 0):
    x = list(zip(itertools.count(start), iterable))
    return x

def with_index2(iterable, start = 0):

    i=0

    while i<len(list(iterable)):

        yield (start, iterable[i])
        start += 1
        i += 1

x = [1, 3, 5, 'a', '10', 3]

for i in with_index2(x, 2):
    print(i)