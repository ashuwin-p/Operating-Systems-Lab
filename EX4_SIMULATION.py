import os

def simulate_cat(filepath):
    if os.path.exists(filepath):
        file = open(filepath, 'r')
        print(file.read())


def simulate_ls(directory = '.'):
    for entry in os.listdir(directory):
        print(entry)
    
def simulate_grep(filepath, pattern):
    if os.path.exists(filepath):
        file = open(filepath, 'r')
        content = file.read().split('\n')
        for line in content:
            if pattern in line:
                print(line)

simulate_ls('/home/ubuntu/Documents')
simulate_cat('/home/ubuntu/OS_Lab/EX4_SIMULATION.py')
simulate_grep('/home/ubuntu/OS_Lab/EX4_SIMULATION.py', 'for')