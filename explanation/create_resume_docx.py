import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml

doc = docx.Document()

# Set standard margins (0.45 inch top/bottom, 0.5 inch left/right for tight 1-page fit)
sections = doc.sections
for section in sections:
    section.top_margin = Inches(0.45)
    section.bottom_margin = Inches(0.45)
    section.left_margin = Inches(0.55)
    section.right_margin = Inches(0.55)

# Color Palette
DARK_NAVY = RGBColor(16, 44, 87)
CHARCOAL = RGBColor(35, 35, 35)
SLATE_GRAY = RGBColor(85, 85, 85)

def add_header(doc):
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(1)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_name = title_p.add_run('AUCHITYA SINGH')
    run_name.font.name = 'Calibri'
    run_name.font.size = Pt(18)
    run_name.font.bold = True
    run_name.font.color.rgb = DARK_NAVY

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(3)
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = sub_p.add_run('Data Analyst & Analytics Engineer (AI-Augmented)')
    run_sub.font.name = 'Calibri'
    run_sub.font.size = Pt(11)
    run_sub.font.bold = True
    run_sub.font.color.rgb = CHARCOAL

    contact_p = doc.add_paragraph()
    contact_p.paragraph_format.space_before = Pt(0)
    contact_p.paragraph_format.space_after = Pt(6)
    contact_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_c = contact_p.add_run('Uttar Pradesh, India  |  +91-7982754566  |  auchityasingh86@gmail.com  |  www.auchityasingh.site\nlinkedin.com/in/auchitya-singh-7b42502a5  |  github.com/CosmicAuchitya')
    run_c.font.name = 'Calibri'
    run_c.font.size = Pt(9.5)
    run_c.font.color.rgb = SLATE_GRAY

def add_section_title(doc, title_text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(5)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(title_text.upper())
    run.font.name = 'Calibri'
    run.font.size = Pt(10.5)
    run.font.bold = True
    run.font.color.rgb = DARK_NAVY
    
    # Bottom accent rule via XML
    pPr = p._p.get_or_add_pPr()
    border_xml = '<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:bottom w:val="single" w:sz="6" w:space="1" w:color="102C57"/></w:pBdr>'
    pPr.append(parse_xml(border_xml))

def add_bullet(doc, bold_prefix, text):
    bp = doc.add_paragraph(style='List Bullet')
    bp.paragraph_format.space_before = Pt(1)
    bp.paragraph_format.space_after = Pt(1.5)
    bp.paragraph_format.line_spacing = 1.05
    run_b = bp.add_run(bold_prefix + ' ')
    run_b.font.name = 'Calibri'
    run_b.font.size = Pt(9)
    run_b.font.bold = True
    run_b.font.color.rgb = CHARCOAL
    run_t = bp.add_run(text)
    run_t.font.name = 'Calibri'
    run_t.font.size = Pt(9)
    run_t.font.color.rgb = CHARCOAL

# Assemble Document
add_header(doc)

# 1. Summary
add_section_title(doc, 'Professional Summary')
sum_p = doc.add_paragraph()
sum_p.paragraph_format.space_before = Pt(2)
sum_p.paragraph_format.space_after = Pt(3)
sum_p.paragraph_format.line_spacing = 1.05
r1 = sum_p.add_run('Analytical, detail-driven Data Analyst & Analytics Engineer with proven experience delivering production data pipelines, executive dashboards (Power BI, DAX, Star Schema), and SQL analytics. ')
r1.font.name = 'Calibri'; r1.font.size = Pt(9); r1.font.color.rgb = CHARCOAL
r2 = sum_p.add_run('Pioneers an AI-augmented engineering methodology, ')
r2.font.name = 'Calibri'; r2.font.size = Pt(9); r2.font.bold = True; r2.font.color.rgb = DARK_NAVY
r3 = sum_p.add_run('pairing critical business acumen, hypothesis formulation, and forensic data validation with autonomous AI pair-programming agents for accelerated implementation, rapid iteration, and production deployment. Proven track record deriving actionable commercial insights and quantifying operational savings across 518K+ flight records, SaaS funnels, and climate time-series.')
r3.font.name = 'Calibri'; r3.font.size = Pt(9); r3.font.color.rgb = CHARCOAL

# 2. Technical Skills
add_section_title(doc, 'Technical Skills')
skills_data = [
    ('Business Intelligence:', 'Microsoft Power BI Desktop, DAX, Star Schema Modeling, Custom WebGL Visuals (Three.js), Tableau Data Marts, Executive Dashboards.'),
    ('Data Engineering & SQL:', 'Python (Pandas, NumPy), In-Memory DuckDB (ANSI SQL, CTEs, Window Functions), Columnar Parquet, Web Scraping (BeautifulSoup), Entity Resolution.'),
    ('Statistical Analysis & ML:', 'Scikit-Learn (HistGradientBoosting, Decision Trees, SGD Classifier, ColumnTransformer), Hypothesis Testing (Welch\'s t-Test), Feature Importance (Gini), Time-Series (Prophet).'),
    ('AI-Augmented Workflow:', 'Autonomous AI Pair-Programming Agents, Prompt Architecture for Code Refactoring, Automated Forensic Code Review, Accelerated Testing.'),
    ('Cloud & Platforms:', 'AWS (S3, Athena, SageMaker), Git/GitHub, Streamlit, Jupyter Notebooks.')
]
for cat, desc in skills_data:
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0.5)
    sp.paragraph_format.space_after = Pt(0.5)
    r_cat = sp.add_run(cat + ' ')
    r_cat.font.name = 'Calibri'; r_cat.font.size = Pt(9); r_cat.font.bold = True; r_cat.font.color.rgb = CHARCOAL
    r_desc = sp.add_run(desc)
    r_desc.font.name = 'Calibri'; r_desc.font.size = Pt(9); r_desc.font.color.rgb = CHARCOAL

