import random
first_list = [1,2,3,4,5,6,7,8,9,10]
second_list = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < 10:
    first_list[i]=random.randrange(0,10)
    second_list[i]=random.randrange(0,10)
    i += 1
print(first_list)
print(second_list) 
first_set = set(first_list)
second_set = set(second_list)
print("Common nunbers are: ", first_set.intersection(second_set))