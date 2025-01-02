# Automated Log Analyzer Tool

## Overview

The Log Analyzer Tool automates the process of analyzing server logs to detect potential security threats. It identifies suspicious IPs based on failed login attempts and provides:
- Detailed reports of suspicious activity.
- Visualizations for easier interpretation.
- Please read my report and also inspect my code to understand the tool in details
  - https://youtu.be/_cYnZaMLaac
  - Check out this video demonstration of the tool
## Features

- **Interactive GUI**: User-friendly interface to select and analyze log files.
- **Regex-Powered Parsing**: Extracts failed login attempts from text-based logs.
- **Detailed Reporting**: Summarizes suspicious IPs and their activities.
- **Visualization**: Generates a bar chart showing failed login attempts.
- **Customizable**: Regex pattern can be tailored for various log formats.
- **Error Handling**: Handles file errors gracefully.

-  # Log Analyzer Tool

## Description
A Python-based tool to analyze SSH logs for failed login attempts. It identifies suspicious IP addresses, generates a report, and visualizes the data.

## Features
- Extracts failed login attempts from SSH logs using regex.
- Aggregates and analyzes suspicious IPs.
- Generates text reports and graphical visualizations.
- User-friendly GUI for file selection and display.

## Core Components

### Log Analysis Engine
- **Custom Implementation**: Built using Python's native `re` (regular expression) module
- **Pattern Matching**: Uses regex pattern `r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"` to identify failed login attempts
- **Data Extraction**: Captures IP addresses from matched log entries

### Interface Components
1. **GUI Framework**
   - **Tool**: Tkinter (Python's standard GUI library)
   - **Version**: Native to Python 3.x
   - **Components**:
     - File selection dialog
     - Report display window
     - Error message boxes

2. **Visualization Tools**
   - **Library**: Matplotlib
   - **Output**: Bar chart visualization
   - **File Format**: PNG (suspicious_activity_graph.png)

3. **Data Processing**
   - **Module**: collections.Counter
   - **Purpose**: Aggregation of IP addresses and attempt counts
   - **Output Format**: Dictionary of IP addresses and frequencies

## Data Flow
1. Log File Input → Text file (.txt)
2. Pattern Matching → IP Address Extraction
3. Data Aggregation → Counter Object
4. Output Generation:
   - Text Report (suspicious_activity_report.txt)
   - Visual Graph (suspicious_activity_graph.png)
   - GUI Display

## Dependencies
- Python 3.x
- tkinter (built-in)
- matplotlib
- re (built-in)
- collections (built-in)

## File Processing
- **Input Format**: Text-based log files
- **Log Pattern**: Compatible with standard SSH log formats
- **Output Formats**:
  - Text report (.txt)
  - Visualization (.png)
  - GUI display (real-time)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dev0558/LogAnalyzerTool.git
   cd LogAnalyzerTool
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python log_analyzer.py
   ```
2. Select a log file using the GUI.
3. View the results in the GUI and check the output files:
   - **Text Report**: `suspicious_activity_report.txt`
   - **Graph**: `suspicious_activity_graph.png`

## Example
Input: A log file with SSH login attempts.

Output:
- `suspicious_activity_report.txt`:
  ```
  IP Address: 192.168.0.1, Failed Attempts: 5
  IP Address: 10.0.0.2, Failed Attempts: 3
  ```
- `suspicious_activity_graph.png`: A bar chart showing IP frequencies.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.



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
    

