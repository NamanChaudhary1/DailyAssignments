import matplotlib.pyplot as plt

file_sizes = [200, 400, 600, 800, 1000]  
c_times = [1.23, 2.45, 3.68, 4.91, 6.13]  
cpp_times = [1.34, 2.67, 4.00, 5.32, 6.65]  
java_times = [1.45, 2.89, 4.33, 5.76, 7.20]  
r_times = [2.56, 5.12, 7.68, 10.24, 12.80]  
python_times = [3.67, 7.34, 11.01, 14.68, 18.35]  

# Create a table
table_data = [c_times, cpp_times, java_times, r_times, python_times]
headers = ['C', 'C++', 'Java', 'R', 'Python']
table = plt.table(cellText=table_data, colLabels=headers, rowLabels=file_sizes, loc='center')

# Format the table
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Hide axes
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.box(on=None)

# Create a graph
plt.plot(file_sizes, c_times, marker='o', label='C')
plt.plot(file_sizes, cpp_times, marker='o', label='C++')
plt.plot(file_sizes, java_times, marker='o', label='Java')
plt.plot(file_sizes, r_times, marker='o', label='R')
plt.plot(file_sizes, python_times, marker='o', label='Python')
plt.xlabel('File Size (MB)')
plt.ylabel('Time (seconds)')
plt.legend()

# Show the table and graph
plt.show()
