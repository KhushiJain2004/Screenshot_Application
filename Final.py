import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Application Window")
root.geometry("+300+100")

# Create a Notebook widget
notebook = ttk.Notebook(root)

# Create tabs
tab_about = ttk.Frame(notebook,style="TFrame")
tab_single_screenshot = ttk.Frame(notebook,style="TFrame")
tab_multiple_screenshot = ttk.Frame(notebook,style="TFrame")


notebook.add(tab_about, text="About")
notebook.add(tab_single_screenshot, text="Single Screenshot")
notebook.add(tab_multiple_screenshot, text="Multiple Screenshots")

# Place the Notebook widget
notebook.pack(fill=tk.BOTH, expand=True)

root.mainloop()
