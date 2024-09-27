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
pdf.cell(0, 10, 'Email: rouhingandhi123@gmail.com | LinkedIn: linkedin.com/in/rouhin', 0, 1, 'C')
pdf.cell(0, 10, 'Github: github.com/rouhin12', 0, 1, 'C')
pdf.ln(10)

# Sections
pdf.add_section('Education', 
    "SVKM's NMIMS Mukesh Patel School of Technology Management & Engineering\n"
    "BTech, Computer Engineering (2022 - 2026)\n"
    "- Relevant Coursework: Algorithms, Data Structures, Web Development, Databases, AI")

pdf.add_section('Experience', 
    "GISE Hub, IIT-Bombay\nGeospatial and Software Intern (May 2024 - July 2024)\n"
    "- Developed geospatial data analysis tools using Python, enhancing spatial visualization.\n"
    "- Worked on GIS applications for real-time data, improving accuracy in data insights.\n"
    "- Contributed to Python-based automation for large-scale data processing.\n\n"
    "Freightwalla\nSales and Strategy Intern (June 2022 - Aug 2022)\n"
    "- Assisted in sales strategies and market research, helping optimize client acquisition.\n"
    "- Managed administrative tasks, enhancing team efficiency and client onboarding process.")

pdf.add_section('Projects', 
    "Bladder Filling Prediction during Radiotherapy using GANs (Sep 2024 - Present)\n"
    "- Collaborating on AI research to predict bladder volume changes in cervical cancer radiotherapy patients.\n"
    "- Pre-processed medical imaging data and trained models for accurate volume predictions.\n"
    "- Developed AI models to assist radiation oncologists in minimizing side effects.\n\n"
    "Web-based GIS Platform (2023)\n"
    "- Built an interactive GIS platform using Leaflet.js for real-time spatial queries.\n"
    "- Integrated geolocation features and dynamic data layers to enhance user experience.")

pdf.add_section('Volunteer Work', 
    "Rotaract Club of Western Suburbs, Joint Secretary (2023 - 2024)\n"
    "- Managed club operations, coordinated events, and expanded member outreach.\n\n"
    "Rotaract Club of Bombay West, Partners In Services Director (2022 - 2023)\n"
    "- Led community service projects, liaised with partners for successful project execution.")

pdf.add_section('Skills', 
    "Programming Languages: C++, Python, Java, HTML, JavaScript, SQL, Django\n"
    "Technical Skills: GIS, Web Development, Data Analysis, Machine Learning\n"
    "Soft Skills: Leadership, Teamwork, Communication, Strategy")

pdf.add_section('Extracurricular Activities', 
    "Head of R&D, Tark\n"
    "- Founded and led a debating society, organizing college-wide debate tournaments.\n\n"
    "Core Council, LAIMUN Society\n"
    "- Helped establish and run an international MUN society, expanding its presence in India.\n\n"
    "Hackathons\n"
    "- Participated in multiple hackathons, securing top positions and building innovative solutions.")

# Save the PDF
output_path = "E:\\Rouhin Projects\\Resume\\Rouhin_Gandhi_Resume.pdf"
pdf.output(output_path)

output_path
