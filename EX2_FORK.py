import os
import time

def child_process():
    print(f"Child Process ID : {os.getpid()}")
    print(f"Parent Process ID : {os.getppid()}")
    time.sleep(2)
    print("Child Process Terminating")
    os._exit(0)

def main():
    print(f"Parent Process ID : {os.getpid()}")
    print("Forking Child ... ")
    pid = os.fork()

    if pid == 0:
        child_process()
    
    elif pid > 0:
        print("Parent Process waiting for child process to complete")
        _, status = os.wait()
        print("Terminating Parent Process")

main()