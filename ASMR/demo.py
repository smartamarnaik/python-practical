def add_fun(a,b):
    c = a + b
    # print(c)
    return c

def sub_fun(a,b):
    c = a - b
    # print(c)
    return c

def multiply_fun(a,b):
    c = a * b
    # print(c)
    return c

def div_fun(a,b):
    c = a / b
    # print(c)
    return c



print(add_fun(10,20))
print(sub_fun(10,20))
print(multiply_fun(10,20))
print(div_fun(10,20))

add = lambda a,b : a + b
sub = lambda a,b : a - b
mul = lambda a,b : a * b
div = lambda a,b :  a / b

print('\n',add(10,20))
print(sub(10,10))
print(mul(10,30))
print(div(50,10))


