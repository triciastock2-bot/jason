import numpy as np
data_type = [('mame', 'S15'), ('class', int), ('height', float)]
students_details = [('John', 20, 6.1), ('Alice', 19, 5.7), ('Bob', 10, 5.8)]

students =np.array(students_details,dtype=data_type)
print("Original Array")
print(students)
print("\nSorted by height")
print(np.sort(students, order='height'))