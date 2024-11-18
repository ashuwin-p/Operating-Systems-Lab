import time
from multiprocessing.shared_memory import SharedMemory
import sys

# Create shared memory segment
shm_server = SharedMemory(create=True, size=100, name='sm2')
buffer = shm_server.buf  # Buffer to read/write from shared memory

try:
    while True:
        # Read and display data from shared memory
        server_data = bytes(buffer[:100]).decode('utf-8')
        print("Server data in memory:", server_data)

        # Check if 'exit' signal is received
        if buffer[:4] == b'exit':
            print("Exit signal received. Terminating server.")
            break

        # Acknowledge message from client
        print("Server received message:", server_data)

        # Update shared memory with a message
        message1 = 'USING SHARED MEMORY'
        buffer[:100] = b'\x00' * 100  # Clear previous content
        message_bytes1 = message1.encode('utf-8')
        buffer[:len(message_bytes1)] = message_bytes1  # Store new message
        print("Server sent message:", message1)

        time.sleep(5)  # Sleep for 5 seconds before updating again

finally:
    # Clean up shared memory
    shm_server.close()
    sys.exit(0)