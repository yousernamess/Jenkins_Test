
"""
Simple Python script for Jenkins testing
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    """Main function"""
    print("Simple Calculator")
    print("-" * 30)
    
    result1 = add(10, 5)
    print(f"10 + 5 = {result1}")
    
    result2 = subtract(10, 5)
    print(f"10 - 5 = {result2}")
    
    result3 = multiply(10, 5)
    print(f"10 * 5 = {result3}")
    
    result4 = divide(10, 5)
    print(f"10 / 5 = {result4}")
    
    print("-" * 30)
    print("All tests passed!")

if __name__ == "__main__":
    main()
