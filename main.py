"""
String Manipulation Project
Collaborative coding assignment using GitHub workflow
"""

# Contributor 1 - Function 1: Factorial of a number
def function1(n: int) -> int:
    """
    Returns the factorial of a non-negative integer n.
    Example: factorial(5) = 120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def function2():
    # Contributor 2 will implement
    pass

def function3():
    # Contributor 3 will implement
    pass

def function4():
    # Contributor 4 will implement
    pass


# Driver (Admin will finalize later)
if __name__ == "__main__":
    print("String Manipulation Project Running...")
    print("Function1 (Factorial of 5):", function1(5))