# 3. Featured Projects
add_section_title(doc, 'Featured Projects')

# Project 1: US Airlines
p1 = doc.add_paragraph()
p1.paragraph_format.space_before = Pt(2.5); p1.paragraph_format.space_after = Pt(0.5); p1.paragraph_format.keep_with_next = True
r_p1_title = p1.add_run('US Commercial Airlines: Flight Delay & Network Operations Forensics')
r_p1_title.font.name = 'Calibri'; r_p1_title.font.size = Pt(9.5); r_p1_title.font.bold = True; r_p1_title.font.color.rgb = DARK_NAVY
r_p1_tech = p1.add_run('  |  Power BI, DAX, Python, DuckDB, Scikit-Learn, Three.js WebGL')
r_p1_tech.font.name = 'Calibri'; r_p1_tech.font.size = Pt(8.5); r_p1_tech.font.italic = True; r_p1_tech.font.color.rgb = SLATE_GRAY

add_bullet(doc, '• Data Hygiene & Relational Architecture:', 'Engineered an end-to-end pipeline ingesting 518,556 flight events across 291 US airports and 44,729 runways; resolved entity key anomalies (CYS fallback) and aggregated runways 1:1, preventing Cartesian joins and reducing storage by 85% via columnar Parquet.')
add_bullet(doc, '• In-Memory SQL & Live Web Scraping:', 'Integrated an in-memory DuckDB ANSI SQL engine executing multi-tier CTE cross-joins in <80ms; scraped live Wikipedia FAA enplanements to uncover the "Medium Hub Paradox" (Medium Hubs suffering 47.2% delays vs 44.6% in Mega Hubs due to physical capacity constraints).')
add_bullet(doc, '• Machine Learning Benchmark:', 'Benchmarked 4 predictive ML models via Scikit-Learn ColumnTransformer; deployed a Champion HistGradientBoosting model achieving 0.742 ROC-AUC (68.6% Accuracy), isolating departure minute (39.2% Gini) and Southwest turnarounds (21.4%) as top delay drivers.')
add_bullet(doc, '• Executive BI & 3D WebGL Telemetry:', 'Architected a 2-page Power BI executive suite with star schema modeling, quantifying a $938.1M FAA economic loss ($74.24/min); developed a custom 3D WebGL spherical airspace radar (.pbiviz) with animated flight paths and real-time corridor hover telemetry.')

# Project 2: PLG Funnel
p2 = doc.add_paragraph()
p2.paragraph_format.space_before = Pt(2.5); p2.paragraph_format.space_after = Pt(0.5); p2.paragraph_format.keep_with_next = True
r_p2_title = p2.add_run('PLG Funnel Analysis and High-Intent User Prediction')
r_p2_title.font.name = 'Calibri'; r_p2_title.font.size = Pt(9.5); r_p2_title.font.bold = True; r_p2_title.font.color.rgb = DARK_NAVY
r_p2_tech = p2.add_run('  |  SQL, Python, Pandas, Scikit-Learn, Jupyter')
r_p2_tech.font.name = 'Calibri'; r_p2_tech.font.size = Pt(8.5); r_p2_tech.font.italic = True; r_p2_tech.font.color.rgb = SLATE_GRAY

