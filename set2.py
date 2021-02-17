alphabet={'a','b','c',2}
number={1,2,3,'a'}
print(number.intersection(alphabet))
print(alphabet.intersection(number)) #중괄호

print(number&alphabet)

print(number.difference(alphabet))
print(alphabet.difference(number))
print(number|alphabet)
print(number.union(alphabet))
number.add(5)
print(number)
number.remove(5)
print(number)