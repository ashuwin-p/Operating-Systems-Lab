import os
import time
import random

BUFFER_SIZE = 5      # Number of items that the producer can produce
MAX_ITEMS = 10       # Max items to be produced and consumed

# Function for the producer process
def producer(write_pipe):
    for i in range(MAX_ITEMS):
        item = random.randint(1, 100)
        print(f"Producer: Producing item {item}")
        
        os.write(write_pipe, str(item).encode() + b'\n')
        time.sleep(random.uniform(0.1, 0.5))

    print("Producer: Finished producing items.")
    os.close(write_pipe)

# Function for the consumer process
def consumer(read_pipe):
    while True:
        item = os.read(read_pipe, 1024).decode().strip()

        if not item:
            break
        
        item = item.split("\n")
        for it in item:
            print(f"Consumer: Consuming item {it}")
            time.sleep(random.uniform(0.2, 0.7))

    print("Consumer: Finished consuming items.")
    os.close(read_pipe)

# Main function to create the pipe and fork processes
def main():
    r, w = os.pipe()

    pid = os.fork()

    if pid > 0:
        # Parent process (Producer)
        os.close(r)  
        producer(w)
        os.wait()

    elif pid == 0:
        # Child process (Consumer)
        os.close(w)
        consumer(r)

if __name__ == "__main__":
    main()
