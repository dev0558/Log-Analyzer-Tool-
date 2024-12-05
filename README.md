# Log Analyzer Tool

## Overview

The Log Analyzer Tool automates the process of analyzing server logs to detect potential security threats. It identifies suspicious IPs based on failed login attempts and provides:
- Detailed reports of suspicious activity.
- Visualizations for easier interpretation.
- Please read my report and also inspect my code to understand the tool in details

## Features

- **Interactive GUI**: User-friendly interface to select and analyze log files.
- **Regex-Powered Parsing**: Extracts failed login attempts from text-based logs.
- **Detailed Reporting**: Summarizes suspicious IPs and their activities.
- **Visualization**: Generates a bar chart showing failed login attempts.
- **Customizable**: Regex pattern can be tailored for various log formats.
- **Error Handling**: Handles file errors gracefully.

## Technologies Used

- **Python**: Main programming language.
- **re**: Regular expressions for log parsing.
- **tkinter**: Graphical interface.
- **matplotlib**: Data visualization.

## High-Level Algorithm

1. **Log File Selection**: Upload logs using the GUI.
2. **Log Analysis**: Parse logs to extract failed login attempts.
3. **Report Generation**: Create a text report of suspicious IPs.
4. **Visualization**: Generate and save a bar chart.

## Getting Started

### Prerequisites
- Python 3.6 or higher
- Install required libraries:
  ```bash
  pip install matplotlib



# Clone the repository
git clone https://github.com/dev0558/LogAnalyzer.git

# Change to the project directory
```bash
cd LogAnalyzer

Run the tool
```bash
python log_analyzer_gui.py


  Test logs provided as sample_logs.txt.
    Suspicious activity report saved as suspicious_activity_report.txt.
    Visualization saved as suspicious_activity_graph.png.
    

