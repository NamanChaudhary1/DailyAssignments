L = ["One", "Two", "Three", "Four", "Five"]

# Open the file in write mode
with open("output.txt", "w") as file:
    # Iterate over the elements in the list
    for element in L:
        # Get the length of the element
        length = len(element)
        # Write to the file in the desired format
        file.write(f"{element}, {length}\n")
