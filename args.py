# ><><><><><><><><><><>< *args ><><><><><><><><><><><

# Example: 
 
# def my_fn(*args):
#     for arg in args:
#         print(arg)
# my_fn("Hello","World",420)

# ><><><><><><><><><><>< **kwargs ><><><><><><><><><><><

# Example:

# def my_fn(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# my_fn(name="momi", age="20", gender="unknown")

# ><><><><><><><><><><>< *args and **kwargs together ><><><><><><><><><><><

# Example:

# def my_fn(*args,**kwargs):
#     print("args: ")
#     for arg in args:
#         print(arg)
#     print("kwargs: ")
#     for key, value in kwargs.items():
#         print(key, ":", value)

# my_fn("IceCream","Donuts","Coffee",Food="Pasta",Drink="Mojito",Dessert="Pudding")


