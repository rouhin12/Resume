from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, 'Rouhin Gandhi - Resume', 0, 1, 'C')

    def add_section(self, title, body):
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)
        self.set_font('Times', '', 12)
        self.multi_cell(0, 10, body)
        self.ln(5)

pdf = PDF()
pdf.set_margins(10, 10, 10)
pdf.add_page()

# Header
pdf.set_font('Times', 'B', 16)
pdf.cell(0, 10, 'ROUHIN GANDHI', 0, 1, 'C')
pdf.set_font('Times', '', 12)
pdf.cell(0, 10, 'Birth Date: 19/09/2004 | Phone: +91 9967350001', 0, 1, 'C')
pdf.cell(0, 10, 'Email: rouhingandhi123@gmail.com | LinkedIn: https://linkedin.com/in/rouhin', 0, 1, 'C')
pdf.cell(0, 10, 'Github: https://github.com/rouhin12', 0, 1, 'C')
pdf.ln(10)

# Sections
pdf.add_section('Education', 
    "SVKM's NMIMS Mukesh Patel School of Technology Management & Engineering\n"
    "BTech, Computer Engineering (2022 - 2026)\n"
    "- Relevant Coursework: Algorithms, Data Structures, Web Development")

pdf.add_section('Experience', 
    "GISE Hub, IIT-Bombay\nGeospatial and Software Intern (May 2024 - July 2024)\n"
    "- Developed innovative GIS tools and applications using Python and Django, improving user accessibility.\n"
    "- Enhanced real-time geospatial data analysis, enabling quicker decision-making for ongoing projects.\n"
    "- Collaborated with multidisciplinary teams to integrate data visualization techniques, enhancing project presentations.\n\n"
    "Freightwalla\nSales and Strategy Intern (June 2022 - Aug 2022)\n"
    "- Supported the sales team by conducting market research to identify potential clients and industry trends.\n"
    "- Managed client acquisition processes, ensuring smooth onboarding and satisfaction.\n"
    "- Streamlined administrative tasks, improving team efficiency and coordination in project delivery.\n\n")

pdf.add_section('Projects', 
    "Bladder Filling Prediction in Radiotherapy using GANs (Sep 2024 - Present)\n"
    "- Collaborating on an AI-driven research project to predict bladder volume changes during radiotherapy.\n"
    "- Preprocessing medical imaging data for GAN training, ensuring high-quality input for model accuracy.\n"
    "- Developing and fine-tuning predictive models to assist radiation oncologists in minimizing side effects and optimizing treatment plans.")
pdf.add_section('Volunteer Work', 
    "Rotaract Club of Western Suburbs, Joint Secretary (2023 - 2024)\n"
    "Rotaract Club of Bombay West, Partners In Services Director (2022 - 2023)")

pdf.add_section('Skills', 
    "Programming: C++, Python, JavaScript, SQL, Django\n"
    "Top Skills: SaaS, Strategy, Software Development")

pdf.add_section('Extracurricular Activities', 
    "Head of R&D, Tark\n"
    "- Founded and led a college debating society, organizing workshops and competitions.\n\n"
    "Core Council, LAIMUN Society\n"
    "- Helped establish and run an international MUN society, expanding its presence in India.\n\n"
    "Hackathons\n"
    "- Participated in multiple hackathons, securing top positions and building innovative solutions.")

# Save the PDF
output_path = "E:\\Rouhin Projects\\Resume\\Rouhin_Gandhi_Resume.pdf"
pdf.output(output_path)

output_path
