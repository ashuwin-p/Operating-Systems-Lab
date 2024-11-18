import time
import random
import threading


class Philosopher(threading.Thread):
    def __init__(self, id, left_fork, right_fork, max_eat):
        super().__init__()
        self.id = id
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.max_eat = max_eat
        self.eat_count = 0

    def think(self):
        print(f"Philosopher {self.id} is Thinking")
        time.sleep(random.uniform(1, 2))

    def eat(self):
        print(f"Philosopher {self.id} is Hungry")
        with self.left_fork:
            print(f"Philosopher {self.id} picked up left fork")
            with self.right_fork:
                print(f"Philosopher {self.id} picked up right fork")
                print(f"Philosopher {self.id} is Eating")
                time.sleep(random.uniform(1, 2))

        self.eat_count += 1
        print(f"Philosopher {self.id} finished Eating and released the forks \n")

    def run(self):
        while self.eat_count < self.max_eat:
            self.think()
            self.eat()


class DiningPhilosophers:
    def __init__(self, num_phil, max_eat):
        self.num_phil = num_phil
        self.max_eat = max_eat
        self.forks = [threading.Semaphore(1) for _ in range(self.num_phil)]
        self.philosophers = [
            Philosopher(
                i, 
                self.forks[i], 
                self.forks[(i + 1) % self.num_phil], 
                self.max_eat
            )
            for i in range(self.num_phil)
        ]

    def start_dining(self):
        print("Started Dining Philosopher Problem")

        for philosopher in self.philosophers:
            philosopher.start()

        for philosopher in self.philosophers:
            philosopher.join()


if __name__ == "__main__":
    DF = DiningPhilosophers(5, 1)
    DF.start_dining()
    print("Finished Dining Philosopher Problem")
