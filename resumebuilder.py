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
    "- Relevant Coursework: Algorithms, Data Structures, Web Development, Financial Institutes Markets instruments and systems, Accounting")

pdf.add_section('Experience', 
    "GISE Hub, IIT-Bombay\nGeospatial and Software Intern (May 2024 - July 2024)\n"
    "- Developed innovative GIS tools and applications using Python and Django, improving user accessibility.\n"
    "- Enhanced real-time geospatial data analysis, enabling quicker decision-making for ongoing projects.\n"
    "- Collaborated with multidisciplinary teams to integrate data visualization techniques, enhancing project presentations.\n\n"
    "Freightwalla\nSales and Strategy Intern (June 2022 - Aug 2022)\n"
    "- Supported the sales team by conducting market research to identify potential clients and industry trends.\n"
    "- Managed client acquisition processes, ensuring smooth onboarding and satisfaction.\n"
    "- Streamlined administrative tasks, improving team efficiency and coordination in project delivery.\n\n")

# Projects section with detailed descriptions
pdf.add_section('Projects', 
"""1. Scalable and Automated Waterbody Analysis through Multi-Index Satellite Imagery on Google Earth Engine 
   Co-authored a research project aimed at extracting and quantifying water bodies over time using the Normalized Difference Water Index (NDWI), NDVI, and NBR, applied to Sentinel-2 satellite data. The project included cloud masking, edge detection, and entropy-based texture analysis to assess water heterogeneity. This methodology was tested over Bhandara District, India (2017-2024), demonstrating how cloud-based platforms like Google Earth Engine can facilitate large-scale, high-frequency environmental monitoring.
   
2. Bladder Filling from Initiation to Completion of Radiotherapy in Women with Cervical Cancer using GANs (Ongoing)
   Led a research project focused on predicting bladder volume changes during cervical cancer radiotherapy. Utilized Generative Adversarial Networks (GANs) to simulate and analyze bladder filling dynamics, aiming to improve patient preparation and treatment planning. This project required a deep understanding of AI model development and medical imaging processing, showcasing the intersection of machine learning and healthcare technology.
3. Predict the relation of bond prices with the Foreign institutional investment in the Indian market (Ongoing)
   Developed a project to predict the relationship between bond prices and Foreign Institutional Investment (FII) in the Indian market. Utilized quantitative techniques and statistical analysis to identify patterns and correlations between bond prices and FII, providing insights for investment strategies and risk management. This project required a deep understanding of financial markets and data analysis, showcasing the intersection of quantitative finance and investment research.""")
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
