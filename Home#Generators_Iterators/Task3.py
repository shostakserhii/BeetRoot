class Lists(object):

    def __init__(self, value):
        self._value = [[] for i in range(value)]
        self.value = 0

    def __setitem__(self, item_num, value_in_item):
        self._value[item_num] = value_in_item
        
    def __getitem__(self, item_num):
        return self._value[item_num]

    def __iter__(self):
        self.value = 0
        return self
    
    def __next__(self):
        if self.value < len(self._value):
            temp = self._value[self.value]
            self.value += 1
            return temp
        else: 
            raise StopIteration


building1 = Lists(4)
building1[0]= "00000"
building1[1]= "11111"
building1[2]= "2222222"
building1[3]= "3333333"
for i in building1:
    print(i)
i = iter(building1)
print(list(i))
