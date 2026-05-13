# Design Circular Queue

## Overview
This project involves designing and implementing a **Circular Queue** (also known as a **Ring Buffer**). Unlike a standard queue, a circular queue connects the end back to the beginning, allowing for efficient use of fixed-size memory.

## Features to Implement
A circular queue should support the following operations:

- **MyCircularQueue(k)**: Initializes the object with the size of the queue to be `k`.
- **Front()**: Gets the front item from the queue. If the queue is empty, return -1.
- **Rear()**: Gets the last item from the queue. If the queue is empty, return -1.
- **enQueue(value)**: Inserts an element into the circular queue. Return `True` if the operation is successful.
- **deQueue()**: Deletes an element from the circular queue. Return `True` if the operation is successful.
- **isEmpty()**: Checks whether the circular queue is empty or not.
- **isFull()**: Checks whether the circular queue is full or not.

## Benefits of a Circular Queue
1. **Memory Efficiency**: Reuses empty spaces created by dequeue operations without needing to shift elements.
2. **Fixed Size**: Ideal for buffering data streams where the maximum capacity is known beforehand.

## Implementation Guide
To implement this efficiently:
- Use an array/list of size `k`.
- Maintain `head` and `tail` pointers.
- Use the modulo operator `%` to wrap pointers around the array.
