import time
print("Built In")
built_in_start_time = time.time_ns()
x = [5, 1, 4, 2, 9, 6, 10, 3, 5, 5, 1, 4, 2, 9, 6, 10, 3, 5, 5, 1, 4, 2, 9, 6, 10, 3, 5, 5, 1, 4, 2, 9, 6, 10, 3, 5]

built_in_end_time = time.time_ns()
sorted_x = sorted(x)
print(sorted_x)
print(built_in_end_time - built_in_start_time)

print("Bubble")
bubble_start_time = time.time_ns()
complete = False

while not complete:
    complete = True

    for i in range(len(x) - 1):
        if x[i] > x[i + 1]:
            complete = False
            x[i], x[i + 1] = x[i + 1], x[i]

bubble_end_time = time.time_ns()
print(x)
print(bubble_end_time - bubble_start_time)

