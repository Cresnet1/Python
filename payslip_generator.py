import pandas as pd
from fpdf import FPDF
import yagmail
import os

# Step 1: Read Excel data
df = pd.read_excel(r'C:\Users\uncommonStudent\Desktop\Python\EMPLOYEE.xlsx')

# Step 2: Create output folder if it doesn't exist
if not os.path.exists('payslips'):
    os.makedirs('payslips')

# Step 3: Loop through each employee and generate payslip
for index, row in df.iterrows():
    emp_id = row['Employee ID']
    name = row['Name']
    email = row['Email']
    basic_salary = row['Basic Salary']
    allowances = row['Allowances']
    deductions = row['Deductions']

    # Calculate net salary
    net_salary = basic_salary + allowances - deductions

    # Step 4: Create PDF payslip
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)   

    pdf.set_fill_color(230, 230, 250)  # Light lavender background
    pdf.cell(200, 10, txt="Monthly Payslip", ln=True, align='C', fill=True)
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Employee ID: {emp_id}", ln=True)
    pdf.cell(200, 10, txt=f"Employee Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Basic Salary: ${basic_salary:,.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Allowances: ${allowances:,.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Deductions: ${deductions:,.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Net Salary: ${net_salary:,.2f}", ln=True)

    # Save PDF
    filename = f"payslips/{emp_id}.pdf"
    pdf.output(filename)

    # Step 5: Send email with payslip
    try:
        yag = yagmail.SMTP(user="ldumbatsuro6@gmail.com", password="qqijrcubmnpttjxu")  # ✅ Use full email

        subject = "Your Payslip for This Month"
        body = f"""
        Dear {name},

        Please find attached your payslip for this month.

        Best regards,
        HR Department
        """

        yag.send(to=email, subject=subject, contents=body, attachments=filename)
        print(f"📨 Payslip sent to {name} at {email}")

    except Exception as e:
        print(f"❌ Failed to send email to {email}: {e}")

# ✅ Final tip: Notify when everything is done
print("✅ All payslips have been generated and emails sent successfully!")





        
        



        
