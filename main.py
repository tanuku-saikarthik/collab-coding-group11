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

def function4(text):
    # Contributor 4 will implement
    """
    Author: Contributor 4
    Returns the frequency of each character in the given string.
    Example: function4("issssn") -> {'i': 1, 's': 4, 'n': 1}
    """
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq


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

     # Function 4: Frequency of characters
    freq_dict = function4(sample)
    print("Function4 (Character Frequency):", freq_dict)
