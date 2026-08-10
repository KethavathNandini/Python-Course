# filter(function ,sequence)

seq = [1,2,3,4]
odd = lambda x:x ** 2
filtered_op = filter(odd,seq)
print(list(filtered_op))

# map
seq = [1,2,3,4]
odd = lambda x:x ** 2
filtered_op = map(odd,seq)
print(list(filtered_op))
