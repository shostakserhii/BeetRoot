#Task_1 The greatest number from 10 random ones
import random
random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
biggest_num = 0
print(random_list)
while i < len(random_list):
    random_list[i]=random.randrange(0,1000)
    print(f"{i+1} element is {random_list[i]}")
    if biggest_num < random_list[i]:
        biggest_num = random_list[i]
    i += 1
print("Biggest number is", biggest_num)