add_bullet(doc, '• Funnel Analytics:', 'Conducted end-to-end SQL funnel analysis for a freemium SaaS dataset to track signup-to-paid conversion rates and surface key activation bottlenecks across user lifecycle stages.')
add_bullet(doc, '• Predictive Lead Scoring:', 'Built a high-intent user classification model pairing behavioral feature engineering with Scikit-Learn to score likely converters, directly supporting targeted product-growth outreach.')

# Project 3: Delhi Temp
p3 = doc.add_paragraph()
p3.paragraph_format.space_before = Pt(2.5); p3.paragraph_format.space_after = Pt(0.5); p3.paragraph_format.keep_with_next = True
r_p3_title = p3.add_run('Delhi Temperature Forecasting on AWS')
r_p3_title.font.name = 'Calibri'; r_p3_title.font.size = Pt(9.5); r_p3_title.font.bold = True; r_p3_title.font.color.rgb = DARK_NAVY
r_p3_tech = p3.add_run('  |  AWS S3, Amazon Athena, Python, Pandas, Facebook Prophet')
r_p3_tech.font.name = 'Calibri'; r_p3_tech.font.size = Pt(8.5); r_p3_tech.font.italic = True; r_p3_tech.font.color.rgb = SLATE_GRAY

add_bullet(doc, '• Cloud Data Pipeline:', 'Built an automated cloud forecasting pipeline on NOAA climate records from 1942 to 2025, storing raw datasets in Amazon S3 and executing serverless analytical queries using Amazon Athena.')
add_bullet(doc, '• Time-Series Modeling:', 'Aggregated daily records into monthly seasonal features and trained a Prophet model, improving forecast accuracy from a naive baseline RMSE of 9.06 to 1.42.')

# 4. Education & Certifications
add_section_title(doc, 'Education & Certifications')
ed1 = doc.add_paragraph()
ed1.paragraph_format.space_before = Pt(1.5); ed1.paragraph_format.space_after = Pt(0.5)
r_ed1 = ed1.add_run("Master's Program in Data Science")
r_ed1.font.name = 'Calibri'; r_ed1.font.size = Pt(9); r_ed1.font.bold = True; r_ed1.font.color.rgb = CHARCOAL
r_ed1_sub = ed1.add_run('  |  Simplilearn in collaboration with IBM  (2025)')
r_ed1_sub.font.name = 'Calibri'; r_ed1_sub.font.size = Pt(9); r_ed1_sub.font.color.rgb = SLATE_GRAY

ed2 = doc.add_paragraph()
ed2.paragraph_format.space_before = Pt(0.5); ed2.paragraph_format.space_after = Pt(0.5)
r_ed2 = ed2.add_run('Bachelor of Commerce (B.Com)')
r_ed2.font.name = 'Calibri'; r_ed2.font.size = Pt(9); r_ed2.font.bold = True; r_ed2.font.color.rgb = CHARCOAL
r_ed2_sub = ed2.add_run('  |  Sardar Patel Smarak Mahavidhyalaya, Larpur  (2022)')
r_ed2_sub.font.name = 'Calibri'; r_ed2_sub.font.size = Pt(9); r_ed2_sub.font.color.rgb = SLATE_GRAY

ed3 = doc.add_paragraph()
ed3.paragraph_format.space_before = Pt(0.5); ed3.paragraph_format.space_after = Pt(1)
r_ed3 = ed3.add_run('Simplilearn Certified Data Scientist')
r_ed3.font.name = 'Calibri'; r_ed3.font.size = Pt(9); r_ed3.font.bold = True; r_ed3.font.color.rgb = CHARCOAL
r_ed3_sub = ed3.add_run("  |  Master's Program in collaboration with IBM  (2025)")
r_ed3_sub.font.name = 'Calibri'; r_ed3_sub.font.size = Pt(9); r_ed3_sub.font.color.rgb = SLATE_GRAY

out_path1 = r'Project_3_US_Airlines_Delay_Analytics\explanation\Auchitya_Singh_Data_Analyst_Resume.docx'
out_path2 = r'C:\Users\91945\OneDrive\Desktop\Auchitya_Singh_Data_Analyst_Resume.docx'
doc.save(out_path1)
doc.save(out_path2)
print('SUCCESS: Saved resume docx to project explanation and Desktop!')
