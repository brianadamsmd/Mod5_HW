#!/usr/bin/env python
# coding: utf-8

# In[16]:


## Due to recursive calling, a global variable needs to be used to check initially if there is a nested list
first_pass = True

def find_inner_most_plus_one_using_recursion(input_list):

    global first_pass


    ## nested function used to check for the presence of a nested list
    def has_nested_list(lst):
        return any(isinstance(item, list) for item in lst)

    ## logic for initial check of the nested list (Error handling)
    if first_pass:
        first_pass = False

        if not has_nested_list(input_list):
            raise ValueError("Input list must contain at least one nested list")

    #if there is a nested list or it is not the first pass through the recursion, the rest of this code will run
    
    # if no nested lists, return the list with each element +1
    if not any(isinstance(item, list) for item in input_list):
        return [x + 1 for x in input_list]
    
    # Recursive case: find the first nested list and recurse
    for item in input_list:
        if isinstance(item, list):
            return find_inner_most_plus_one_using_recursion(item)

find_inner_most_plus_one_using_recursion([1,2,3,4,5,6,7,8,9,[ 34, 56, 79]])

