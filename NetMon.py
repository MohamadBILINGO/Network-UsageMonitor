import psutil
import time
import csv
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from collections import deque
import threading

class AdvancedNetworkMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Real-Time Network Monitor")
        self.root.geometry("900x550")
        
        # تنظیم جدول
        columns = ("Time", "In KB/s", "Out KB/s", "Max In", "Max Out", "Avg In", "Avg Out")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")
        self.tree.pack(side="top", fill="x")
        
        # دکمه‌ها
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        self.save_button = tk.Button(btn_frame, text="Save Data to CSV", command=self.save_csv)
        self.save_button.pack(side="left", padx=10)
        self.clear_button = tk.Button(btn_frame, text="Clear Data", command=self.clear_data)
        self.clear_button.pack(side="left", padx=10)
        
        # نمودار
        self.fig, self.ax = plt.subplots(figsize=(9,3))
        self.ax.set_title("Network Traffic (KB/s)")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Speed (KB/s)")
        self.ax.grid(True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        
        # مقادیر اولیه
        self.prev_net_io = psutil.net_io_counters()
        self.times = deque(maxlen=50)
        self.in_speeds = deque(maxlen=50)
        self.out_speeds = deque(maxlen=50)
        self.data_records = []
        
        # بروزرسانی
        self.update_interval = 1000  # میلی‌ثانیه
        self.lock = threading.Lock()
        self.update_traffic()
    
    def update_traffic(self):
        curr_net_io = psutil.net_io_counters()
        
        # تغییرات
        bytes_in = curr_net_io.bytes_recv - self.prev_net_io.bytes_recv
        bytes_out = curr_net_io.bytes_sent - self.prev_net_io.bytes_sent
        speed_in_kbps = (bytes_in / 1024) / (self.update_interval / 1000)
        speed_out_kbps = (bytes_out / 1024) / (self.update_interval / 1000)
        
        current_time = time.strftime("%H:%M:%S")
        
        # اضافه کردن به جدول
        max_in = max(list(self.in_speeds)+[speed_in_kbps])
        max_out = max(list(self.out_speeds)+[speed_out_kbps])
        avg_in = (sum(self.in_speeds)+speed_in_kbps)/(len(self.in_speeds)+1)
        avg_out = (sum(self.out_speeds)+speed_out_kbps)/(len(self.out_speeds)+1)
        
        self.tree.insert("", "end", values=(current_time, f"{speed_in_kbps:.2f}", f"{speed_out_kbps:.2f}",
                                            f"{max_in:.2f}", f"{max_out:.2f}", f"{avg_in:.2f}", f"{avg_out:.2f}"))
        self.tree.yview_moveto(1)
        
        # ذخیره داده‌ها
        self.data_records.append([current_time, speed_in_kbps, speed_out_kbps, max_in, max_out, avg_in, avg_out])
        
        # نمودار
        self.times.append(current_time)
        self.in_speeds.append(speed_in_kbps)
        self.out_speeds.append(speed_out_kbps)
        self.ax.clear()
        color_in = "green" if speed_in_kbps < 500 else "orange" if speed_in_kbps < 1000 else "red"
        color_out = "blue" if speed_out_kbps < 500 else "purple" if speed_out_kbps < 1000 else "red"
        self.ax.plot(self.times, self.in_speeds, label="In KB/s", color=color_in)
        self.ax.plot(self.times, self.out_speeds, label="Out KB/s", color=color_out)
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Speed (KB/s)")
        self.ax.set_title("Network Traffic (KB/s)")
        self.ax.legend()
        self.ax.grid(True)
        self.fig.autofmt_xdate()
        self.canvas.draw()
        
        self.prev_net_io = curr_net_io
        self.root.after(self.update_interval, self.update_traffic)
    
    def save_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files","*.csv")])
        if file_path:
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Time", "In KB/s", "Out KB/s", "Max In", "Max Out", "Avg In", "Avg Out"])
                writer.writerows(self.data_records)
            messagebox.showinfo("Saved", f"Data saved to {file_path}")
    
    def clear_data(self):
        with self.lock:
            self.tree.delete(*self.tree.get_children())
            self.times.clear()
            self.in_speeds.clear()
            self.out_speeds.clear()
            self.data_records.clear()
            self.ax.clear()
            self.ax.set_title("Network Traffic (KB/s)")
            self.ax.set_xlabel("Time")
            self.ax.set_ylabel("Speed (KB/s)")
            self.ax.grid(True)
            self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedNetworkMonitor(root)
    root.mainloop()
