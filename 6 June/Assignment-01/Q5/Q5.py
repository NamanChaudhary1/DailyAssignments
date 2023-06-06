import random

list1 = [random.randint(10,30) for _ in range(10)]
list2 = [random.randint(10,30) for _ in range(10)]

print ("List 1:",list1)
print ("List 2:",list2)

#(i)
common = list(set(list1) & set(list2))
print("Common:",common)

#(ii)
unique = list(set(list1)^set(list2))
print("Unique",unique) 

# (iii) 
min_value = min(min(list1), min(list2))
print("Minimum value:", min_value)

# (iv)
max_value = max(max(list1), max(list2))
print("Maximum value:", max_value)

# (v)
sum_of_lists = sum(list1) + sum(list2)
print("Sum of lists:", sum_of_lists)