import itertools

def with_index(iterable, start = 0):
    x = list(zip(itertools.count(start), iterable))
    return x
        
def with_index2(iterable, start = 0):

    while start<len(iterable):
        yield (start, iterable[start])
        start += 1

x = [1, 3, 5, 'a', '10', 3]

for i in with_index2(x, 2):
    print(i)
