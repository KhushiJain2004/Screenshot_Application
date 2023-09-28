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

# Add tabs to the Notebook
notebook.add(tab_about, text="About")
notebook.add(tab_single_screenshot, text="Single Screenshot")
notebook.add(tab_multiple_screenshot, text="Multiple Screenshots")

# Place the Notebook widget
notebook.pack(fill=tk.BOTH, expand=True)

#single screenshot tab layout
style = ttk.Style()
style.configure("CustomLabel.TLabel", font=("Times New Roman", 15, "bold"), foreground="black")
style.configure("Custom.TFrame",background="white")
label1=ttk.Label(tab_single_screenshot,text="SCREENSHOT APPLICATION",style="CustomLabel.TLabel")
label1.grid(row=0,column=0,columnspan=3,pady=20)

label2=ttk.Label(tab_single_screenshot,text="Single screenshots :) ")
label2.config(font=("Times New Roman",13,"bold"))
label2.grid(row=1,column=0,columnspan=3,pady=10)

frame1=ttk.Frame(tab_single_screenshot,height=10,style="Custom.TFrame")
frame1.grid(row=2,column=0,columnspan=3,pady=20)

label3=ttk.Label(frame1,text="Click capture button to take a single screenshot.")
label3.config(font=("Times New Roman", 13))
label3.grid(row=2,column=0,columnspan=2,pady=20)

capture=ttk.Button(frame1,text="Capture",command=None)
capture.grid(row=2,column=2,pady=20)

delay_label=tk.Label(frame1,text=" Enter a time delay :")
delay_label.grid(row=3,column=0,columnspan=1,pady=20)
delay_label.config(font=("Times New Roman", 13))

delay_entry=ttk.Entry(frame1)
delay_entry.grid(row=3,column=1,columnspan=1,pady=20)

capture_delay=ttk.Button(frame1,text="Capture with delay",command=None)
capture_delay.grid(row=3,column=2,pady=20)

root.mainloop()
