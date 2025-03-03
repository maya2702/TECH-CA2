import streamlit as st 

def generatePassword(pwlength):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = [] 

    for i in pwlength:
        password = "" 
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]
        
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        
        passwords.append(password) 
    
    return passwords


def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
    return pword


def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
    return pword


# NEW: Added a function to handle valid input
def get_valid_input(prompt, min_value=3):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input >= min_value:
                return user_input
            else:
                print(f"Password length should be at least {min_value}. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def main():
    print("Welcome to the Password Generator!")
    print("This program will help you generate secure passwords based on your preferences.")
    
    # NEW: Ask how many passwords the user wants to generate
    numPasswords = get_valid_input("How many passwords do you want to generate? (Enter a number): ", min_value=1)
    
    print(f"\nGenerating {numPasswords} passwords...")

    passwordLengths = []

    # NEW: Ask the user to specify the length for each password
    for i in range(numPasswords):
        length = get_valid_input(f"Enter the length for Password #{i + 1} (minimum 3 characters): ", min_value=3)
        passwordLengths.append(length)
    
    # NEW: Ask if the user wants special characters or numbers included
    include_special_chars = input("Would you like to include special characters (e.g., !, @, #)? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Would you like to include numbers (0-9)? (y/n): ").strip().lower() == 'y'

    Password = generatePassword(passwordLengths)

    print("\nGenerated Passwords:")
    
    for i in range(numPasswords):
        password = Password[i]
        
        # NEW: Add optional complexity based on user input
        if include_numbers:
            password = replaceWithNumber(password)
        if include_special_chars:
            special_chars = "!@#$%^&*()"
            special_char = random.choice(special_chars)
            password = password + special_char

        print(f"Password #{i + 1}: {password}")
        
    print("\nThank you for using the Password Generator!")

# NEW: Run the main function
main()
