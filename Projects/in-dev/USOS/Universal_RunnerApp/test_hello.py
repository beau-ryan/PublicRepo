#!/usr/bin/env python3
"""
Simple test script for Universal Runner CLI testing
"""

def main():
    print("Hello from Universal Runner!")
    print("This is a test script running successfully.")
    
    # Test some basic Python functionality
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print(f"Numbers: {numbers}")
    print(f"Squares: {squares}")
    
    # Test string operations
    message = "Universal Runner is working!"
    print(f"Message length: {len(message)}")
    print("Test completed successfully!")

if __name__ == "__main__":
    main()