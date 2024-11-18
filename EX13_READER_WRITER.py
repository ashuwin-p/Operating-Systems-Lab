import threading
import random
import time

class Read_Write_Lock:
    def __init__(self):
        self.read_lock = threading.Semaphore()
        self.write_lock = threading.Semaphore(1)
        self.reader_count = 0
        self.reader_count_lock = threading.Lock()

    def acquire_read_lock(self):
        with self.reader_count_lock:
            self.reader_count += 1
            if self.reader_count == 1:
                self.acquire_write_lock()
    
    def release_read_lock(self):
        with self.reader_count_lock:
            self.reader_count -= 1
            if self.reader_count == 0:
                self.release_write_lock()
    
    def acquire_write_lock(self):
        self.write_lock.acquire()
    
    def release_write_lock(self):
        self.write_lock.release()

class Reader(threading.Thread):
    def __init__(self, id, rwlock, max_read):
        super().__init__()
        self.id = id
        self.rwlock = rwlock
        self.max_read = max_read
        self.read_count = 0
    
    def run(self):
        while self.read_count < self.max_read:
            time.sleep(random.uniform(1,2))

            self.rwlock.acquire_read_lock()
            print(f"Reader {self.id} is Reading")
            time.sleep(random.uniform(1,2))
            print(f"Reader {self.id} Finished Reading")
            self.rwlock.release_read_lock()
            self.read_count += 1
        print(f"Reader {self.id} Finished \n")

class Writer(threading.Thread):
    def __init__(self, id, rwlock, max_write):
        super().__init__()
        self.id = id
        self.rwlock = rwlock
        self.max_write = max_write
        self.write_count = 0
    
    def run(self):
        while self.write_count < self.max_write:
            time.sleep(random.uniform(1,2))

            self.rwlock.acquire_write_lock()
            print(f"Writer {self.id} is Writing")
            time.sleep(random.uniform(1,2))
            print(f"Writer {self.id} Finished Writing")
            self.rwlock.release_write_lock()
            self.write_count += 1
        print(f"Writer {self.id} Finished \n")  


class Reader_Writer_Problem:
    def __init__(self, num_reader, max_read, num_writer, max_write):
        self.num_reader = num_reader
        self.num_writer = num_writer
        self.max_read = max_read
        self.max_write = max_write
        self.rw_lock = Read_Write_Lock()

        self.readers = [Reader(i, self.rw_lock, self.max_read) for i in range (self.num_reader)]
        self.writers = [Writer(i, self.rw_lock, self.max_write) for i in range (self.num_writer)]

    def start_simulation(self):
        print("Starting Readers-Writers Simulation")

        for reader in self.readers:
            reader.start()
        
        for writer in self.writers:
            writer.start()

        for reader in self.readers:
            reader.join()

        for writer in self.writers:
            writer.join()
        
        print("Readers-Writers Simulation Completed")


if __name__ == '__main__':
    RWP = Reader_Writer_Problem(5,3,4,2)
    RWP.start_simulation()