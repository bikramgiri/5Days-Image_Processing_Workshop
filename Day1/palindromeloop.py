# palindrome loop program

def is_palindrome(string):
    string = string.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    length = len(string)
    
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True

# Take user input in a loop
while True:
    user_input = input("Enter a word or phrase (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    if is_palindrome(user_input):
        print("It's a palindrome!")
    else:
        print("Not a palindrome.")



# Output:
# Enter a word or phrase (or type '
# exit' to quit): hello
# Not a palindrome.
# Enter a word or phrase (or type '
# exit' to quit): racecar
# It's a palindrome!