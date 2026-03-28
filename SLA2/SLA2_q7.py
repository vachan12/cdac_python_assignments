def add_by_last_digit():
    # Initialize a list with 10 empty sub-lists (for digits 0-9)
    dynamic_list = [[] for _ in range(10)]
    
    # Pre-filling with your example data for context
    example_data = [10, 30, 20, 40, 11, 31, 41, 31, 22, 32, 42]
    for val in example_data:
        dynamic_list[val % 10].append(val)

    print(f"Current State: {dynamic_list}")

    try:
        user_input = int(input("Enter a number to add: "))
        last_digit = user_input % 10
        
        # Dynamically append to the sub-list at the index of the last digit
        dynamic_list[last_digit].append(user_input)
        
        # Removing trailing empty lists to match your example format if needed
        # but keeping the structure intact for logic.
        print(f"Resultant List: {dynamic_list}")
    except ValueError:
        print("Please enter a valid integer.")

add_by_last_digit()