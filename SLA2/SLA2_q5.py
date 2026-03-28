# 1. The original list provided in your assignment
lst = [12, 1, 3, 7, 8, 5, 8]

# 2. Find the highest number to determine how long the new list needs to be.
# Since the max value is 12, we need 13 slots (0 through 12).
max_val = max(lst)

# 3. Create the "initial list" filled with -1.
lst1 = [-1] * (max_val + 1)

# Display the initial state (with one value set as per your assignment example)
initial_display = lst1.copy()
initial_display[1] = 1 
print("initial list")
print(f"lst1={initial_display}")

# 4. The Exchange: 
# We loop through 'lst' and use the VALUE as the INDEX for 'lst1'.
# We store the original POSITION (index) as the value.
for index, value in enumerate(lst):
    lst1[value] = index

# 5. Display the final modified list
print("\nmodified list")
print(f"lst1={lst1}")