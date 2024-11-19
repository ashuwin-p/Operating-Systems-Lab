# Page Preplacement Algorithms

class FIFO:
    def __init__(self, capacity):
        self.memory = []
        self.capacity = capacity
        self.page_fault = 0
    
    def isFull(self):
        return self.capacity == len(self.memory)
        
    def insert_page(self, page):
        before = self.memory.copy()
        if not page in self.memory:
            self.page_fault += 1
            if self.isFull():
                self.memory.pop(0)
            self.memory.append(page)
            
            print(f"{str(before):<15} {page} \t MISS \t {self.memory}")


        
        else:
            print(f"{str(before):<15} {page} \t HIT \t {self.memory}")

    
    def run(self, pages):
        print(f"{'BEFORE':<15} PAGE \t STATUS \t AFTER")

        for page in pages:
            self.insert_page(page)
        
        print(f"\nFAULT RATIO : {self.page_fault / len(pages)}")
        print(f"\nHIT RATIO   : {(len(pages) - self.page_fault) / len(pages)}")
        

if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    PR = FIFO(3)
    PR.run(pages)
        


class LRU:
    def __init__(self, capacity):
        self.memory = []
        self.capacity = capacity
        self.page_fault = 0
    
    def isFull(self):
        return self.capacity == len(self.memory)
        
    def insert_page(self, page):
        before = self.memory.copy()
        if not page in self.memory:
            self.page_fault += 1
            if self.isFull():
                self.memory.pop(0)
            self.memory.append(page)
            
            print(f"{str(before):<15} {page} \t MISS \t {self.memory}")


        
        else:
            self.memory.remove(page)
            self.memory.append(page)
            print(f"{str(before):<15} {page} \t HIT \t {self.memory}")

    
    def run(self, pages):
        print(f"{'BEFORE':<15} PAGE \t STATUS \t AFTER")

        for page in pages:
            self.insert_page(page)
        
        print(f"\nFAULT RATIO : {self.page_fault / len(pages)}")
        print(f"\nHIT RATIO   : {(len(pages) - self.page_fault) / len(pages)}")
        

if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    PR = LRU(3)
    PR.run(pages)


# Page Preplacement Algorithms

class OPTIMAL_PR:
    def __init__(self, capacity):
        self.memory = []
        self.capacity = capacity
        self.page_fault = 0
    
    def isFull(self):
        return self.capacity == len(self.memory)
        
    def insert_page(self, page, future_request):
        before = self.memory.copy()
        if not page in self.memory:
            self.page_fault += 1
            if self.isFull():
                page_remove = self.get_optimal(page, future_request)
                self.memory.remove(page_remove)
                
            self.memory.append(page)
            
            print(f"{str(before):<15} {page} \t MISS \t {self.memory}")


        
        else:
            print(f"{str(before):<15} {page} \t HIT \t {self.memory}")
    
    def get_optimal(self, page, future_request):
        optimal_page = None
        optimal_index = -1
        
        for page in self.memory:
            try:
                index = future_request.index(page)
            except:
                return page
            
            if index > optimal_index:
                optimal_index = index
                optimal_page = page
        
        return optimal_page

    
    def run(self, pages):
        print(f"{'BEFORE':<15} PAGE \t STATUS \t AFTER")

        for i, page in enumerate(pages):
            self.insert_page(page, pages[i+1 : ])
        
        print(f"\nFAULT RATIO : {self.page_fault / len(pages)}")
        print(f"\nHIT RATIO   : {(len(pages) - self.page_fault) / len(pages)}")
        

if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    PR = OPTIMAL_PR(3)
    PR.run(pages)
