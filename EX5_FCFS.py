"""
    AUTHOR : ASHUWIN P
    REG. NO : 3122 22 5002 013
    COURSE : UIT2512 OPERATING SYSTEMS PRACTICES LAB

    TOPIC : FCFS CPU SCHEDULING ALOGORITHM
"""


class process:
    def __init__(self, pid, BT, AT=0):
        self.pid = pid
        self.BT = BT
        self.AT = AT
        self.WT = 0
        self.TT = 0
        self.start_time = 0
        self.completion_time = 0

    def __lt__(self, other):
        return self.AT < other.AT

    def __str__(self):
        details = f"{self.pid} \t {self.AT} \t {self.BT} \t {self.WT} \t {self.TT}"
        return details


class Scheduler:
    def __init__(self, processes):
        self.processes = processes

    def FCFS(self):
        self.processes.sort()  # Sort the processes based on Arrival Time
        clock = 0
        for process in self.processes:
            if clock < process.AT:
                clock = process.AT  # Ensure the CPU waits if the process hasn't arrived yet
            process.start_time = clock
            process.WT = clock - process.AT
            process.TT = process.WT + process.BT
            clock += process.BT
            process.completion_time = clock

    def display(self):
        print("PID \t AT \t BT \t WT \t TT")
        for process in self.processes:
            print(process)

    def display_gantt_chart(self):
        print("\nGantt Chart:")
        # Print the process sequence
        for process in self.processes:
            print(f"|  {process.pid}  ", end="")
        print("|")

        # Print the time intervals below the process sequence

        print("0", end="")
        for process in self.processes:
            print(f"    {process.completion_time}", end="")
        print("\n")


if __name__ == "__main__":
    processes = [
        process("P1", 5, 0),
        process("P2", 3, 1),
        process("P3", 8, 2),
        process("P4", 6, 3),
    ]

    scheduler = Scheduler(processes)
    scheduler.FCFS()
    scheduler.display()
    scheduler.display_gantt_chart()
