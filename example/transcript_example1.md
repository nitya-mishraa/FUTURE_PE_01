```python
# Student Input:
def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)

print(calculate_average([]))
```

### AI Response:

Hi! Let’s work through this bug together. Can you explain what this function is supposed to do?

I notice that when the input list is empty, there’s a potential runtime error. Can you think about what happens when len(numbers) is zero?

Hint: Try printing intermediate values and check how the code behaves for an empty list. What does dividing by zero do?

You could also test with small non-empty lists first to see if the logic works as expected.

Did that hint help? Want me to guide you through the next step without giving the solution?
