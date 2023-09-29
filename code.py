import time
import os
import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab
from tkinter import filedialog
from tkinter import font

root = tk.Tk()
root.title("Application Window")
root.geometry("+300+100")

#menu bar functions
path=None
def view_previous():
    if(path):
        os.startfile(path)

def open_folder():
    folder_path= filedialog.askdirectory()
    if(folder_path):
        os.startfile(folder_path)

# Create a Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create an "view" menu
view = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view)
view.add_command(label="View Folder",font=font.Font(family="Times New Roman", size=11 ),command=open_folder)
view.add_command(label="View Last screenshot",font=font.Font(family="Times New Roman", size=11),command=view_previous)

# Create an "Exit" menu
def exit_application():
    root.quit()
menu_bar.add_command(label="Exit", command=exit_application)


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

#single capture functions
def capture_single():
    status_label=tk.Label(tab_single_screenshot, text="")
    status_label.grid(row=3,column=0,columnspan=3,pady=20)
    
    root.withdraw()
    time.sleep(0.2)

    screenshot = ImageGrab.grab()
    global path
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    path=save_path
    if save_path:
        screenshot.save(save_path)
        status_label.config(text=f"Screenshot saved as {os.path.basename(save_path)}",font=("Times New Roman",13))

    root.deiconify()
    folder_message = ttk.Label(root, text=f"Screenshots saved in folder: {save_path}  :)")
    folder_message.pack(pady=20)

def start_countdown(delay):
    countdown_label=ttk.Label(tab_single_screenshot, text="")
    countdown_label.grid(row=3,column=0,columnspan=3)
    countdown_label.config(text=f"Taking a screenshot in {delay} seconds...",font=("Times New Roman",13))
    tab_single_screenshot.update()  # Update the GUI to show the countdown label

    for remaining_time in range(delay, -1, -1):
        countdown_label.config(text=f"Taking a screenshot in {remaining_time} seconds...")
        tab_single_screenshot.update()  # Update the GUI to show the updated countdown label
        time.sleep(1)

    countdown_label.grid_forget()
    
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

capture=ttk.Button(frame1,text="Capture",command=capture_single)
capture.grid(row=2,column=2,pady=20)

delay_label=tk.Label(frame1,text=" Enter a time delay :")
delay_label.grid(row=3,column=0,columnspan=1,pady=20)
delay_label.config(font=("Times New Roman", 13))

delay_entry=ttk.Entry(frame1)
delay_entry.grid(row=3,column=1,columnspan=1,pady=20)

capture_delay=ttk.Button(frame1,text="Capture with delay",command=None)
capture_delay.grid(row=3,column=2,pady=20)

root.mainloop()