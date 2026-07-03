import matplotlib.pyplot as plt
from openpyxl import Workbook
from datetime import datetime

tickets = []

# ================= ADD TICKET =================
def add_ticket():
    tech = input("Technician name: ").lower()
    store = input("Store name: ")
    ttype = input("Type (KDS / DayEnd / Online / MX): ")
    status = input("Status (Closed / OnHold / Onsite / Open): ").lower()

    ticket = {
        "tech": tech,
        "store": store,
        "type": ttype,
        "status": status,
        "time": datetime.now(),
        "shift_date": datetime.now().date()
    }

    tickets.append(ticket)
    print("✅ Ticket logged.\n")


# ================= TECHNICIAN SHIFT REPORT =================
def shift_report():
    if not tickets:
        print("No tickets logged yet.\n")
        return

    print("\n===== TECHNICIAN SHIFT REPORT =====")

    shifts = set((t["tech"], t["shift_date"]) for t in tickets)

    for tech, date in shifts:
        closed = sum(1 for t in tickets if t["tech"] == tech and t["shift_date"] == date and t["status"] == "closed")
        onhold = sum(1 for t in tickets if t["tech"] == tech and t["shift_date"] == date and t["status"] == "onhold")
        onsite = sum(1 for t in tickets if t["tech"] == tech and t["shift_date"] == date and t["status"] == "onsite")

        total = closed + onhold + onsite

        print(f"\nTechnician: {tech.title()} | Date: {date}")
        print("Closed:", closed)
        print("OnHold:", onhold)
        print("Onsite:", onsite)
        print("Total Worked:", total)


# ================= GRAPH PER TECH =================
def tech_graph():
    tech_name = input("Enter technician name: ").lower()

    closed = sum(1 for t in tickets if t["tech"] == tech_name and t["status"] == "closed")
    onhold = sum(1 for t in tickets if t["tech"] == tech_name and t["status"] == "onhold")
    onsite = sum(1 for t in tickets if t["tech"] == tech_name and t["status"] == "onsite")

    plt.figure()
    plt.bar(["Closed", "OnHold", "Onsite"], [closed, onhold, onsite])
    plt.title(f"{tech_name.title()} Performance")
    plt.ylabel("Tickets Worked")
    plt.show()


# ================= GRAPH PER SHIFT =================
def shift_graph():
    if not tickets:
        print("No tickets logged.\n")
        return

    tech_name = input("Enter technician name: ").lower()

    shifts = set(t["shift_date"] for t in tickets if t["tech"] == tech_name)

    for date in shifts:
        closed = sum(1 for t in tickets if t["tech"] == tech_name and t["shift_date"] == date and t["status"] == "closed")
        onhold = sum(1 for t in tickets if t["tech"] == tech_name and t["shift_date"] == date and t["status"] == "onhold")
        onsite = sum(1 for t in tickets if t["tech"] == tech_name and t["shift_date"] == date and t["status"] == "onsite")

        plt.figure()
        plt.bar(["Closed", "OnHold", "Onsite"], [closed, onhold, onsite])
        plt.title(f"{tech_name.title()} Shift {date}")
        plt.ylabel("Tickets Worked")
        plt.show()


# ================= GRAPH ALL TECH =================
def all_tech_graph():
    techs = set(t["tech"] for t in tickets)

    names = []
    totals = []

    for tech in techs:
        total = sum(1 for t in tickets if t["tech"] == tech)
        names.append(tech.title())
        totals.append(total)

    plt.figure()
    plt.bar(names, totals)
    plt.title("All Technicians Performance")
    plt.xticks(rotation=45)
    plt.ylabel("Total Tickets Worked")
    plt.show()


# ================= EXPORT TO EXCEL =================
def export_excel():
    if not tickets:
        print("No tickets to export.\n")
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "Ticket Report"

    ws.append(["Technician", "Store", "Type", "Status", "Shift Date", "Time"])

    for t in tickets:
        ws.append([
            t["tech"],
            t["store"],
            t["type"],
            t["status"],
            str(t["shift_date"]),
            str(t["time"])
        ])

    wb.save("ticket_report.xlsx")
    print("📁 Excel report saved as ticket_report.xlsx\n")


# ================= SLA ALERT =================
def sla_alert():
    now = datetime.now()
    print("\n===== SLA ALERTS (24+ Hours Open) =====")

    for t in tickets:
        hours = (now - t["time"]).total_seconds() / 3600
        if hours >= 24 and t["status"] != "closed":
            print(f"⚠ {t['tech']} | {t['store']} | {t['type']} | {round(hours,1)} hrs open")

    print("Done.\n")


# ================= MENU =================
while True:
    print("\n===== SMART IT TICKET SYSTEM =====")
    print("1 Add Ticket")
    print("2 Technician Shift Report")
    print("3 Technician Graph")
    print("4 Graph Per Shift")
    print("5 Graph All Technicians")
    print("6 Export to Excel")
    print("7 SLA Alerts")
    print("8 Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_ticket()
    elif choice == "2":
        shift_report()
    elif choice == "3":
        tech_graph()
    elif choice == "4":
        shift_graph()
    elif choice == "5":
        all_tech_graph()
    elif choice == "6":
        export_excel()
    elif choice == "7":
        sla_alert()
    elif choice == "8":
        print("Goodbye 👋")
        break
    else:
        print("Invalid option.\n")