

ar2D = [[1,2,3],
        [4,5,6],
        [7,8,9]]
sum_a=0
sum_b=0
for each in range(len(ar2D)):
    sum_a+= (ar2D[each][each])

for each in range(len(ar2D)):
    sum_b+=(ar2D[each][(len(ar2D)-1)-each])


return abs(a-b)
