## Queue
A queue is structured as an ordered collection of items which are 
added at one end, called the **rear**, and removed from the other 
end, called the **front**. 
Queues maintain a **FIFO** ordering property. 
Queue operations:
- **Queue()** creates a new queue that is empty. It needs no parameters and returns an empty queue.
- **enqueue(item)** adds a new item to the rear of the queue. It needs the item and returns nothing.
- **dequeue()** removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
- **is_empty()** tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
- **size()** returns the number of items in the queue. It needs no parameters and returns an integer.

## Deque (Double-ended queue)
 Ordered collection of items where items are added and removed from either end (front or rear).
 Deque operations:
- **Deque()** creates a new deque that is empty. It needs no parameters and returns an empty deque.
- **add_front(item)** adds a new item to the front of the deque. It needs the item and returns nothing.
- **add_rear(item)** adds a new item to the rear of the deque. It needs the item and returns nothing.
- **remove_front()** removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
- **remove_rear()** removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
- **is_empty()** tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
- **size()** returns the number of items in the deque. It needs no parameters and returns an integer.