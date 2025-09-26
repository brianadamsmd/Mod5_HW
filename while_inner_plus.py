#!/usr/bin/env python
# coding: utf-8

# In[19]:


def find_innermost_list_plus_one_using_while(input_nested_list):
    ## current = used as a list to iterate through while loop and is initially set to the nested lists that are passed as an argument
    current = input_nested_list

    ## first test to make sure there is a nested list that was passed into the function
    if not any(isinstance(item, list) for item in current):
        raise ValueError("Input list must contain at least one nested list")
    
    else:
        
        ## first while loop evaluates if there are any lists in the current list that is being iterated through
        while any(isinstance(item, list) for item in current):
            
            ## iter_num = variable to be used to count the number of iterations and used to index a list
            iter_num = 0

            ## inner while loop is entered if there is a list found in the current list
            while iter_num < len(current):
                if isinstance(current[iter_num], list):
                    current = current[iter_num]
                    break
                iter_num += 1
            
    return [x + 1 for x in current]

find_innermost_list_plus_one_using_while([1,2,3,4,5,6,7,8,9,[12,14,17]])


# In[ ]:




