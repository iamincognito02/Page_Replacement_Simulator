# Virtual Memory Page Replacement Simulator

This Python application simulates and visualizes three popular virtual memory page replacement algorithms: FIFO (First-In-First-Out), LRU (Least Recently Used), and OPT (Optimal). It provides an educational tool for understanding these algorithms and allows users to experiment with different memory access patterns.

## Features
- **Algorithm Selection**: Choose from FIFO, LRU, or OPT.
- **Custom Memory Access Pattern Input**: Input a space-separated list of page numbers.
- **Visual Feedback**: Displays page hits, faults, evictions, and replacements.
- **Performance Metrics**: Analyze the number of page faults, hits, and replacements.
- **Educational Tool**: Helps users understand virtual memory management in real-world systems.

## Page Replacement Algorithms

### FIFO (First-In-First-Out)
- **Description**: FIFO is a straightforward page replacement algorithm that evicts the oldest page in memory when a page fault occurs. The page at the head of the list (oldest) is replaced by the new page.
- **Implementation**:
    ```python
    class FIFOPageReplacement(PageReplacementAlgorithm):
        def page_in(self, page, access_pattern):
            page_fault, eviction, replacement = 0, 0, 0
            if page not in self.frames:
                page_fault = 1
                if len(self.frames) < self.frame_count:
                    self.frames.append(page)
                else:
                    eviction = 1
                    self.frames.pop(0)
                    self.frames.append(page)
                    replacement = 1
            return page_fault, eviction, replacement
    ```

### LRU (Least Recently Used)
- **Description**: LRU replaces the page that has not been used for the longest time. It maintains a record of the order in which pages are accessed and evicts the least recently used page when a page fault occurs.
- **Implementation**:
    ```python
    class LRUPageReplacement(PageReplacementAlgorithm):
        def page_in(self, page, access_pattern):
            page_fault, eviction, replacement = 0, 0, 0
            if page not in self.frames:
                page_fault = 1
                if len(self.frames) >= self.frame_count:
                    eviction = 1
                    lru_page_index = self.find_lru_page(access_pattern)
                    self.frames.pop(lru_page_index)
                self.frames.append(page)
            return page_fault, eviction, replacement
    ```

### OPT (Optimal)
- **Description**: OPT replaces the page that will not be used for the longest time in the future. This algorithm is considered optimal as it minimizes page faults, but it is impractical for real systems because it requires future knowledge of page accesses.
- **Implementation**:
    ```python
    class OPTPageReplacement(PageReplacementAlgorithm):
        def page_in(self, page, access_pattern):
            page_fault, eviction, replacement = 0, 0, 0
            if page not in self.frames:
                page_fault = 1
                if len(self.frames) >= self.frame_count:
                    eviction = 1
                    farthest_used = -1
                    page_to_replace = None
                    for i, frame in enumerate(self.frames):
                        if frame not in access_pattern[i:]:
                            page_to_replace = frame
                            break
                        distance = access_pattern[i:].index(frame)
                        if distance > farthest_used:
                            farthest_used = distance
                            page_to_replace = frame
                    self.frames.remove(page_to_replace)
                self.frames.append(page)
            return page_fault, eviction, replacement
    ```

## User Interface
- **Algorithm Selection**: Choose one of the three page replacement algorithms (FIFO, LRU, or OPT).
- **Memory Access Pattern Input**: Enter a space-separated list of page numbers.
- **Start Simulation**: Initiates the simulation with the selected algorithm and input pattern.
- **Clear Results**: Clears previous simulation results.
- **Results Display**: Shows the status of each page (Page Hit or Page Fault) and indicates if an eviction or replacement occurred.

## Performance Metrics
- **Page Fault (P)**: Occurs when the accessed page is not found in memory, leading to a replacement.
- **Page Hit (H)**: Occurs when the accessed page is already in memory.
- **Eviction**: When a page is removed from memory to make space for a new page.
- **Replacement**: When a page is replaced due to a page fault.

## Output
![GUI (1)](https://github.com/user-attachments/assets/cb2a56f9-2100-4fcf-99f5-23b5250172d0)
![GUI (2)](https://github.com/user-attachments/assets/bb2bc71a-d491-46db-b2aa-3a5e97a0230a)
![GUI (3)](https://github.com/user-attachments/assets/1f11f632-21f4-4812-ba83-16b7bbb3e4db)
![GUI (4)](https://github.com/user-attachments/assets/dd7ad1ed-6076-4243-abeb-58f4d1aa8d53)

