#2. For each temperature find how many days until a warmer temperature.
# ex: [22, 18, 28, 32, 25, 20, 23]
# out: [2, 1, 1, 0, 0, 1, 0]

from stack import Stack 

def warmer_days(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = Stack()

    for current_day in range(n):

        while (not stack.is_empty() and temperatures[current_day] > temperatures[stack.peek()]):

            previous_day = stack.pop()

            result[previous_day] = current_day - previous_day

        stack.push(current_day)

    return result


# Example usage
temps = [22, 18, 28, 32, 25, 20, 23]

print(warmer_days(temps))