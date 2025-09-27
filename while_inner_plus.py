
def find_innermost_list_plus_one_using_while(input_nested_list):
    
    # -----------------------------------------------
    # 1. VALIDATION PHASE (Check for only int or list)
    # -----------------------------------------------
    validation_stack = [input_nested_list]
    is_valid = True
    
    while len(validation_stack) > 0:

        #outer while loop will continue to iterate until there are no integers or lists in the validation stack
        current_list = validation_stack.pop()
        index = 0
        
        while index < len(current_list):
            item = current_list[index]
            
            if isinstance(item, int):
                pass
            elif isinstance(item, list):
                #This step adds any lists onto the end of the validation stack until there are no more lists to add
                validation_stack.append(item)
            else:
                is_valid = False
                break
            
            index += 1
        
        if not is_valid:
            break

    if not is_valid:
        return "Error: Input list or its nested lists contain elements that are not integers or lists."

    # -------------------------------------------------------------
    # 2. FIND AND INCREMENT ALL INNERMOST LISTS PHASE (ANSWER TO QUESTION - NOT VALIDATING INPUT ANYMORE)
    # -------------------------------------------------------------
    
    solution_stack = [input_nested_list]
    
    # Outer WHILE loop: It continues as long as there are lists on the stack that need to be processed.
    while len(solution_stack) > 0:
        
        current_list = solution_stack.pop()
        has_nested_list = False
        
        # Inner WHILE loop: Manually iterates through all elements of the current_list.
        item_index = 0
        while item_index < len(current_list):
            item = current_list[item_index]
            
            if isinstance(item, list):
                # Found a nested list! This means the current_list is NOT an innermost list.
                has_nested_list = True
                
                # PUSH the nested list back onto the stack to be processed later.
                solution_stack.append(item)
            
            item_index += 1
        
        # After the inner loop finishes, this evaluates has_nested_list to determine if additional iteration is needed.
        # If has_nested_list is False, this list contains ONLY integers and is therefore the INNERMOST NESTED LIST.
        if not has_nested_list:
            
            # current_list is now the innermost list and needs modification.
            # Initialize an index for modifying the elements of the innermost list
            mod_index = 0
            
            # Third WHILE loop: Iterates through the elements of the identified innermost list.
            while mod_index < len(current_list):
                
                if isinstance(current_list[mod_index], int):
                    # modify the list IN PLACE.
                    current_list[mod_index] += 1
                
                mod_index += 1            

    
    return input_nested_list

list_input = [1, 2, 3, 4, [5, 6, 7, [8, 9,1,3,4,65,6,43,3,4,5,56,3,4,5,56,45,4,3],45,4,3],[8, 9,1,3,4,65,6,43,3,4,5,56,[8, 9,1,3,4,65,6,43,[3,4,5,56,45,4,3],3,4,5,56,45,4,3],45,4,[8, 9,1,3,4,65,6,43,[3,4,5,56,[1,2,3,4],45,4,3],3]]]
print(f"Input: {list_input}")

print(f"Output:{find_innermost_list_plus_one_using_while(list_input)}")



