import multiprocessing.shared_memory as shared_memory

# Access existing shared memory segment
shm_client = shared_memory.SharedMemory(name="sm2")
buffer = shm_client.buf  # Buffer to read/write from shared memory

try:
    while True:
        # Read and display data from shared memory
        client_data = bytes(buffer[:100]).decode('utf-8')
        print("Server says:", client_data)

        # Acknowledge the message received from the server
        print("Client received message:", client_data)

        # Check if the server signaled to exit
        if client_data.strip() == 'exit':
            print("Exit signal received from server. Terminating client.")
            break

        # Prompt user for input and update shared memory
        user_input = input("Enter message (or 'exit' to quit): ")
        
        # Clear previous content
        buffer[:100] = b'\x00' * 100
        message_bytes = user_input.encode('utf-8')
        buffer[:len(message_bytes)] = message_bytes  # Store new message in shared memory
        print("Client sent message:", user_input)

        # If user wants to exit, set 'exit' flag in shared memory
        if user_input == 'exit':
            buffer[:4] = b'exit'
            print("Client sent exit signal to server.")
            break

finally:
    # Clean up shared memory
    shm_client.close()
    try:
        shm_client.unlink()  # Only unlink if it exists
        print("Client shared memory cleaned up and closed.")
    except FileNotFoundError:
        print("Shared memory already unlinked or not found.")
