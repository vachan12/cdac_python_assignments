def add_string_grouped(new_string, current_list):
    if not new_string or len(new_string) < 2:
        return current_list

    char_to_find = new_string[1]
    insertion_index = -1

    # Find the last occurrence of a string with the same 2nd character
    for i, s in enumerate(current_list):
        if len(s) >= 2 and s[1] == char_to_find:
            insertion_index = i + 1
    
    if insertion_index != -1:
        current_list.insert(insertion_index, new_string)
    else:
        # If no match is found, just append to the end
        current_list.append(new_string)
    
    return current_list

# Initial list
words = ["dxz", "axz", "bat", "rat", "cat", "pat", "bbc", "bbm", "cbm"]

# User adds 'sat'
words = add_string_grouped("sat", words)
print(f"Grouped List: {words}")