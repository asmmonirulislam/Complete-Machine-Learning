l1 = []
for i in range(1, 11):
    if(i%2==0):
        l1.append(i)
print(*l1) # 2 4 6 8 10



l2 = [i for i in range(1, 11) if i%2==0]
print(*l2) # 2 4 6 8 10