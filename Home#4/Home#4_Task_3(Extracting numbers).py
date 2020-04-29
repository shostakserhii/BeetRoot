#int_list = [i for i in range(100) if i % 7 == 0 and i % 5 != 0]
#print(int_list)
n=0
i=0
listo = []
while i<100:
    if i %7 == 0 and i % 5 !=0:
        listo.append(i)
        i += 1
    else: i += 1
print (listo)