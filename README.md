Project started 01/03/2026:  Smart IT Ticket System 
Technical Documentation & Demonstration Manual 
1. Executive Summary & Project Purpose 
I designed and built the Smart IT Ticket System to solve a common operational challenge in IT service desk environments: tracking incident response times, technician productivity, and SLA compliance in real time. 
This tool provides a lightweight, command-line interface for logging store issues (Till, KDS, Network, EOD errors), generating shift summaries, exporting reports to Excel, and monitoring critical SLA threshold breaches. 
2. Project Evolution 
The system was built iteratively across four distinct phases, demonstrating progressive growth in Python software development and data handling: 
Stage 	Feature Focus 	Core Technical Skills 
Phase 1: Basic Counter 	Simple loops to log and count incoming store issues. 	Variables, Control Flow, User Input 
Phase 2: List 
Management 	Stored multiple ticket properties dynamically in memory. 	Data Structures, Dictionaries & Lists 
Phase 3: SLA & Timestamps 	Integrated datetime modules to track ticket lifespan. 	Logic Design, Time Calculations 
Phase 4: Analytics & Automation 	Added visual stacked bar graphs and automated Excel reporting. 	Data Visualization (matplotlib), File I/O (openpyxl) 
3. System Architecture & Capabilities 
 
 
 
 
 
Core Functions: 
•	add_ticket(): Logs technician name, store location, issue type (KDS, DayEnd, Online Ordering, MX, Network, Till Issue), and status (Open, Onsite, Closed). 
•	shift_report(): Generates instant counts of active and total worked tickets per technician. 
•	performance_graph(): Uses matplotlib to render stacked bar charts showing technician performance by ticket status. 
•	export_excel(): Uses openpyxl to write data into structured Excel spreadsheets (ticket_report.xlsx). 
•	sla_alert(): Scans open incidents and flags tickets exceeding 20 hours as Proactive Pre-Breach Alerts before violating the 24-hour SLA. 4. Execution Process 
To run the program: 
bash 
cd "C:\Users\Fhumulani\OneDrive\Desktop\IT_Ticket_Project" python ticket_system.py The menu appears: 
  
5. System Output Walkthrough 
Step 1: Application Menu & Data Entry 
  
Step 2: Automated Excel Export Generated Spreadsheet Data: 
  
  
Step 3: Visual Performance Analytics 
Selecting Option 3 generates an interactive graph visualizing workload distribution per technician. 
Custom Features: Fixed bar widths, custom color palette for statuses, non-decimal Y-axis scaling. 
  
 
Conclusion 
The Smart IT Ticketing System successfully demonstrates how Python automation can streamline manual ticket management and IT operational workflows. By integrating script-driven data processing directly with spreadsheet outputs, the project eliminates manual data entry, reduces error rates, and speeds up SLA reporting. Overall, this tool provides a scalable, efficient foundation for managing service desk tickets, offering management clear visibility into technical support performance and issue resolution. 
