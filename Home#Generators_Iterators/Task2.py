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

def in_range(start, end, step = 1):

    if (start > end and step > 0):
        return ("start should be < end if step > 0")
    if (start < end and step < 0):
        return ("start should be > end if step < 0")

    while start != end:

        if (step > 0 and start>end):
            break
        if (step < 0 and start<end):
            break

        yield start

        start += step


x = list(in_range(10, 0, 1))
print(x)
