num = '8461'
mult = 1
result = [int(index) for index in num]
result.reverse()
print (result)
result.sort()
print (result)
for i in range(1, 4):
    mult *= result[i]
print (mult)