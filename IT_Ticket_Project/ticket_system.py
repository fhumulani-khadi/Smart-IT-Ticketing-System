import matplotlib.pyplot as plt
from openpyxl import Workbook
from datetime import datetime

tickets = []

# ================= 1. ADD TICKET =================
def add_ticket():
    tech = input("Technician name: ").lower().strip()
    store = input("Store name: ").strip()
    ttype = input("Type (KDS / DayEnd / Online Ordering / MX / Network / Till Issue): ").strip()
    status = input("Status (Closed / OnHold / Onsite / Open / In Progress): ").lower().strip()

    ticket = {
        "tech": tech,
        "store": store,
        "type": ttype,
        "status": status,
        "time": datetime.now(),
        "shift_date": datetime.now().date()
    }

    tickets.append(ticket)
    print("[INFO] Ticket logged successfully.\n")


# ================= 2. TECHNICIAN SHIFT REPORT =================
def shift_report():
    if not tickets:
        print("[INFO] No tickets logged yet.\n")
        return

    print("\n===== TECHNICIAN SHIFT REPORT =====")
    shifts = set((t["tech"], t["shift_date"]) for t in tickets)

    for tech, date in shifts:
        tech_tickets = [t for t in tickets if t["tech"] == tech and t["shift_date"] == date]
        print(f"\nTechnician: {tech.title()} | Date: {date}")
        
        status_counts = {}
        for t in tech_tickets:
            st = t["status"].title()
            status_counts[st] = status_counts.get(st, 0) + 1
            
        for status_name, count in status_counts.items():
            print(f"  {status_name}: {count}")
            
        print(f"Total Worked: {len(tech_tickets)}")


# ================= 3. PERFORMANCE GRAPH (VERY THIN BAR FIX) =================
def performance_graph():
    if not tickets:
        print("[INFO] No tickets logged yet to display on graph.\n")
        return

    techs = list(set(t["tech"].title() for t in tickets))
    
    closed_counts = []
    onsite_counts = []
    other_counts = []

    for tech in techs:
        t_lower = tech.lower().strip()
        closed = sum(1 for t in tickets if t["tech"].lower().strip() == t_lower and t["status"].lower().strip() == "closed")
        onsite = sum(1 for t in tickets if t["tech"].lower().strip() == t_lower and t["status"].lower().strip() == "onsite")
        other = sum(1 for t in tickets if t["tech"].lower().strip() == t_lower and t["status"].lower().strip() not in ["closed", "onsite"])
        
        closed_counts.append(closed)
        onsite_counts.append(onsite)
        other_counts.append(other)

    plt.figure(figsize=(7, 5))
    
    # Very small bar width to keep the column nice and thin
    bar_width = 0.08

    # Stacked bars: Closed (bottom), Onsite (middle), Other (top)
    plt.bar(techs, closed_counts, width=bar_width, color='#002060', label='Closed')
    plt.bar(techs, onsite_counts, width=bar_width, bottom=closed_counts, color='#0070C0', label='Onsite')
    
    bottom_other = [c + o for c, o in zip(closed_counts, onsite_counts)]
    plt.bar(techs, other_counts, width=bar_width, bottom=bottom_other, color='#8EA9DB', label='OnHold / Open / In Progress')

    plt.title("Technician Performance Breakdown", fontsize=12, fontweight='bold')
    plt.xlabel("Technicians", fontsize=10)
    plt.ylabel("Number of Tickets", fontsize=10)
    
    # Stops Matplotlib from stretching a single bar across the whole window
    if len(techs) == 1:
        plt.xlim(-0.5, 0.5)

    # Use whole numbers for Y-axis (0, 1, 2...)
    max_val = max([c + o + ot for c, o, ot in zip(closed_counts, onsite_counts, other_counts)] or [1])
    plt.yticks(range(0, max_val + 2))
    
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()


# ================= 4. EXPORT TO EXCEL =================
def export_excel():
    if not tickets:
        print("[INFO] No tickets to export.\n")
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "Ticket Report"

    ws.append(["Technician", "Store", "Type", "Status", "Shift Date", "Time Logged"])

    for t in tickets:
        ws.append([
            t["tech"].title(),
            t["store"],
            t["type"],
            t["status"].capitalize(),
            str(t["shift_date"]),
            str(t["time"].strftime("%Y-%m-%d %H:%M:%S"))
        ])

    wb.save("ticket_report.xlsx")
    print("[INFO] Excel report exported successfully as 'ticket_report.xlsx'\n")


# ================= 5. SLA ALERT =================
def sla_alert():
    now = datetime.now()
    print("\n===== SLA ALERTS (20+ Hours Open) =====")

    found = False
    for t in tickets:
        hours = (now - t["time"]).total_seconds() / 3600
        if hours >= 20 and t["status"] != "closed":
            print(f"[WARNING] Tech: {t['tech'].title()} | Store: {t['store']} | Type: {t['type']} | Open for {round(hours, 1)} hrs")
            found = True

    if not found:
        print("[INFO] No SLA breaches found.")

    print("[INFO] SLA check complete.\n")


# ================= MAIN MENU LOOP =================
while True:
    print("\n===== SMART IT TICKET SYSTEM =====")
    print("1. Add Ticket")
    print("2. Shift Report")
    print("3. View Performance Graph")
    print("4. Export to Excel")
    print("5. SLA Alerts")
    print("6. Exit")

    choice = input("Choose option (1-6): ").strip()

    if choice == "1":
        add_ticket()
    elif choice == "2":
        shift_report()
    elif choice == "3":
        performance_graph()
    elif choice == "4":
        export_excel()
    elif choice == "5":
        sla_alert()
    elif choice == "6":
        print("[INFO] System exiting. Goodbye!")
        break
    else:
        print("[ERROR] Invalid selection. Choose an option from 1 to 6.\n")