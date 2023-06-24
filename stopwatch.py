import tkinter as tk
import time
import math

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch App")

        self.is_running = False
        self.start_time = 0
        self.lap_start_time = 0
        self.lap_times = []

        # Create GUI elements
        self.elapsed_var = tk.StringVar()
        self.lap_var = tk.StringVar()

        self.elapsed_label = tk.Label(root, textvariable=self.elapsed_var, font=("Helvetica", 24))
        self.elapsed_label.pack(pady=10)

        self.lap_label = tk.Label(root, textvariable=self.lap_var, font=("Helvetica", 18))
        self.lap_label.pack(pady=5)

        self.lap_listbox = tk.Listbox(root, font=("Helvetica", 14), width=20, height=10)
        self.lap_listbox.pack(pady=5)

        self.start_button = tk.Button(root, text="Start", command=self.toggle_stopwatch)
        self.start_button.pack(pady=5)

        self.lap_button = tk.Button(root, text="Lap", command=self.record_lap)
        self.lap_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_stopwatch)
        self.reset_button.pack(pady=5)

        # Start the stopwatch display
        self.update_elapsed_time()
        self.update_lap_time()

    def format_time(self, minutes, seconds, milliseconds):
        """Formats time into string format MM:SS.mmm"""
        return f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

    def update_elapsed_time(self):
        """Updates the elapsed time label"""
        if self.is_running:
            elapsed_time = time.time() - self.start_time
            minutes = math.floor(elapsed_time // 60)
            seconds = math.floor(elapsed_time % 60)
            milliseconds = math.floor((elapsed_time % 1) * 1000)
            self.elapsed_var.set(self.format_time(minutes, seconds, milliseconds))
        self.root.after(1, self.update_elapsed_time)

    def update_lap_time(self):
        """Updates the lap time label"""
        if self.is_running:
            lap_elapsed_time = time.time() - self.lap_start_time
            minutes = math.floor(lap_elapsed_time // 60)
            seconds = math.floor(lap_elapsed_time % 60)
            milliseconds = math.floor((lap_elapsed_time % 1) * 1000)
            self.lap_var.set(self.format_time(minutes, seconds, milliseconds))
        self.root.after(1, self.update_lap_time)

    def toggle_stopwatch(self):
        """Starts or stops the stopwatch based on its current state"""
        if not self.is_running:
            self.start_stopwatch()
        else:
            self.stop_stopwatch()

    def start_stopwatch(self):
        """Starts the stopwatch"""
        self.is_running = True
        if self.start_time == 0:
            self.start_time = time.time()
        if self.lap_start_time == 0:
            self.lap_start_time = self.start_time
        self.start_button.config(text="Stop")

    def stop_stopwatch(self):
        """Stops the stopwatch"""
        self.is_running = False
        self.start_button.config(text="Start")

    def record_lap(self):
        """Records a lap time"""
        if self.is_running:
            lap_elapsed_time = time.time() - self.lap_start_time
            self.lap_times.append(lap_elapsed_time)
            minutes = math.floor(lap_elapsed_time // 60)
            seconds = math.floor(lap_elapsed_time % 60)
            milliseconds = math.floor((lap_elapsed_time % 1) * 1000)
            lap_text = f"Lap {len(self.lap_times)}: {self.format_time(minutes, seconds, milliseconds)}"
            self.lap_listbox.insert(tk.END, lap_text)
            self.lap_start_time = time.time()

    def reset_stopwatch(self):
        """Resets the stopwatch"""
        self.is_running = False
        self.start_button.config(text="Start")
        self.elapsed_var.set("00:00.000")
        self.lap_var.set("")
        self.start_time = 0
        self.lap_start_time = 0
        self.lap_times.clear()
        self.lap_listbox.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
