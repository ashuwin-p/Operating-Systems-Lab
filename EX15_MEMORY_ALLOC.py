class DynamicMemoryAllocator:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks
    
    def first_fit(self, processes):
        allocation = [None] * len(processes)
        process_num = 0
        for process_size in processes:
            allocated = False
            for idx, block_size in enumerate(self.memory_blocks):
                if block_size >= process_size:
                    temp = block_size
                    self.memory_blocks[idx] -= process_size
                    allocation[process_num] = idx + 1  # Index is 1-based for allocation
                    print(f"Process {process_num + 1} with size {process_size} allocated to Block {idx + 1} with size {temp}")
                    allocated = True
                    break
            
            if not allocated:
                print(f"Process {process_num + 1} with size {process_size} couldn't be allocated")
            
            process_num += 1

        return allocation

    def best_fit(self, processes):
        allocation = [None] * len(processes)
        process_num = 0
        for process_size in processes:
            best_idx = -1
            best_size = float('inf')
            for idx, block_size in enumerate(self.memory_blocks):
                if block_size >= process_size and (block_size - process_size) < best_size:
                    best_idx = idx
                    best_size = block_size - process_size
            
            if best_idx != -1:
                temp = self.memory_blocks[best_idx]
                self.memory_blocks[best_idx] -= process_size
                allocation[process_num] = best_idx + 1  # 1-based index for allocation
                print(f"Process {process_num + 1} with size {process_size} allocated to Block {best_idx + 1} with size {temp}")
            else:
                print(f"Process {process_num + 1} with size {process_size} couldn't be allocated")

            process_num += 1

        return allocation
    
    def worst_fit(self, processes):
        allocation = [None] * len(processes)
        process_num = 0
        for process_size in processes:
            worst_idx = -1
            worst_size = -1
            for idx, block_size in enumerate(self.memory_blocks):
                if block_size >= process_size and (block_size - process_size) > worst_size:
                    worst_idx = idx
                    worst_size = block_size - process_size
            
            if worst_idx != -1:
                temp = self.memory_blocks[worst_idx]
                self.memory_blocks[worst_idx] -= process_size
                allocation[process_num] = worst_idx + 1  # 1-based index for allocation
                print(f"Process {process_num + 1} with size {process_size} allocated to Block {worst_idx + 1} with size {temp}")
            else:
                print(f"Process {process_num + 1} with size {process_size} couldn't be allocated")

            process_num += 1

        return allocation
    
    def reset_memory(self, memory):
        self.memory_blocks = memory.copy()  # Ensures the internal state is reset from the original list.
            

if __name__ == '__main__':
    memory_blocks = [100, 500, 200, 300, 600]
    memory = memory_blocks.copy()  # Keep a copy of the original memory blocks for resetting
    MA = DynamicMemoryAllocator(memory_blocks)
    processes = [212, 417, 112, 426]

    print("\nFirst Fit Allocation\n")
    print(MA.first_fit(processes))
    MA.reset_memory(memory)

    print("\nBest Fit Allocation\n")
    print(MA.best_fit(processes))
    MA.reset_memory(memory)

    print("\nWorst Fit Allocation\n")
    print(MA.worst_fit(processes))
    MA.reset_memory(memory)
