list = [10, 20 ,30,40,50]

print(list)  

list.extend([60,70,80])
print(list)

list.append(90)
print(list)

list.extend("CDAC")
print(list)

list.insert(0, 5)
print(list)

list.remove(30)
print(list)

#explain the append?
#append is used to add a single element to the end of the list. It takes one argument, which is the element you want to add. When you use append, it adds that element as a single item to the end of the list, regardless of whether it's a single value or another list.

#explain the extend?
#extend is used to add multiple elements to the end of the list. It takes an iterable (like a list, tuple, or string) as an argument and adds each element of that iterable to the end of the list. When you use extend, it iterates through the provided iterable and adds each element individually to the list.

list.pop()
print(list)

list.pop(0)
print(list) 