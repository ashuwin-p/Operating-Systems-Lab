import os

# Command paths - ensure correct paths or use commands available in the system's environment
command_path = ['/bin/ls', '/bin/ps', '/usr/bin/clear']

while True:
    print("""
    1. List all Files
    2. List Processes  
    3. Clear Screen
    4. Exit
    """)

    option = int(input("Enter Option: "))

    if option == 1:
        # Executes 'ls -l' to list files
        os.execl(command_path[option-1], 'ls', '-l')

    elif option == 2:
        # Executes 'ps aux' to list processes
        os.execl(command_path[option-1], 'ps', 'aux')

    elif option == 3:
        # Executes 'clear' to clear the screen
        os.execl(command_path[option-1], 'clear')

    elif option == 4:
        print("Exiting program.")
        break  # Exit the loop and terminate the program

    else:
        print("Invalid option. Please choose a valid option.")
