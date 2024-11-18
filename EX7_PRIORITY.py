"""
    AUTHOR : ASHUWIN P
    REG. NO : 3122 22 5002 013
    COURSE : UIT2512 OPERATING SYSTEMS PRACTICES LAB

    TOPIC : PRIORITY CPU SCHEDULING ALOGORITHM
"""

class Process:
    def __init__(self, pid, BT, priority, AT=0):
        self.pid = pid
        self.BT = BT
        self.priority = priority  # Priority for Priority Scheduling
        self.AT = AT
        self.WT = 0
        self.TT = 0
        self.start_time = 0
        self.completion_time = 0
        self.remaining_BT = BT
        self.isCompleted = False

    def __lt__(self, other):
        return self.AT < other.AT  # Sort based on Arrival Time

    def __str__(self):
        return f"{self.pid} \t {self.AT} \t {self.BT} \t {self.WT} \t {self.TT} \t {self.priority}"


class Scheduler:
    def __init__(self, processes):
        self.processes = processes

    def display(self):
        print("\nPID\tAT\tBT\tWT\tTT\tPriority")
        for p in self.processes:
            print(p)

    def calculate_averages(self):
        total_WT = sum(p.WT for p in self.processes)
        total_TT = sum(p.TT for p in self.processes)
        n = len(self.processes)
        avg_WT = total_WT / n
        avg_TT = total_TT / n
        print(f"\nAverage Waiting Time: {avg_WT:.2f}")
        print(f"Average Turnaround Time: {avg_TT:.2f}")

    def priority_non_preemptive(self):
        self.processes.sort()  # Sort the processes based on Arrival Time
        clock = 0
        completed = 0
        total_processes = len(self.processes)
        execution_order = []  # Track the order of execution

        while completed < total_processes:
            ready_queue = [
                p for p in self.processes if p.AT <= clock and not p.isCompleted
            ]  # Ready queue
            if ready_queue:
                # Select process with the highest priority (lowest priority number)
                process = min(ready_queue, key=lambda x: x.priority)

                process.start_time = clock
                process.WT = clock - process.AT
                process.TT = process.WT + process.BT
                clock += process.BT
                process.completion_time = clock
                process.isCompleted = True  # Mark process as completed

                completed += 1
                execution_order.append(process)
            else:
                clock += 1  # If no process is ready, increment clock

        return execution_order

    def priority_preemptive(self):
        self.processes.sort()  # Sort processes based on Arrival Time
        clock = 0
        completed = 0
        total_processes = len(self.processes)
        execution_order = []  # Track the order of execution
        last_process = None  # To track the last process that was executed

        while completed < total_processes:
            ready_queue = [
                p for p in self.processes if p.AT <= clock and not p.isCompleted
            ]  # Ready queue
            if ready_queue:
                # Select process with the highest priority (lowest priority number)
                process = min(ready_queue, key=lambda x: x.priority)
                print(f"Clock : {clock} Process : {process.pid}")

                # Only add to execution order if there's a switch of process
                if process != last_process:
                    execution_order.append(process)
                    last_process = process

                process.remaining_BT -= 1
                clock += 1

                # If the process is finished
                if process.remaining_BT == 0:
                    process.completion_time = clock
                    process.WT = process.completion_time - process.AT - process.BT
                    process.TT = process.WT + process.BT
                    process.isCompleted = True  # Mark process as completed
                    completed += 1
            else:
                clock += 1  # If no process is ready, increment the clock

        return execution_order

    def display_gantt_chart(self, execution_order):
        print("\nGantt Chart:")
        for process in execution_order:
            print(f"| {process.pid:<5}", end="")
        print("|")
        current_time = 0
        print(f"{current_time:<5}", end="")
        for process in execution_order:
            current_time = process.completion_time
            print(f"{current_time:<5}", end="")
        print("\n")


# Sample test to demonstrate Priority scheduling
process_list = [
    Process("P1", 3, 0, 3),  # Process P1 with priority 0
    Process("P2", 4, 1, 2),  # Process P2 with priority 2
    Process("P3", 6, 2, 4),  # Process P3 with priority 1
    Process("P4", 4, 3, 6),  # Process P4 with priority 3
    Process("P5", 2, 5, 10),  # Process P5 with priority 0
]

scheduler1 = Scheduler(process_list)

# Priority Non-Preemptive
print("Priority Non-Preemptive:")
execution_order_non_preemptive = scheduler1.priority_non_preemptive()
scheduler1.display()
scheduler1.display_gantt_chart(execution_order_non_preemptive)
scheduler1.calculate_averages()


process_list = [
    Process("P1", 3, 0, 3),  # Process P1 with priority 0
    Process("P2", 4, 1, 2),  # Process P2 with priority 2
    Process("P3", 6, 2, 4),  # Process P3 with priority 1
    Process("P4", 4, 3, 6),  # Process P4 with priority 3
    Process("P5", 2, 5, 10),  # Process P5 with priority 0
]

scheduler2 = Scheduler(process_list)

# Priority Preemptive
print("Priority Preemptive:")
execution_order_preemptive = scheduler2.priority_preemptive()
scheduler2.display()
scheduler2.display_gantt_chart(execution_order_preemptive)
scheduler2.calculate_averages()
