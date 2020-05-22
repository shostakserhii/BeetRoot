class Mathematician():

    def __init__(self, l=[1, -2, 3, -4], years = [2001, 1884, 1995, 2000, 2003, 2020]):
        self.l=l
        self.years = years

    def list_of_squares(self):
        new_list = []
        for item in self.l:
            new_list.append(item*item)
        return new_list


    def remove_positives(self):
        new_list = self.l
        for item in new_list:
            if item > 0:
                new_list.remove(item)
        return new_list

    def filter_leaps(self):
        new_list = []
        for item in self.years:
            if item % 4 == 0 or (item % 100 != 0 and item % 400 == 0):
                new_list.append(item)
        return new_list

math = Mathematician()

print(f" {math.l} == {math.list_of_squares()}")
print(f" {math.l} == {math.remove_positives()}")
print(f" {math.years} == {math.filter_leaps()}")