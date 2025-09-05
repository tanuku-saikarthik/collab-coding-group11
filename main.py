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
    word = word.lower().replace(" ", "")  # normalize by removing spaces & ignoring case
    return word == word[::-1]


def function3():
    # Contributor 3 will implement
    pass

def function4():
    # Contributor 4 will implement
    pass


# Driver (Admin will finalize later)
if __name__ == "__main__":
    print("String manipulation Project Running...")
    sample = input("String to reverse: ")
    print("Function1 (Reverse):", function1(sample))
    # Admin will call all contributed functions here
