# Function to calculate the average of a list
def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)  # Potential bug if list is empty

# Test the function
print(calculate_average([]))  # Empty list
