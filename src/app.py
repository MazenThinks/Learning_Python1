n = input("gonna double ur numba just type it : ")

def my_function():
    global n
    return lambda a : a * n

function_doubler = my_function()

print(function_doubler(2))