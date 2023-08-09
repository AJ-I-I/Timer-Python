import tkinter as tk
from tkinter import messagebox
import threading
import time

def start_timer():
    global total_seconds
    total_seconds = int(entry_minutes.get()) * 60 + int(entry_seconds.get())
    if total_seconds <= 0:
        messagebox.showerror("Invalid Input", "Please enter a valid time.")
        return
    
    entry_minutes.config(state=tk.DISABLED)
    entry_seconds.config(state=tk.DISABLED)
    start_button.config(state=tk.DISABLED)
    
    update_timer()

def update_timer():
    global total_seconds
    if total_seconds > 0:
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        total_seconds -= 1
        timer_label.after(1000, update_timer)  # Update every 1 second
    else:
        messagebox.showinfo("Timer Finished", "Time's up!")
        entry_minutes.config(state=tk.NORMAL)
        entry_seconds.config(state=tk.NORMAL)
        start_button.config(state=tk.NORMAL)

# Create main window
root = tk.Tk()
root.title("Timer Program")
root.geometry("600x400")

# Create and place widgets
label_minutes = tk.Label(root, text="Minutes:")
label_minutes.pack(pady=10)
entry_minutes = tk.Entry(root)
entry_minutes.pack()

label_seconds = tk.Label(root, text="Seconds:")
label_seconds.pack(pady=10)
entry_seconds = tk.Entry(root)
entry_seconds.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=20)

timer_label = tk.Label(root, text="", font=("Helvetica", 48))
timer_label.pack()

# Start the main loop
root.mainloop()
