import random
import os
from datetime import datetime
from fpdf import FPDF

# Ensure directory exists
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

    # Employee Details Section
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, "Employee ID", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(40, 10, employee_details['employee_id'], ln=True)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, "Employee Name", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(40, 10, employee_details['employee_name'], ln=True)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, "Designation", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, employee_details['designation'])

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, "Department", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(40, 10, employee_details['department'], ln=True)

    pdf.ln(10)  # Add space after employee details

    # Table headers for salary breakdown
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, "Gross Salary", border=1, align="C")
    pdf.cell(40, 10, "Total Working Days", border=1, align="C")
    pdf.cell(40, 10, "Leaves Taken", border=1, align="C")
    pdf.cell(40, 10, "LOP Days", border=1, align="C")
    pdf.cell(40, 10, "Paid Days", border=1, align="C")
    pdf.ln()

    # Salary Breakdown
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
    eid_bonus = gross_salary if month == 7 else 0  # Eid-ul-Fitr bonus for July 2014

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
    gross_salary = 12000  # In BDT (Updated Gross Salary)
    payment_method = "Cash"
    weekends = ["Friday"]  # Typical weekends in Bangladesh

    # Define holidays and Eid vacation for relevant months
    holiday_data = {
        9: ["15th September"],  # National Mourning Day
        10: [],  # No major holidays
        11: [],  # No major holidays
        12: ["25th December"],  # Christmas
        1: [],  # No major holidays
        2: [],  # No major holidays
        3: ["17th March"],  # National Poet's Day
    }

    for month in range(4, 13):  # Generating payslips for April 2015 to April 2016
        holidays = holiday_data.get(month, [])
        employee_details = calculate_monthly_payslip(month, 2015, gross_salary, weekends, holidays, payment_method)
        generate_payslip_pdf(employee_details, pdf)

    for month in range(1, 5):  # Generating payslips for January to April 2016
        holidays = holiday_data.get(month, [])
        employee_details = calculate_monthly_payslip(month, 2016, gross_salary, weekends, holidays, payment_method)
        generate_payslip_pdf(employee_details, pdf)


if __name__ == '__main__':
    # Create a PDF document
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Generate payslips for April 2015 to April 2016
    generate_payslips_for_period(pdf)

    # Save the PDF to a file in the "salary_slip" directory
    pdf.output("salary_slip/payslips_apr_2015_to_apr_2016.pdf")
