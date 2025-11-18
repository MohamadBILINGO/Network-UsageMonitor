# Network-UsageMonitor

# 🚀 Advanced Real-Time Network Monitor

**Advanced Real-Time Network Monitor** is a sleek and intuitive graphical tool that tracks your system's network traffic in real-time. Whether you're curious about your upload/download speeds or need detailed network stats, this tool makes it easy to monitor and analyze your network activity live.

## 🌟 Key Features:

- **Real-Time Table View** – See the current time, incoming/outgoing speeds, maximum and average speeds in an easy-to-read table.
- **Dynamic Live Chart** – Network traffic chart updates live with color-coded speeds (green, orange, red for incoming; blue, purple, red for outgoing).
- **Save Data to CSV** – Export your network stats to CSV for future analysis.
- **Clear Data Anytime** – Reset the table and chart with a single click.
- **Simple and Lightweight GUI** – Built with Tkinter for a smooth user experience.

## 🛠 Requirements:

- Python 3.x
- Libraries:
  - `psutil`
  - `matplotlib`
  - `tkinter` (usually included with Python)

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

Simply run the script:

```bash
python NetMon.py
```

A sleek window will open displaying live network traffic in both table and chart formats.

## 💾 CSV Export:

- **Save Data:** Click the "Save Data to CSV" button and choose where to save the file.
- **Clear Data:** Click the "Clear Data" button to wipe the table and chart for a fresh start.

## 🎨 Color Coding in Charts:

- **Incoming Speeds:** 
  - Green: < 500 KB/s  
  - Orange: 500–1000 KB/s  
  - Red: > 1000 KB/s
- **Outgoing Speeds:**  
  - Blue: < 500 KB/s  
  - Purple: 500–1000 KB/s  
  - Red: > 1000 KB/s

This makes it easy to spot spikes and monitor network performance at a glance.

## 📄 License

This project is licensed under the **MIT License** – see the `LICENSE` file for details.Just use for Educational purposes 

> ⚡ **Tip:** Keep this monitor running in the background while downloading, streaming, or gaming to see how your network behaves in real-time!




