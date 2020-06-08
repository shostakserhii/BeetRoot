import itertools

def with_index(iterable, start = 0):
    x = list(zip(itertools.count(start), iterable))
    for i in x:
        print(i)
        
def with_index2(iterable, start = 0):
    while start<len(iterable):
        print(f"#{start}, element: {iterable[start]}, {type(iterable[start])}")
        start += 1

x = [1, 3, 5, 'a', '10', 3]


with_index(x)
with_index2(x, 2)