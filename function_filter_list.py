#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Function used to answer the question and print the filtered list
def filter_list(input_list, filter_num):
    return [x for x in input_list if x <= filter_num]

#Function used to parse the input of the list and create a list that can then be passed to the filter_list function
#this function ensures that integers were entered
def parse_list_input(input_str):
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

#I was unsure if the question intended for the user to input both the list and the filter. This try statement handles errors associated with inputting a list
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
        filter_num = float(input("Enter the filter value: "))
        if not filter_num.is_integer():
            raise ValueError("Filter number must be an integer")
        filter_num = int(filter_num)
        result = filter_list(input_list, filter_num)
        print(f"Filtered list (elements <= {filter_num}): {result}")
        break
    except ValueError as e:
        if str(e) == "Threshold must be an integer":
            print(f"Error: {e}")
        else:
            print("Error: Please enter a valid number")

