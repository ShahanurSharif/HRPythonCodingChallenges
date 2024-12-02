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

    # Salary Breakdown (Horizontal)
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

    # Final Payment details (Net Salary, Bonus, Total Payment)
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
    gross_salary = 52000  # Updated Gross Salary to 52,000 BDT
    payment_method = "Cash"
    weekends = ["Friday"]  # Typical weekends in Bangladesh

    # Define holidays accurately for the relevant months
    holiday_data = {
        7: ["15/07/2019", "16/07/2019"],  # Eid-ul-Fitr (July)
        8: ["12/08/2019", "13/08/2019", "14/08/2019", "15/08/2019"],  # Eid-ul-Adha (August)
        9: ["24/05/2020", "25/05/2020", "26/05/2020"],  # Eid-ul-Fitr (May)
        10: ["01/08/2020", "02/08/2020", "03/08/2020", "04/08/2020"],  # Eid-ul-Adha (August)
        11: [],  # No holidays
        12: [],  # No holidays
        1: [],  # No holidays
        2: [],  # No holidays
        3: [],  # No holidays
        4: [],  # No holidays
        5: [],  # No holidays
        6: [],  # No holidays
    }

    total_salary = 0  # Variable to store total salary

    # List to store generated payslips
    payslips = []

    for month in range(7, 13):  # Generating payslips for Jul 2019 to Dec 2019
        holidays = holiday_data.get(month, [])
        employee_details = calculate_monthly_payslip(month, 2019, gross_salary, weekends, holidays, payment_method)
        payslips.append(employee_details)

        # Generate PDF for this month
        generate_payslip_pdf(employee_details, pdf)
        total_salary += employee_details['total_payment']

    # Generate payslips for the first half of 2020
    for month in range(1, 7):  # Generating payslips for Jan 2020 to Jun 2020
        holidays = holiday_data.get(month, [])
        employee_details = calculate_monthly_payslip(month, 2020, gross_salary, weekends, holidays, payment_method)
        payslips.append(employee_details)

        # Generate PDF for this month
        generate_payslip_pdf(employee_details, pdf)
        total_salary += employee_details['total_payment']

    # After generating all payslips, save the PDF
    pdf_output_file = "salary_slip/salary_slip_jan_to_dec_2019_2020.pdf"
    pdf.output(pdf_output_file)

    print(f"Total salary for all employees: {total_salary}")


if __name__ == "__main__":
    pdf = FPDF()
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)

    generate_payslips_for_period(pdf)
