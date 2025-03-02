"""
Define a variable name = "Alice" at the global level. Create a function change_name that has a local variable also called name with the value "Bob". Print name both inside and outside the function after calling change_name.

- Observe how Python handles variables with the same name in different scopes.
- Try adding global name inside change_name and see what happens to the global name.
"""


name = "Alice"  

def change_name():
    name = "Bob"
    print("Inside function:", name)

change_name()
print("Outside function:", name)


def change_name():
    global name 
    name = "Bob"
    print("Inside function:", name)

change_name()
print("Outside function:", name) 

'''პითონი მიჰყვება წესს (ლოკალური, თანდართული, გლობალური, ჩაშენებული), რათა განსაზღვროს რომელი ცვლადი გამოიყენოს, როდესაც არსებობს ერთიდაიმავე სახელწოდების ცვლადები'''
name = "Alice"
def change_name():
    global name 
    name = "Bob"
    print("Inside function:", name)

change_name()
print("Outside function:", name)