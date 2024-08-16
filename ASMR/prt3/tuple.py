tup = (1,'prem',4,6,34,'amar')
print("Length of tupple :",len(tup))
print("Type :",type(tup))
print("Slicing :",tup[:2])

tup1 = list(tup)
tup1.append("wedidit")
tup = tuple(tup1)
print(tup)

print(tup.count("prem"))
print(tup.index(34))

