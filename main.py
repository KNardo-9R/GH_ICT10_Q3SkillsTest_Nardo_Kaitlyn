# account creation
from pyscript import display, document 

def signup(e): 
    document.getElementById('signresult').innerHTML = ' '

    # CONVERTING THE INPUTS 
    username = document.getElementById('user').value.lower() 
    password = document.getElementById('pass').value 

    # CHECKING THE INPUTS 
    # for username 
    username_characters = len(username) # checking # of characters in the username input

    # for password 
    password_characters = len(password) # checking # of characters in the password input 
    password_letters = any(passw.isalpha() for passw in password) # checking if input contains at least one letter 
    password_numbers = any(passw.isdigit() for passw in password) # checking if input contains at least one number 
    
    # For keyword = container for the iterable objects in the list =
    # In keyword to direct where to get the contents of the passw container, which is the password variable 


    # CHECKING IF INPUTS ARE APPLICABLE 
    # for username 
    if username_characters < 7: 
        display(f'❌Username needs at least 7 characters', target='signresult')
    else: 
        display(f'✅Username has 7 characters or more', target='signresult')

    # for password 
    if password_letters: 
        display (f'✅Password contains at least one letter', target='signresult')
    else: 
        display(f'❌Password needs to contain at least one letter', target='signresult')

    if password_numbers: 
        display (f'✅Password contains at least one number', target='signresult')
    else: 
        display(f'❌Password needs to contain at least one number', target='signresult')

    if password_characters < 10: 
        display(f'❌Password needs at least 10 characters',target='signresult')
    else: 
        display(f'✅Password has 10 or more characters', target='signresult')

    
        
