# Understanding List

fitness_data = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]

first_index = 0
print(fitness_data[first_index])

last_index = len(fitness_data) -1
print(fitness_data[last_index])

fitness_data = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
slice_list = fitness_data[1:3]
print(slice_list)

fitness_data = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
list_daily_steps = []
# Write your code here to correctly assign the slice to list_daily_steps
list_daily_steps = fitness_data[1:(len(fitness_data) -1)]
print(list_daily_steps)

list_daily_steps = [7000, 5500, 10300, 8000, 1200, 2000, 5000]
for steps in list_daily_steps:
    print(steps)

for index in range(5):
  print(index)