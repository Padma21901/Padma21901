import tkinter as tk
import tkinter.ttk as ttk
import datetime
import winsound

# Function to play sound
def play_sound():
    winsound.Beep(1000, 1000)

# Function to schedule reminder
def schedule_reminder():
    selected_day = day_var.get()
    selected_time = time_var.get()
    selected_activity = activity_var.get()
    
    # Get current day and time
    current_day = datetime.datetime.now().strftime('%A')
    current_time = datetime.datetime.now().strftime('%H:%M')
    
    # Calculate time difference
    time_difference = datetime.datetime.strptime(selected_time, '%H:%M') - datetime.datetime.strptime(current_time, '%H:%M')
    if time_difference.days < 0:  # If time has already passed for the day, schedule for the next day
        time_difference += datetime.timedelta(days=1)
    
    # Calculate seconds until reminder
    seconds_until_reminder = time_difference.total_seconds()
    
    # Schedule reminder
    root.after(int(seconds_until_reminder * 1000), play_sound)
    reminder_label.config(text=f"Reminder scheduled for {selected_day} at {selected_time} for {selected_activity}")

# Create main window
root = tk.Tk()
root.title("Reminder Application")

# Create dropdowns for day, time, and activity
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_var = tk.StringVar()
day_dropdown = ttk.Combobox(root, textvariable=day_var, values=days)
day_dropdown.grid(row=0, column=0, padx=5, pady=5)

times = [f"{i:02d}:00" for i in range(24)]
time_var = tk.StringVar()
time_dropdown = ttk.Combobox(root, textvariable=time_var, values=times)
time_dropdown.grid(row=0, column=1, padx=5, pady=5)

activities = ['Wake up', 'Go to gym', 'Breakfast', 'Meetings', 'Lunch', 'Quick nap', 'Go to library', 'Dinner', 'Go to sleep']
activity_var = tk.StringVar()
activity_dropdown = ttk.Combobox(root, textvariable=activity_var, values=activities)
activity_dropdown.grid(row=0, column=2, padx=5, pady=5)

# Create schedule button
schedule_button = tk.Button(root, text="Schedule Reminder", command=schedule_reminder)
schedule_button.grid(row=1, columnspan=3, padx=5, pady=5)

# Label to display reminder status
reminder_label = tk.Label(root, text="")
reminder_label.grid(row=2, columnspan=3, padx=5, pady=5)

root.mainloop()