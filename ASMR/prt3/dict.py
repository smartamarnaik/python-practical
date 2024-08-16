new = {
    1 : 'amar',
    2 : 'prem',
    3 : 'atharv',
    4 : 'samii',
    5 : 'yash'
}

new1 = new.copy()
print("copy : " , new1)

a = new1.get(3)
print("Get_function",a)

print('ITEM()',new1.items())

print('keys() :',new1.keys())

print('pop() :',new1.pop(2))

print('popitem() : ',new1.popitem())