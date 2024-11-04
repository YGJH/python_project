import copy

def call_by_value(func):
    def wrapper(*args, **kwargs):
        return func(*[copy.deepcopy(arg) for arg in args],  #1
                    **{k: copy.deepcopy(v) for k, v in kwargs.items()})  #2, #3
    return wrapper

# Usage example
@call_by_value
def modify_list(my_list):
    my_list.append(4)
    print("Inside function:", my_list) 

original_list = [1, 2, 3]
modify_list(original_list)
print("Outside function:", original_list)
