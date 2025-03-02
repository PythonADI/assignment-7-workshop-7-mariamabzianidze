"""
Create a function called `increase_counter` that increases a `counter` variable by 1 each time it's called. Try initializing `counter` = 0 outside the function (global scope), and then call `increase_counter` multiple times.

- What happens when you try to update counter inside the function without using global?
- Now, try declaring counter as global inside the function and observe the results.
"""
counter = 0

def increase_counter():
    global counter
    counter += 1
    print("Counter:", counter)

increase_counter()
increase_counter()
increase_counter() 
increase_counter()



'''counter = 0  
def increase_counter():
    counter += 1  # trying to update the counter without  global
    print("Counter:", counter)

increase_counter() '''



def increase_counter():
    global counter
    counter += 1 
    print("Counter:", counter)

increase_counter()  
increase_counter()
increase_counter() 

