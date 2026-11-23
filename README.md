# Smart IT Ticket System (CLI Service Desk & SLA Tracker)

> **Tech Stack:** Python 3 (`datetime`, `matplotlib`, `openpyxl`) | **Focus:** IT Service Desk Automation, Incident Triage & SLA Tracking

## 1. Executive Summary & Project Purpose
Designed and built the **Smart IT Ticket System** to solve a common operational challenge in multi-site IT service desk environments: **tracking incident response times, technician productivity, and SLA compliance in real time.**

This tool provides a lightweight Command-Line Interface (CLI) for logging retail/store technical issues (`Till`, `KDS`, `Network`, `DayEnd`, `Online Ordering`, `MX`), generating instant technician shift summaries, exporting structured Excel reports, and flagging open tickets before they breach a **24-hour SLA**.

---

## 2. Project Evolution
The system was built iteratively across four distinct phases, demonstrating progressive growth in Python software development, data structures, and operational reporting:

| Stage | Feature Focus | Core Technical Skills |
| :--- | :--- | :--- |
| **Phase 1: Basic Counter** | Simple loops to log and count incoming store issues. | Variables, Control Flow, User Input |
| **Phase 2: List Management** | Stored multiple ticket properties dynamically in memory. | Data Structures, Dictionaries & Lists |
| **Phase 3: SLA & Timestamps** | Integrated `datetime` modules to track exact ticket lifespan. | Logic Design, Time Delta Calculations |
| **Phase 4: Analytics & Automation** | Added stacked bar charts and automated Excel reporting. | Data Visualization (`matplotlib`), File I/O (`openpyxl`) |

---

## 3. System Architecture & Capabilities

```mermaid
flowchart TD
    Incident([Store Incident Reported]) --> AddTicket[1. Add Ticket CLI]
    AddTicket --> Store[(In-Memory Ticket Store)]

    Store --> Shift[2. Shift Report\nSummary by Technician]
    Store --> Graph[3. Performance Graph\nStacked Bar Chart]
    Store --> Excel[4. Export to Excel\nticket_report.xlsx]
    Store --> SLA[5. SLA Alerts\n20+ Hour Pre-Breach Warning]
```

### Core Functions
* **`add_ticket()`**: Logs technician name, store location, issue category (`KDS`, `DayEnd`, `Online Ordering`, `MX`, `Network`, `Till Issue`), timestamp, and ticket status (`Open`, `OnHold`, `Onsite`, `Closed`).
* **`shift_report()`**: Generates instant counts of active and total worked tickets per technician for shift handovers.
* **`performance_graph()`**: Uses `matplotlib` to render stacked bar charts visualizing technician workload distribution by ticket status (featuring fixed bar widths, custom status colors, and integer Y-axis scaling).
* **`export_excel()`**: Uses `openpyxl` to write ticket records into a structured Excel spreadsheet (`ticket_report.xlsx`) for management reporting.
* **`sla_alert()`**: Scans open incidents and flags tickets exceeding **20 hours** as **Proactive Pre-Breach Alerts** before violating the **24-hour SLA**.

---

## 4. Execution Process

### Prerequisites
```bash
pip install matplotlib openpyxl
```

### Run the Program
```bash
git clone https://github.com
cd Smart-IT-Ticketing-System/IT_Ticket_Project
python ticket_system.py
```

The main menu appears:

<img width="975" height="353" alt="image" src="https://github.com/user-attachments/assets/8cbbb112-c946-4e66-a18f-ef312d3360ee" />


---

## 5. System Output Walkthrough

### Step 1: Application Menu & Data Entry

<img width="975" height="350" alt="image" src="https://github.com/user-attachments/assets/a6ed2edb-5737-4bf8-81ce-dc080851155e" />


### Step 2: Automated Shift Summary & Excel Export
Generated Spreadsheet Data (`ticket_report.xlsx`):

<img width="973" height="386" alt="image" src="https://github.com/user-attachments/assets/4779742e-6fd1-47d1-90cd-08e3c41b7c83" />
<img width="975" height="202" alt="image" src="https://github.com/user-attachments/assets/53c699a8-1103-4ade-8070-ed0b980f7f21" />



### Step 3: Visual Performance Analytics
Selecting Option 3 generates an interactive graph visualizing workload distribution per technician.

**Custom Features:** Fixed bar widths, custom color palette for statuses, and non-decimal Y-axis scaling.

<img width="975" height="337" alt="image" src="https://github.com/user-attachments/assets/580ab2dd-3315-4985-94ac-ff98a43ca3b1" />


---

## 6. Conclusion
The **Smart IT Ticket System** demonstrates how Python automation streamlines manual service desk workflows. By combining script-driven SLA tracking with automated Excel exports and visual analytics, the tool reduces manual reporting errors and gives IT support leads real-time visibility into ticket resolution and SLA compliance.
