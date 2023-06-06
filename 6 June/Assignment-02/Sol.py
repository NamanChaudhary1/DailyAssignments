#To sort we have to make a common custom
#sorting approach

L = ["Ram", 1, "Shyam", 2, "Aman", 3]
print("Original list:", L)

def custom_sort(elem):
    # Convert numbers to a higher value to be sorted after strings
    if isinstance(elem, int):
        return str(elem)
    else:
        return elem
    
L.sort(key=custom_sort)
print(L)