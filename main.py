"""
String manipulation Project
Collaborative coding assignment using GitHub workflow
"""

# Placeholder functions (contributors will implement them)

def function1(text):
    """
    Author: Jagadeesh T
    Returns the reverse of the given string.
    Example: function1("hello") -> "olleh"
    """
    return text[::-1]

def function2(word):
    """
    Author: Dhanraj
    Checks if the given string is a palindrome.
    Returns True if palindrome, False otherwise.
    Example: function2("madam") -> True
    """
    word = word.lower().replace(" ", "")
    return word == word[::-1]


def function3(text):
    """
    Author: Om
    Counts the number of vowels (a, e, i, o, u) in the given string.
    Example: function3("hello") -> 2
    """
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

def function4():
    # Contributor 4 will implement
    pass


# Driver (Admin will finalize later)
if __name__ == "__main__":
   print("String Manipulation Project Running...\n")
    
    sample = input("Enter a string: ")
    
    # Function 1: Reverse string
    reversed_text = function1(sample)
    print("Function1 (Reverse):", reversed_text)
    
    # Function 2: Check palindrome
    is_palindrome = function2(sample)
    print("Function2 (Palindrome Check):", is_palindrome)
    
    # Function 3: Count vowels
    vowel_count = function3(sample)
    print("Function3 (Vowel Count):", vowel_count)
    # Admin will call all contributed functions here
