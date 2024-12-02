import random
from datetime import datetime
from fpdf import FPDF


def generate_payslip_pdf(employee_details, pdf):
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt=f"PAYSLIP FOR THE MONTH OF {employee_details['month'].upper()}, {employee_details['year']}",
             ln=True, align="C")
    pdf.ln(10)

    # Employee Details
    pdf.set_font("Arial", size=12)
    pdf.cell(100, 10, txt=f"Employee ID       : {employee_details['employee_id']}")
    pdf.ln(5)
    pdf.cell(100, 10, txt=f"Employee Name     : {employee_details['employee_name']}")
    pdf.ln(5)
    pdf.cell(100, 10, txt=f"Designation       : {employee_details['designation']}")
    pdf.ln(5)
    pdf.cell(100, 10, txt=f"Department        : {employee_details['department']}")
    pdf.ln(5)
    pdf.cell(100, 10, txt=f"Payment Method    : {employee_details['payment_method']}")
    pdf.ln(10)

    # Salary Breakdown
    pdf.cell(100, 10, txt=f"Gross Salary      : {employee_details['gross_salary']} BDT")
    pdf.ln(5)
    pdf.cell(100, 10, txt=f"Total Working Days: {employee_details['total_working_days']}")
    pdf.ln(5)
    pdf.cell(100, 10, txt=f"Weekends          : {', '.join(employee_details['weekends'])}")
    pdf.ln(5)
    pdf.cell(100, 10, txt=f"Holidays          : {', '.join(employee_details['holidays'])}")
    pdf.ln(5)
    pdf.cell(100, 10, txt=f"Leaves Taken      : {employee_details['leaves']}")
    pdf.ln(5)
    pdf.cell(100, 10, txt=f"LOP Days          : {employee_details['lop_days']}")
    pdf.ln(5)
    pdf.cell(100, 10, txt=f"Paid Days         : {employee_details['paid_days']}")
    pdf.ln(10)

    # Final Payment
    pdf.cell(100, 10, txt=f"Net Salary        : {employee_details['net_salary']} BDT")
    pdf.ln(5)
    pdf.cell(100, 10, txt=f"Bonus             : {employee_details['bonus']} BDT")
    pdf.ln(5)
    pdf.cell(100, 10, txt=f"Total Payment     : {employee_details['total_payment']} BDT")
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
    gross_salary = 10000  # Updated gross salary to 10,000 BDT
    payment_method = "Cash"
    weekends = ["Friday"]  # Typical weekends in Bangladesh

    # Define holidays and Eid vacation for relevant months
    holiday_data = {
        9: ["1st September", "21st September"],  # Eid-ul-Adha in September
        10: [],  # No major holidays
        11: ["16th November"],  # Language Movement Day
        12: ["25th December"],  # Christmas
        1: [],  # No major holidays
        2: ["21st February"],  # International Mother Language Day
        3: ["26th March"],  # Independence Day
    }

    for month in range(9, 4, -1):
        holidays = holiday_data.get(month, [])
        employee_details = calculate_monthly_payslip(month, 2014, gross_salary, weekends, holidays, payment_method)
        generate_payslip_pdf(employee_details, pdf)


if __name__ == '__main__':
    # Create a PDF document
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Generate payslips for September 2014 to March 2015
    generate_payslips_for_period(pdf)

    # Save the PDF to a file
    pdf.output("salary_slip/payslips_sep_2014_to_mar_2015.pdf")
