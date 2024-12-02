import random
import os
from datetime import datetime
from fpdf import FPDF

# Ensure the directory exists
if not os.path.exists('salary_slip'):
    os.makedirs('salary_slip')


def generate_payslip_pdf(employee_details, pdf):
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt=f"PAYSLIP FOR THE MONTH OF {employee_details['month'].upper()} {employee_details['year']}",
             ln=True, align="C")
    pdf.ln(10)

    # Employee Details Section (Formatted with ":")
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(50, 10, "Employee ID:", ln=False)
    pdf.set_font("Arial", size=12)
    pdf.cell(50, 10, employee_details['employee_id'], ln=True)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(50, 10, "Employee Name:", ln=False)
    pdf.set_font("Arial", size=12)
    pdf.cell(50, 10, employee_details['employee_name'], ln=True)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(50, 10, "Designation:", ln=False)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, employee_details['designation'])

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(50, 10, "Department:", ln=False)
    pdf.set_font("Arial", size=12)
    pdf.cell(50, 10, employee_details['department'], ln=True)

    pdf.ln(10)  # Add space after employee details

    # Salary Details Section (Horizontal table format)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, "Gross Salary", border=1, align="C")
    pdf.cell(40, 10, "Total Working Days", border=1, align="C")
    pdf.cell(40, 10, "Leaves Taken", border=1, align="C")
    pdf.cell(40, 10, "LOP Days", border=1, align="C")
    pdf.cell(40, 10, "Paid Days", border=1, align="C")
    pdf.ln()

    # Salary Breakdown (Horizontal)
    pdf.set_font("Arial", size=12)
    pdf.cell(40, 10, f"{employee_details['gross_salary']} BDT", border=1, align="C")
    pdf.cell(40, 10, str(employee_details['total_working_days']), border=1, align="C")
    pdf.cell(40, 10, str(employee_details['leaves']), border=1, align="C")
    pdf.cell(40, 10, str(employee_details['lop_days']), border=1, align="C")
    pdf.cell(40, 10, str(employee_details['paid_days']), border=1, align="C")
    pdf.ln()

    # Final Payment details
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, "Net Salary", border=1, align="C")
    pdf.cell(40, 10, "Bonus", border=1, align="C")
    pdf.cell(40, 10, "Total Payment", border=1, align="C")
    pdf.ln()

    # Final Payment values
    pdf.set_font("Arial", size=12)
    pdf.cell(40, 10, f"{employee_details['net_salary']} BDT", border=1, align="C")
    pdf.cell(40, 10, f"{employee_details['bonus']} BDT", border=1, align="C")
    pdf.cell(40, 10, f"{employee_details['total_payment']} BDT", border=1, align="C")
    pdf.ln(10)

    # Separator line
    pdf.cell(200, 0, ln=True, align='C')
    pdf.cell(200, 10, ln=True, align='C')


def calculate_monthly_payslip(month, year, gross_salary, weekends, holidays, payment_method):
    total_working_days = 30 if month in [4, 6, 9, 11] else 31  # Approximation for simplicity
    if month == 2:
        total_working_days = 28 if year % 4 != 0 else 29  # February handling

    leaves = random.randint(0, 3)
    lop_days = random.randint(0, 2)
    eid_bonus = gross_salary if month in [7, 9] else 0  # Eid-ul-Fitr bonus for July and Eid-ul-Adha bonus for September

    paid_days = total_working_days - len(holidays) - lop_days
    daily_salary = gross_salary / total_working_days
    net_salary = round(daily_salary * paid_days, 2)
    total_payment = net_salary + eid_bonus

    employee_details = {
        "employee_id": "1001",
        "employee_name": "Shahanur Md Sharif",
        "designation": "Founder & Lead Full Stack Developer",
        "department": "Web & Software Development",
        "gross_salary": gross_salary,
        "total_working_days": total_working_days,
        "weekends": weekends,
        "holidays": holidays,
        "leaves": leaves,
        "lop_days": lop_days,
        "paid_days": paid_days,
        "net_salary": net_salary,
        "bonus": eid_bonus,
        "total_payment": total_payment,
        "payment_method": payment_method,
        "month": datetime(year, month, 1).strftime('%B'),
        "year": year
    }

    return employee_details


def generate_payslips_for_period(pdf):
    gross_salary = 30000  # Updated Gross Salary to 30,000 BDT
    payment_method = "Cash"
    weekends = ["Friday"]  # Typical weekends in Bangladesh

    # Define holidays and Eid vacation for relevant months
    holiday_data = {
        1: ["01/01/2017"],  # New Year's Day (January 1)
        3: ["26/03/2017"],  # Independence Day (March 26)
        5: ["01/05/2017"],  # Labor Day (May 1)
        7: ["06/07/2017", "07/07/2017", "08/07/2017"],  # Eid-ul-Fitr (July)
        8: [],  # No holidays
        9: ["01/09/2017", "02/09/2017", "03/09/2017"],  # Eid-ul-Adha (September)
        10: [],  # No holidays
        11: [],  # No holidays
        12: ["16/12/2017"],  # Victory Day (December 16)
    }

    for month in range(11, 13):  # Generating payslips for Nov 2016 - Dec 2017
        holidays = holiday_data.get(month, [])
        employee_details = calculate_monthly_payslip(month, 2016, gross_salary, weekends, holidays, payment_method)
        generate_payslip_pdf(employee_details, pdf)

    for month in range(1, 13):  # For 2017 from Jan to Dec
        holidays = holiday_data.get(month, [])
        employee_details = calculate_monthly_payslip(month, 2017, gross_salary, weekends, holidays, payment_method)
        generate_payslip_pdf(employee_details, pdf)


if __name__ == '__main__':
    # Create a PDF document
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Generate payslips for Nov 2016 to Dec 2017
    generate_payslips_for_period(pdf)

    # Save the PDF to a file in the "salary_slip" directory
    pdf.output("salary_slip/payslips_nov_2016_to_dec_2017.pdf")
