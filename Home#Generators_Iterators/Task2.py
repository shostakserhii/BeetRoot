"""def in_range(start, end, step = 1):

    new = []

    if (start > end and step > 0):
        return ("start should be < end if step > 0")
    if (start < end and step < 0):
        return ("start should be > end if step < 0")

    while start != end:
        if (step > 0 and start>end):
            return new
        if (step < 0 and start<end):
            return new
        new.append(start)
        start += step

    return new

x = in_range(0, -100, -5)
print(x)
"""

def in_range(start, end = None, step = 1):
    if end == None:
        end = start
        start = 0
    if (start > end and step > 0):
        return []
    if (start < end and step < 0):
        return []

    while start != end:

        yield start

        start += step


x = list(in_range(0, 10 ,1))
print(x)

