import threading
import queue
import random
import time

BUFFER_SIZE = 5
MAX_ITEMS = 10  # Maximum number of items to produce and consume
buffer = queue.Queue(maxsize=BUFFER_SIZE)

mutex = threading.Lock()
empty = threading.Semaphore(BUFFER_SIZE)  # Initially, buffer has BUFFER_SIZE empty slots
full = threading.Semaphore(0)             # Initially, buffer has 0 full slots

# Separate counts for producer and consumer
producer_count = 0
consumer_count = 0

# Locks to protect separate counts
producer_count_lock = threading.Lock()
consumer_count_lock = threading.Lock()

def display_buffer():
    """Displays the current state of the buffer."""
    print(f"Buffer state: {list(buffer.queue)}")

def producer():
    global producer_count
    while producer_count < MAX_ITEMS:
        item = random.randint(1, 100)  # Produce an item
        empty.acquire()  # Wait if the buffer is full
        
        # Acquire the mutex to access the buffer using `with`
        with mutex:
            buffer.put(item)
            print(f"Produced {item}")
            display_buffer()

        full.release()   # Signal that the buffer has one more full slot

        # Update producer count after producing using `with`
        with producer_count_lock:
            producer_count += 1

        time.sleep(random.uniform(0.1, 1))  # Sleep for a random interval

def consumer():
    global consumer_count
    while consumer_count < MAX_ITEMS:
        full.acquire()  # Wait if the buffer is empty

        # Acquire the mutex to access the buffer using `with`
        with mutex:
            item = buffer.get()
            print(f"Consumed {item}")
            display_buffer()

        empty.release()  # Signal that the buffer has one more empty slot

        # Update consumer count after consuming using `with`
        with consumer_count_lock:
            consumer_count += 1

        time.sleep(random.uniform(0.1, 1))  # Sleep for a random interval

# Creating and starting producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# Wait for threads to finish
producer_thread.join()
consumer_thread.join()

print(f"Total items produced: {producer_count}")
print(f"Total items consumed: {consumer_count}")
