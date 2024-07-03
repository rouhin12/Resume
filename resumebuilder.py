from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, 'Rouhin Gandhi - Resume', 0, 1, 'C')

    def section_title(self, title):
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def section_body(self, body):
        self.set_font('Times', '', 12)
        self.multi_cell(0, 10, body)
        self.ln(5)

    def add_section(self, title, body):
        self.section_title(title)
        self.section_body(body)

pdf = PDF()
pdf.set_left_margin(10)
pdf.set_right_margin(10)
pdf.add_page()

# Header with contact information
pdf.set_font('Times', 'B', 16)
pdf.cell(0, 10, 'ROUHIN GANDHI', 0, 1, 'C')
pdf.set_font('Times', '', 12)
pdf.cell(0, 10, 'Birth Date: 19/09/2004', 0, 1, 'C')
pdf.cell(0, 10, 'Phone: +91 9967350001', 0, 1, 'C')
pdf.cell(0, 10, 'Email: rouhingandhi123@gmail.com', 0, 1, 'C')
pdf.cell(0, 10, 'LinkedIn: linkedin.com/in/rouhin', 0, 1, 'C')
pdf.ln(10)

# Adding sections without new pages
pdf.add_section('Education', 
"""SVKM's NMIMS Mukesh Patel School of Technology Management & Engineering
Bachelor of Technology (BTech), Computer Engineering (2022 - 2026)
- Relevant Coursework: [List relevant courses if available]

Utpal Shanghvi School
IGCSE, Science (January 2007 - June 2020)""")

pdf.add_section('Experience', 
"""Indian Institute of Technology, Bombay
Geospatial and Software Intern
May 2024 - Present | Mumbai, Maharashtra, India
- Working with the GISE Hub team on innovative projects involving the analysis and application of geospatial data.
- Enhancing expertise in geospatial and software development through hands-on projects.

Freightwalla
Sales and Strategy Intern
June 2022 - August 2022 | Mumbai, Maharashtra, India
- Supported sales team with administrative assistance and coordinated paperwork.
- Gained insights into best practices and strategies for maximizing sales revenue.
- Assisted in maintaining customer relationships through follow-up calls.
- Managed customer expectations and supported client acquisition strategies.""")

pdf.add_section('Volunteer Work', 
"""Rotaract Club of Western Suburbs
Joint Secretary
June 2023 - June 2024 | Mumbai, Maharashtra, India

Rotaract Club of Bombay West
Partners In Services Director
May 2022 - January 2023 | Mumbai, Maharashtra, India""")

pdf.add_section('Skills', 
"""Programming Languages:
- C++
- Python
- R
- Java
- HTML, JavaScript, AngularJS, NodeJS
- SQL
- Django

Top Skills:
- Software as a Service (SaaS)
- SaaS Sales
- Strategy
- Software Devlopment""")

pdf.add_section('Extracurricular Activities', 
"""Head of R&D, Tark
- Founded and led a successful college-wide debating society, showcasing leadership and communication skills.

Core Council, LAIMUN Society
- Extended an international MUN society's roots to India and now serve in the capacity of core council.

Hackathons
- Participated in multiple hackathons and secured runners-up position in the same.

Model United Nations (MUNs)
- Avid MUNner, delegated in over 40 MUNs and chaired over 15 MUNs pan India, with recognition from multiple organizations.""")

# Save the PDF to a specified path
output_path = "/home/rouhin/resume builder/Rouhin_Gandhi_Resume_Formatted.pdf"
pdf.output(output_path)

output_path
