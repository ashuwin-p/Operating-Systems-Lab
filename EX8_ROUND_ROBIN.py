"""
    AUTHOR : ASHUWIN P
    REG. NO : 3122 22 5002 013
    COURSE : UIT2512 OPERATING SYSTEMS PRACTICES LAB

    TOPIC : ROUND ROBIN CPU SCHEDULING ALOGORITHM
"""

class Process:
    def __init__(self, pid, BT, AT=0):
        self.pid = pid 
        self.BT = BT 
        self.AT = AT 
        self.WT = 0 
        self.TT = 0 
        self.remaining_BT = BT
        self.completion_time = 0
        self.isCompleted = False

    def __lt__(self, other):
        return self.AT < other.AT


class Scheduler:
    def __init__(self, processes, time_quantum):
        self.processes = processes
        self.time_quantum = time_quantum

    def round_robin(self):
        self.processes.sort()  # Sort by Arrival Time
        ready_queue = []
        time = 0
        completed = 0
        n = len(self.processes)

        while completed < n:
            # Add processes that have arrived by the current time
            for p in self.processes:
                if p.AT <= time and not p.isCompleted and p not in ready_queue:
                    ready_queue.append(p)

            # If the ready queue is not empty, schedule the next process
            if ready_queue:
                process = ready_queue.pop(0)  # Get the first process in the queue

                # Execute the process for the time quantum or remaining burst time
                if process.remaining_BT <= self.time_quantum:
                    time += process.remaining_BT
                    process.completion_time = time
                    process.TT = process.completion_time - process.AT
                    process.WT = process.TT - process.BT
                    process.isCompleted = True
                    process.remaining_BT = 0
                    completed += 1
                else:
                    time += self.time_quantum
                    process.remaining_BT -= self.time_quantum
                    ready_queue.append(process)  # Reinsert process back into queue

                print(
                    f"Time {time}: Executing ... Process {process.pid} remaining burst time {process.remaining_BT}"
                )
            else:
                time += 1  # If no process is ready, increment time

    def display(self):
        print("\nPID\tAT\tBT\tWT\tTT")
        for p in self.processes:
            print(f"{p.pid}\t{p.AT}\t{p.BT}\t{p.WT}\t{p.TT}")

    def calculate_averages(self):
        total_WT = sum(p.WT for p in self.processes)
        total_TT = sum(p.TT for p in self.processes)
        n = len(self.processes)
        avg_WT = total_WT / n
        avg_TT = total_TT / n
        print(f"\nAverage Waiting Time: {avg_WT:.2f}")
        print(f"Average Turnaround Time: {avg_TT:.2f}")


# Sample test to demonstrate Round Robin Scheduling
process_list = [
    Process("P1", 5, 0),
    Process("P2", 3, 1),
    Process("P3", 8, 2),
    Process("P4", 6, 3),
]


time_quantum = 2  # Time Quantum for Round Robin Scheduling

scheduler = Scheduler(process_list, time_quantum)
scheduler.round_robin()
scheduler.display()
scheduler.calculate_averages()
