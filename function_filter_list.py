def filter_list(input_list, filter_num):
    """
    Filters a list to keep only elements less than or equal to a given filter number/threshold.
    
    Uses the built-in 'filter' function with a lambda expression for efficient, 
    one-line list filtering.
    
    Args:
        input_list (list): The list of numbers to be filtered.
        filter_num (int): The maximum value to retain in the list.
    
    Returns:
        list: A new list containing the filtered elements.
    """
    return list(filter(lambda item: item <= filter_num, input_list))

def parse_list_input(input_str):
    """
    Parses a string input (e.g., "[1,2,3]" or "1,2,3") into a list of integers.

    Performs validation to ensure all elements are valid integers.

    Args:
        input_str (str): The raw string input from the user.

    Returns:
        list: A list of integers.

    Raises:
        ValueError: If the input is empty or contains non-integer elements.
    """
    try:
        # Remove brackets and split by commas
        input_str = input_str.strip().strip('[]')
        if not input_str:
            raise ValueError("List cannot be empty")
       
        # Convert input string to list of integers
        input_list = [int(x) for x in input_str.split(',')]
        return input_list
    except ValueError:
        raise ValueError("Please enter a valid list of integers (e.g., [1,2,3] or 1,2,3)")


# I was unsure if the question intended for the user to input both the list and the filter. 
# This try statement handles errors associated with inputting a list
while True:
    try:
        input_str = input("Enter the list of integers (e.g., [1,2,3] or 1,2,3): ")
        input_list = parse_list_input(input_str)
        break
    except ValueError as e:
        print(f"Error: {e}")


#I wanted to make sure that an integer was input by the user, so I used a try statement
while True:
    try:
        
        # Use float() first to safely catch all non-numeric inputs
        filter_num = float(input("Enter the filter value: "))
        
        # Check if the float value is actually an integer (no decimal part)
        if not filter_num.is_integer():
            raise ValueError("Filter number must be an integer")
        
        filter_num = int(filter_num)

        # Execute the core logic and print the result
        result = filter_list(input_list, filter_num)
        print(f"Filtered list (elements <= {filter_num}): {result}")
        break
    except ValueError as e:
        if str(e) == "Threshold must be an integer":
            print(f"Error: {e}")
        else:
            print("Error: Please enter a valid number")

