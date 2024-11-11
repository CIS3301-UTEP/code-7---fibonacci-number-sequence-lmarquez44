def get_fibonacci_number(position):
    """Recursively calculates the Fibonacci number at the specified position."""
    if position <= 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fibonacci_number(position - 1) + get_fibonacci_number(position - 2)

def get_fibonacci_number_sequence(number):
    """Generates a list of Fibonacci sequence numbers for the specified number of elements."""
    sequence = []
    for i in range(1, number + 1):
        sequence.append(get_fibonacci_number(i))
    return sequence
if __name__ == "__main__":
    # Test the Fibonacci number function for a specific position
    position = 7
    print(f"Fibonacci number at position {position}:", get_fibonacci_number(position))

    # Test the Fibonacci sequence function for a given number of elements
    sequence_length = 7
    print(f"Fibonacci sequence of {sequence_length} elements:", get_fibonacci_number_sequence(sequence_length))
