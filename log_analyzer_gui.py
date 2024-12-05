import tkinter as tk
from tkinter import filedialog, messagebox
import re
from collections import Counter
import matplotlib.pyplot as plt

def analyze_log_file(file_path):
    """Analyze the log file for failed login attempts and return a list of suspicious IPs."""
    suspicious_ips = []
    failed_login_pattern = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

    try:
        with open(file_path, 'r') as file:
            for line in file:
                match = failed_login_pattern.search(line)
                if match:
                    suspicious_ips.append(match.group(1))
    except Exception as e:
        messagebox.showerror("Error", f"Error reading log file: {e}")
        return []

    return suspicious_ips

def generate_report(ips):
    """Generate a report of suspicious IP addresses and display it."""
    if not ips:
        messagebox.showinfo("Report", "No suspicious activity detected.")
        return None

    ip_counts = Counter(ips)
    report = "Suspicious Activity Report:\n\n"
    report += "IP Address\t\tFailed Attempts\n"
    report += "-" * 40 + "\n"
    for ip, count in ip_counts.items():
        report += f"{ip}\t\t{count}\n"

    # Display report in a new window
    report_window = tk.Toplevel(root)
    report_window.title("Suspicious Activity Report")
    report_text = tk.Text(report_window, wrap=tk.WORD)
    report_text.insert(tk.END, report)
    report_text.pack(fill=tk.BOTH, expand=True)

    # Save report to file
    try:
        with open("suspicious_activity_report.txt", "w") as file:
            file.write(report)
    except Exception as e:
        messagebox.showerror("Error", f"Error saving report: {e}")

    return ip_counts

def visualize_data(ip_counts):
    """Visualize the suspicious activity data using a bar chart."""
    if not ip_counts:
        return

    ips = list(ip_counts.keys())
    counts = list(ip_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(ips, counts, color='skyblue')
    plt.xlabel("IP Addresses")
    plt.ylabel("Failed Login Attempts")
    plt.title("Suspicious Login Attempts by IP")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Save graph to file
    try:
        plt.savefig("suspicious_activity_graph.png")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving graph: {e}")

    plt.show()

def select_file_and_analyze():
    """Allow the user to select a log file and analyze it."""
    file_path = filedialog.askopenfilename(filetypes=[("Log Files", "*.txt")])
    if not file_path:
        return

    suspicious_ips = analyze_log_file(file_path)
    ip_counts = generate_report(suspicious_ips)
    visualize_data(ip_counts)

# GUI Setup
root = tk.Tk()
root.title("Log Analyzer")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Log Analyzer Tool", font=("Helvetica", 16))
label.pack()

button = tk.Button(frame, text="Select Log File and Analyze", command=select_file_and_analyze)
button.pack(pady=10)

root.mainloop()

