import tkinter as tk
import pyautogui
import datetime
import random
import time
import threading

def move_mouse(start_hour, end_hour):
    while True:
        now = datetime.datetime.now()
        if now.hour >= start_hour and now.hour < end_hour:
            x = random.randint(400, 500) # generate a random x coordinate
            y = random.randint(400, 500) # generate a random y coordinate
            pyautogui.moveTo(x, y, duration=0.5) # move the mouse cursor to the random position
            time.sleep(5) # wait for 10 seconds
        else:
            break

def run_program():
    start_hour = int(start_hour_entry.get())
    end_hour = int(end_hour_entry.get())
    threading.Thread(target=move_mouse, args=(start_hour, end_hour)).start()

def stop_program():
    pyautogui.FAILSAFE = True
    pyautogui.click()

root = tk.Tk()
root.title("Mouse Movement Program")
root.geometry("400x250")

start_hour_label = tk.Label(root, text="Starting hour (24-hour format):")
start_hour_label.pack(pady=5)
start_hour_entry = tk.Entry(root)
start_hour_entry.pack(pady=5)

end_hour_label = tk.Label(root, text="Ending hour (24-hour format):")
end_hour_label.pack(pady=5)
end_hour_entry = tk.Entry(root)
end_hour_entry.pack(pady=5)

run_button = tk.Button(root, text="Run", command=run_program)
run_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_program)
stop_button.pack(pady=10)

root.mainloop()
