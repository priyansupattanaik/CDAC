list = [10, 20 ,30,40,50, 60, 70, 80, 90, 100]
print(list)

list.append(999)
print(list)

list.append([55,66,77])
print(list)

list.extend([1000])
print(list)

list.insert(10, 555)
print(list)

list.pop()
print(list)

list.pop(0)
print(list)

list.remove(555)
print(list)

print(list.index(999))

print(len(list))

list2 = list.copy()
print(list2)

list.clear()
print(list)