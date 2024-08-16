set1 = {'amar',2,66,'prem',True}
set2 ={2,5,8,556,66,'letsdoit'}

set1.add("letsadd")
print("Item add: ",set1)

set3 = set1.copy()
print("set_3 copied from set_1 :",set3)


print("Union :",set1 | set2)

print("Interection :", set1 & set2)

print("difference: ",set1 - set2)

print("SYMMERIC_difference: ",set1 ^ set2)

set1.update(set2)
print("update:", set1)

set2.symmetric_difference_update(set1)
print("symmetric_difference_update", set2)

set1.discard(True)
print("Discard successful: ",set1)