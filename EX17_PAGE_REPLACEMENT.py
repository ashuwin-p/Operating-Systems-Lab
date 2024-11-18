from collections import deque

class FIFO:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.memory = deque(maxlen = max_capacity)
        self.page_faults = 0

    def memoryFull(self):
        return len(self.memory) == self.max_capacity
    
    def display(self):
        print("Memory Status : ",list(self.memory))
    
    def insert_page(self, page):
        if page not in self.memory:
            self.page_faults += 1
            print(f"\nPage Miss : Page {page}")
            if self.memoryFull():
                print(f"Removing Page {self.memory[0]} from Memory")
            
            print(f"Loading Page {page} into Memory")
            self.memory.append(page)
        else:
            print(f"\nPage Hit : Page {page}")
        
        self.display()
    
    def get_page_faults(self):
        return self.page_faults
    
# if __name__ == '__main__':
#     pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
#     capacity = 3 

#     PR = FIFO(capacity)

#     for page in pages:
#         PR.insert_page(page)
    
#     print(f"\nTotal Page Faults : {PR.get_page_faults()}\n")
            


class LRU:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.memory = []
        self.page_faults = 0

    def memoryFull(self):
        return len(self.memory) == self.max_capacity
    
    def display(self):
        print("Memory Status : ",list(self.memory))
    
    def insert_page(self, page):
        if page not in self.memory:
            self.page_faults += 1
            print(f"\nPage Miss : Page {page}")
            if self.memoryFull():
                lru_page = self.memory.pop(0)
                print(f"Removing Page {lru_page} from Memory")
            
            print(f"Loading Page {page} into Memory")
            self.memory.append(page)
        else:
            print(f"\nPage Hit : Page {page}, Updating Position ...")
            self.memory.remove(page)
            self.memory.append(page)
        
        self.display()
    
    def get_page_faults(self):
        return self.page_faults
    

# if __name__ == '__main__':
#     pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
#     capacity = 3 

#     PR = LRU(capacity)

#     for page in pages:
#         PR.insert_page(page)
    
#     print(f"\nTotal Page Faults : {PR.get_page_faults()}\n")


class OptimalPR:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.memory = []
        self.page_faults = 0

    def memoryFull(self):
        return len(self.memory) == self.max_capacity
    
    def display(self):
        print("Memory Status : ",list(self.memory))
    
    def insert_page(self, page, future_request):
        if page not in self.memory:
            self.page_faults += 1
            print(f"\nPage Miss : Page {page}")

            if self.memoryFull():
                optimal_page = self.find_optimal_page(page, future_request)
                self.memory.remove(optimal_page)
                print(f"Removing Page {optimal_page} from Memory")
            
            print(f"Loading Page {page} into Memory")
            self.memory.append(page)
        
        else:
            print(f"\nPage Hit : Page {page}")
        
        self.display()
    
    def find_optimal_page(self, page, future_request):
        optimal_page = None
        optimal_index = -1

        for current_page in self.memory:
            try:
                index = future_request.index(current_page)
            except:
                return current_page
            
            if index > optimal_index:
                optimal_index = index
                optimal_page = current_page

        return optimal_page
    
    def get_page_faults(self):
        return self.page_faults

if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 3 

    PR = OptimalPR(capacity)

    for idx, page in enumerate(pages):
        PR.insert_page(page, pages[idx+1 : ])
    
    print(f"\nTotal Page Faults : {PR.get_page_faults()}\n")