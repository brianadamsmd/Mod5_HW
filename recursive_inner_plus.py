
def recursive_inner_plus_then_increment(input_nested_list):
    """
    Validates a list (only int or list), finds all innermost nested lists, 
    and increments all integers within them by one, using ONLY recursion.
    """

    # -----------------------------------------------
    # 1. VALIDATION FUNCTION: Checks for only int or list across all levels.
    # -----------------------------------------------
    def validate_recursive(lst):
        if not lst:
            return True
        
        # Split the list into a head element and a tail element.
        head = lst[0]
        tail = lst[1:]
        
        # Recursive Step: Check the head element.
        if isinstance(head, int):
            # Integer is valid. Recurse on the rest of the list (tail).
            return validate_recursive(tail)
        
        elif isinstance(head, list):
            # List is valid. Check its contents recursively AND check the rest of the list (tail).
            return validate_recursive(head) and validate_recursive(tail)
        
        else:
            # Found an invalid type. Stop and return False.
            return False

    if not validate_recursive(input_nested_list):
        return "Error: Input list or its nested lists contain elements that are not integers or lists."

    # -------------------------------------------------------------
    # 2. PROCESSING FUNCTION: Finds and increments all innermost lists.
    # -------------------------------------------------------------

    def increment_recursive(lst):
        # Base Case 1: Empty list. Return the empty list.
        if not lst:
            return []

        # Create the head and the tail.
        head = lst[0]
        tail = lst[1:]
        
        # Check if a list contains any further lists.
        def contains_nested_list(check_lst):
            if not check_lst:
                return False
            
            # Check the head element.
            if isinstance(check_lst[0], list):
                return True
            
            # Recurse on the tail.
            return contains_nested_list(check_lst[1:])

        # --- Check the Head ---
        
        if isinstance(head, int):
            # Case A: Head is an integer. Return it and recurse on the tail.
            return [head] + increment_recursive(tail)
        
        elif isinstance(head, list):
            # Case B: Head is a list.
            
            if contains_nested_list(head):
                # Subcase B.1: The nested list is NOT innermost. - Recurse into the nested list, and then recurse on the tail.
                return [increment_recursive(head)] + increment_recursive(tail)
            
            else:
                # Subcase B.2: The nested list IS innermost (contains only integers).
                
                # --- Increment the Innermost List (Recursively) ---
                def modify_innermost(inner_lst):
                    if not inner_lst:
                        return []
                        
                    innermost_head = inner_lst[0]
                    innermost_tail = inner_lst[1:]

                    return [innermost_head + 1] + modify_innermost(innermost_tail)

                # Replace the original innermost list with the modified one,
                # then continue recursing on the tail of the outer list.
                return [modify_innermost(head)] + increment_recursive(tail)

    return increment_recursive(input_nested_list)

# ---------------------------------
# CODE TESTING SECTION
# ---------------------------------
list_input = [1, 2, 3, 4, [5, 6, 7, [8, 9,1,3,4,65,6,43,3,4,5,56,3,4,5,56,45,4,3],45,4,3],[8, 9,1,3,4,65,6,43,3,4,5,56,[8, 9,1,3,4,65,6,43,[3,4,5,56,45,4,3],3,4,5,56,45,4,3],45,4,[8, 9,1,3,4,65,6,43,[3,4,5,56,[1,2,3,4],45,4,3],3]]]
print(f"Original Input: {list_input}")
print(f"Recursive Output: {recursive_inner_plus_then_increment(list_input)}")

