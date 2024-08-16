list1= [2,4,8.6,6,1,3,5,7]
list1.reverse()
print("Reverse :",list1)
list1.sort()
print("Sorted :",list1)


list2 = [1,5,7,5,'amar',4.6]
list1.extend(list2)
print("Extended :",list1)
print("Slicing :",list1[1:3])
while True:
    a = input("Enter :")
    if a == 'exit'.lower():
        break
    list2.append(a)
print("Appended:",list2)
list2.insert(0,"Samii")
print("Inserted :" ,list2)
print("Present at :",list2.count('amar'))

print("Present at :",list1.index(7))
list2.remove('amar')
list1.pop(0)
print(list2)
print(list1)

