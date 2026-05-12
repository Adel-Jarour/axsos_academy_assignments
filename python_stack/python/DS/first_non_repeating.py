#  First Non-Repeating Character in a Stream. As characters arrive return the first non-repeating one, using a queue or stack.

from queue import Queue

def first_non_repeating(stream):

    # Store frequency of each character
    count = {}

    # Create queue
    queue = Queue()

    # Store answers
    result = []

    # Process characters one by one
    for char in stream:

        # Update frequency
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

        # Add character to queue
        queue.enqueue(char)

        # Remove repeated characters from front
        while (not queue.is_empty() and
            count[queue.peek()] > 1):

            queue.dequeue()

        # Store current first non-repeating character
        if not queue.is_empty():
            result.append(queue.peek())
        else:
            result.append(None)

    return result


# Example usage
stream = ['a', 'b', 'a', 'c', 'b', 'd']

print(first_non_repeating(stream))