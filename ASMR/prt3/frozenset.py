list1 = frozenset([10,32,58,3,55,77])
list2 = frozenset([57,7,34,6,78,88,23])

list3 = list1.copy()
print("Copying :",list3)

union_1 = list1.union(list2)
print('Union () :', union_1)

inter_1 = list2.intersection(list1)
print('intersection () :',inter_1)

dif_1 = list1.difference(list2)
print("difference() :" , dif_1)

sym_dif = list1.symmetric_difference(list2)
print("symmetric_diference ():" , sym_dif)

demo = list1.isdisjoint(list2)
print(demo)

demo1 = list1.issubset(list3)
print(demo1)

demo2 = list1.issuperset(list3)
print(demo2)