import tkinter as tk
from tkinter import ttk
from cie3_final_algorithm import FIFOPageReplacement, LRUPageReplacement, OPTPageReplacement

class PageReplacementSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement Simulator")
        self.frame_count = 3
        self.algorithm = None

        # Create a style for improved appearance
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat")

        # Create algorithm selection
        self.create_algorithm_selection(style)

        # Create memory access pattern input
        self.create_memory_access_input(style)

        # Create start and clear buttons with improved style
        self.create_action_buttons(style)

        # Create a frame to display results
        self.result_frame = tk.Frame(root)
        self.result_frame.pack()
        self.create_table_headers()

    def create_algorithm_selection(self, style):
        algorithm_frame = tk.Frame(self.root)
        algorithm_frame.pack()

        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("Select")

        ttk.Label(algorithm_frame, text="Select Algorithm: ").pack(side=tk.LEFT, padx=5, pady=25)
        algorithm_menu = ttk.OptionMenu(algorithm_frame, self.algorithm_var,"Select", "FIFO", "LRU", "OPT")
        algorithm_menu.pack(side=tk.LEFT, padx=5)



    def create_memory_access_input(self, style):
        input_frame = tk.Frame(self.root)
        input_frame.pack()

        ttk.Label(input_frame, text="Memory Access Pattern (space-separated):").pack(side=tk.LEFT, padx=5, pady=25)

        self.input_text = tk.Entry(input_frame, width=40)
        self.input_text.pack(side=tk.LEFT, padx=5)

    def create_action_buttons(self, style):
        action_frame = tk.Frame(self.root)
        action_frame.pack()

        ttk.Button(action_frame, text="Start Simulation", command=self.start_simulation, style="TButton").pack(side=tk.LEFT, padx=5, pady=25)
        ttk.Button(action_frame, text="Clear", command=self.clear_results, style="TButton").pack(side=tk.LEFT, padx=5, pady=25)

    def create_table_headers(self):
        headers = ["Page", "Page Fault", "Eviction", "Replacement"]
        for col, header in enumerate(headers):
            header_label = tk.Label(self.result_frame, text=header, borderwidth=1, relief="solid", width=15)
            header_label.grid(row=0, column=col, sticky="nsew")

    def start_simulation(self):
        algorithm_choice = self.algorithm_var.get()
        access_pattern = self.input_text.get().split()

        if algorithm_choice == "FIFO":
            self.algorithm = FIFOPageReplacement(self.frame_count)
        elif algorithm_choice == "LRU":
            self.algorithm = LRUPageReplacement(self.frame_count)
        elif algorithm_choice == "OPT":
            self.algorithm = OPTPageReplacement(self.frame_count)

        # Perform simulation and display results
        self.clear_results()
        self.simulate(access_pattern)

    def simulate(self, access_pattern):
        for page in access_pattern:
            page_fault, eviction, replacement = self.algorithm.page_in(page, access_pattern)
            self.add_row_to_table(page, page_fault, eviction, replacement)

    def clear_results(self):
        for widget in self.result_frame.winfo_children():
            widget.grid_forget()
        self.create_table_headers()

    def add_row_to_table(self, page, page_fault, eviction, replacement):
        row = self.result_frame.grid_size()[1]
        page_label = tk.Label(self.result_frame, text=page, borderwidth=1, relief="solid", width=15)
        page_label.grid(row=row, column=0, sticky="nsew")

        # Determine if it's a page hit or page fault
        if page_fault == 1:
            hit_or_fault = "P"
        else:
            hit_or_fault = "H"
    
        fault_label = tk.Label(self.result_frame, text=hit_or_fault, borderwidth=1, relief="solid", width=15)
        fault_label.grid(row=row, column=1, sticky="nsew")
    
        eviction_label = tk.Label(self.result_frame, text=eviction, borderwidth=1, relief="solid", width=15)
        eviction_label.grid(row=row, column=2, sticky="nsew")
    
        replacement_label = tk.Label(self.result_frame, text=replacement, borderwidth=1, relief="solid", width=15)
        replacement_label.grid(row=row, column=3, sticky="nsew")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = PageReplacementSimulator(root)
    root.mainloop()
