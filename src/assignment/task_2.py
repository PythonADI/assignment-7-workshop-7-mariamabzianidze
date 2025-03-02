"""
Write a function called outer_function that defines a local variable message = "Hello". Inside it, define another function called inner_function that tries to access and modify message. Call inner_function within outer_function and see if the changes persist.

- What happens if you use the nonlocal keyword with message inside inner_function?
- Can inner_function modify message without nonlocal?
"""

def outer_function():
    message = "Hello"

    def inner_function():
        message = "Hi" 
        print("Inner message:", message) 

    inner_function()
    print("Outer message:", message)  
    
outer_function()


def outer_function():
    message = "Hello"

    def inner_function():
        nonlocal message  
        message = "Hi"
        print("Inner message:", message)  

    inner_function()
    print("Outer message:", message)  

outer_function()

'''nonlocal საკვანძო სიტყვას inner_function-ში საშუალებას აძლევს ფუნქციას შეცვალოს შეტყობინების ცვლადი outer_function-დან'''
'''inner_function არ შეუძლია შეცვალოს შეტყობინება outer_function-დან nonlocal-ის გარეშე, ის შექმნის ახალ ლოკალურ ცვლადს inner_function-ში და უცვლელად დატოვებს გარე შეტყობინებას'''