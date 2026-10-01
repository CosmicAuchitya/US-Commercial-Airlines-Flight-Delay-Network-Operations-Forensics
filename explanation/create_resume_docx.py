import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml

doc = docx.Document()

# Set standard margins (0.4 inch top/bottom, 0.45 inch left/right for pristine layout)
sections = doc.sections
for section in sections:
    section.top_margin = Inches(0.4)
    section.bottom_margin = Inches(0.4)
    section.left_margin = Inches(0.45)
    section.right_margin = Inches(0.45)

DARK_NAVY = RGBColor(15, 23, 42)     # #0f172a
ACCENT_BLUE = RGBColor(30, 58, 138)  # #1e3a8a
CHARCOAL = RGBColor(30, 41, 59)      # #1e293b
SLATE_GRAY = RGBColor(71, 85, 105)   # #475569

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
    run_sub = sub_p.add_run('Insight Analyst | Commercial & Product Data Analytics (AI-Augmented)')
    run_sub.font.name = 'Calibri'
    run_sub.font.size = Pt(10.5)
    run_sub.font.bold = True
    run_sub.font.color.rgb = ACCENT_BLUE

    contact_p = doc.add_paragraph()
    contact_p.paragraph_format.space_before = Pt(0)
    contact_p.paragraph_format.space_after = Pt(5)
    contact_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_c = contact_p.add_run('Uttar Pradesh, India  |  +91-7982754566  |  auchityasingh86@gmail.com  |  www.auchityasingh.site\nlinkedin.com/in/auchitya-singh-7b42502a5  |  github.com/CosmicAuchitya')
    run_c.font.name = 'Calibri'
    run_c.font.size = Pt(9)
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
    
    pPr = p._p.get_or_add_pPr()
    border_xml = '<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:bottom w:val="single" w:sz="6" w:space="1" w:color="0F172A"/></w:pBdr>'
    pPr.append(parse_xml(border_xml))

def add_bullet(doc, bold_prefix, text):
    bp = doc.add_paragraph(style='List Bullet')
    bp.paragraph_format.space_before = Pt(0.5)
    bp.paragraph_format.space_after = Pt(1.5)
    bp.paragraph_format.line_spacing = 1.05
    run_b = bp.add_run(bold_prefix + ' ')
    run_b.font.name = 'Calibri'
    run_b.font.size = Pt(8.8)
    run_b.font.bold = True
    run_b.font.color.rgb = DARK_NAVY
    run_t = bp.add_run(text)
    run_t.font.name = 'Calibri'
    run_t.font.size = Pt(8.8)
    run_t.font.color.rgb = CHARCOAL

add_header(doc)

# 1. Summary
add_section_title(doc, 'Professional Summary')
sum_p = doc.add_paragraph()
sum_p.paragraph_format.space_before = Pt(2)
sum_p.paragraph_format.space_after = Pt(3)
sum_p.paragraph_format.line_spacing = 1.05
r1 = sum_p.add_run('Commercial-minded ')
r1.font.name = 'Calibri'; r1.font.size = Pt(8.8); r1.font.color.rgb = CHARCOAL
r2 = sum_p.add_run('Insight Analyst ')
r2.font.name = 'Calibri'; r2.font.size = Pt(8.8); r2.font.bold = True; r2.font.color.rgb = DARK_NAVY
r3 = sum_p.add_run('combining a strong academic foundation in Commerce (B.Com) with advanced analytics engineering and data science training (IBM / Simplilearn). Specializes in unit economics, gross margin leakage diagnostics, customer churn root-cause autopsies, and operational bottleneck forensics. ')
r3.font.name = 'Calibri'; r3.font.size = Pt(8.8); r3.font.color.rgb = CHARCOAL
r4 = sum_p.add_run('Pioneers an AI-augmented analytical workflow, ')
r4.font.name = 'Calibri'; r4.font.size = Pt(8.8); r4.font.bold = True; r4.font.color.rgb = ACCENT_BLUE
r5 = sum_p.add_run('pairing critical business judgment and hypothesis formulation with autonomous AI pair-programming agents for accelerated data modeling, forensic code integrity, and rapid production deployment. Demonstrated capability translating 500K+ transactional logs into C-suite strategy, modeling over $938.1M in FAA delay drain, $1.09M in identified EBITDA recovery, and $1.67M in subscription ARR at risk through advanced SQL, Power BI, Python, and DuckDB.')
r5.font.name = 'Calibri'; r5.font.size = Pt(8.8); r5.font.color.rgb = CHARCOAL

# 2. Competencies
add_section_title(doc, 'Core Competencies & Technical Stack')
skills_data = [
    ('Commercial & Product Analytics:', 'Unit Economics, Gross Margin Forensics, Customer Retention & Churn Autopsy, 12-Month Cohort Retention Heatmaps, RFM Customer Segmentation, PLG Funnel Optimization, LTV & ARR Modeling, Pricing & Installment Elasticity.'),
    ('Data Modeling & Querying:', 'Advanced SQL (CTEs, Window Functions, DDL/DML, Performance Indexing), In-Memory DuckDB Engine, Columnar Parquet Storage, Star Schema Data Warehousing, Relational Database Modeling (MySQL 8.0, PostgreSQL, SQLite).'),
    ('Business Intelligence & Storytelling:', 'Power BI Desktop (DAX Measures, Data Modeling, Custom 3D WebGL Airspace Radar via Three.js, SaaS-Grade KPI Cockpits, Custom SVG Wireframing), Tableau, Executive Scorecards, Commercial Data Storytelling.'),
    ('Programming & Data Science:', 'Python (pandas, NumPy, scikit-learn, statsmodels, scipy.stats), Git/GitHub, REST APIs, Web Scraping (BeautifulSoup), FAISS (Vector Indexing), Streamlit.'),
    ('AI-Augmented Workflow:', 'Autonomous AI Pair-Programming Agents, Prompt Architecture for Code Refactoring, Automated Forensic Code Auditing, AI-Accelerated ETL & Unit Testing.')
]
for cat, desc in skills_data:
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0.5)
    sp.paragraph_format.space_after = Pt(0.5)
    r_cat = sp.add_run(cat + ' ')
    r_cat.font.name = 'Calibri'; r_cat.font.size = Pt(8.8); r_cat.font.bold = True; r_cat.font.color.rgb = DARK_NAVY
    r_desc = sp.add_run(desc)
    r_desc.font.name = 'Calibri'; r_desc.font.size = Pt(8.8); r_desc.font.color.rgb = CHARCOAL

# 3. Featured Projects
add_section_title(doc, 'Featured Analytical Projects')

# Project 1: US Airlines
p1 = doc.add_paragraph()
p1.paragraph_format.space_before = Pt(3); p1.paragraph_format.space_after = Pt(0.5); p1.paragraph_format.keep_with_next = True
r_p1_title = p1.add_run('US Commercial Airlines: Flight Delay & Network Operations Forensics')
r_p1_title.font.name = 'Calibri'; r_p1_title.font.size = Pt(9.5); r_p1_title.font.bold = True; r_p1_title.font.color.rgb = DARK_NAVY
r_p1_tech = p1.add_run('  |  Power BI, In-Memory DuckDB (ANSI SQL), Python, Three.js WebGL')
r_p1_tech.font.name = 'Calibri'; r_p1_tech.font.size = Pt(8.2); r_p1_tech.font.italic = True; r_p1_tech.font.color.rgb = SLATE_GRAY

add_bullet(doc, '• Relational Data Architecture:', 'Ingested and harmonized 518,556 commercial flight events across 291 US airports and 44,729 runways; resolved entity key anomalies (CYS fallback) and compressed storage by 85% via columnar Parquet with zero Cartesian row inflation.')
add_bullet(doc, '• Economic Bleed & Savings Plan:', 'Quantified a $938.1M fleet-wide economic delay bleed using the FAA standard $74.24/min aircraft operating cost; formulated a buffer-protection turnaround strategy identifying $99.4M in addressable operational savings.')
add_bullet(doc, '• Operational Choke Autopsy:', 'Uncovered the "Southwest Turnaround Anomaly": identified that Southwest Airlines operates the highest domestic volume (94K flights) but suffers an industry-worst 69.8% delay rate due to unbuffered 25-minute turnarounds causing delays to compound from 48.2% morning to 81.3% night ($150M+ loss across 5 corridors).')
add_bullet(doc, '• In-Memory DuckDB & Live Scraping:', 'Integrated an in-memory DuckDB ANSI SQL engine executing multi-tier elevation and hub CTE cross-joins in <80ms; scraped live Wikipedia FAA enplanements to uncover the "Medium Hub Paradox" (Medium Hubs suffering 47.2% delays vs 44.6% in Mega Hubs due to runway bottlenecking).')
add_bullet(doc, '• Machine Learning & 3D WebGL Telemetry:', 'Deployed a Champion HistGradientBoosting model achieving 0.742 ROC-AUC (68.6% Accuracy); architected a 2-page Power BI executive suite featuring a custom 3D WebGL spherical airspace radar (.pbiviz) with animated flight paths and corridor hover telemetry.')

# Project 2: Olist
p2 = doc.add_paragraph()
p2.paragraph_format.space_before = Pt(3); p2.paragraph_format.space_after = Pt(0.5); p2.paragraph_format.keep_with_next = True
r_p2_title = p2.add_run('Olist E-Commerce: Unit Economics, Freight Leakage & Customer Retention Forensics')
r_p2_title.font.name = 'Calibri'; r_p2_title.font.size = Pt(9.5); r_p2_title.font.bold = True; r_p2_title.font.color.rgb = DARK_NAVY
r_p2_tech = p2.add_run('  |  MySQL 8.0, Microsoft Power BI Desktop, Star Schema, Advanced SQL, Python')
r_p2_tech.font.name = 'Calibri'; r_p2_tech.font.size = Pt(8.2); r_p2_tech.font.italic = True; r_p2_tech.font.color.rgb = SLATE_GRAY

add_bullet(doc, '• Star Schema Marketplace Architecture:', 'Modeled an enterprise relational Star Schema across 100,000+ orders, 112,000+ line items, and 99,000+ reviews, analyzing marketplace economics across a 20-month operational timeline ($13.59M total GMV).')
add_bullet(doc, '• Freight Margin Bleed & 3PL Strategy:', 'Diagnosed severe freight margin leakage exceeding 29% to 36% of GMV across high-volume categories (Electronics, Seasonal Goods); formulated a regional 3PL fulfillment model with $716,000 in estimated gross margin recovery.')
add_bullet(doc, '• Churn Autopsy & Hypothesis Busting:', 'Conducted a forensic churn autopsy revealing a 96.9% one-time buyer rate; debunked the discount-seeker hypothesis by demonstrating that 96.3% of single-order buyers paid full price with zero vouchers.')
add_bullet(doc, '• SLA Delays & Executive BI Cockpit:', 'Correlated delivery SLA breaches with a 7x surge in 1-star reviews (46.2% vs 6.6% on-time, exposing $1.16M GMV); engineered a SaaS-grade 2-page Power BI cockpit with SVG wireframes and installment elasticity proving a 3.5x basket size lift ($96 to $335 AOV).')

# Project 3: Customer Churn
p3 = doc.add_paragraph()
p3.paragraph_format.space_before = Pt(3); p3.paragraph_format.space_after = Pt(0.5); p3.paragraph_format.keep_with_next = True
r_p3_title = p3.add_run('Customer Churn Forensics, 12-Month Cohort Retention & RFM Segmentation')
r_p3_title.font.name = 'Calibri'; r_p3_title.font.size = Pt(9.5); r_p3_title.font.bold = True; r_p3_title.font.color.rgb = DARK_NAVY
r_p3_tech = p3.add_run('  |  Python (pandas, scikit-learn, seaborn), Advanced SQL, Cohort Retention Analysis')
r_p3_tech.font.name = 'Calibri'; r_p3_tech.font.size = Pt(8.2); r_p3_tech.font.italic = True; r_p3_tech.font.color.rgb = SLATE_GRAY

add_bullet(doc, '• Dual Business Model Churn Modeling:', 'Investigated customer retention mechanics across Contractual Subscriptions (7,043 accounts) and Transactional E-Commerce (541,909 retail transaction logs), isolating $1.67M in Annual Recurring Revenue (ARR) at risk.')
add_bullet(doc, '• Fiber Optic Paradox & Tech Support Moat:', 'Discovered month-to-month contracts drove 88.6% of platform churn ($1.45M ARR) at 42.7% churn rate; proved bundling Tech Support with high-risk Fiber Optic crashed churn from 55.0% to 14.2% (-40.8 pp) while lifting ARPU from $86 to $105.')
add_bullet(doc, '• 12-Month Cohort Retention Matrix:', 'Engineered a 12-month cohort retention matrix (Triangular Heatmap), proving that an 80% Month 1 customer drop-off flattens into a 25% loyal core, validating that retention investments must concentrate in the first 30 days.')
add_bullet(doc, '• RFM Customer Segmentation:', 'Executed RFM segmentation across 4,338 authenticated retail accounts, proving the Pareto principle: top 37.2% accounts drive 77.6% of total revenue ($6.92M), while isolating 550 At-Risk VIPs representing $912K in historical spend.')

# Project 4: PLG Funnel
p4 = doc.add_paragraph()
p4.paragraph_format.space_before = Pt(3); p4.paragraph_format.space_after = Pt(0.5); p4.paragraph_format.keep_with_next = True
r_p4_title = p4.add_run('Product-Led Growth (PLG) SaaS Funnel & Conversion Attribution')
r_p4_title.font.name = 'Calibri'; r_p4_title.font.size = Pt(9.5); r_p4_title.font.bold = True; r_p4_title.font.color.rgb = DARK_NAVY
r_p4_tech = p4.add_run('  |  SQL, Python (pandas, scikit-learn), Jupyter Notebook')
r_p4_tech.font.name = 'Calibri'; r_p4_tech.font.size = Pt(8.2); r_p4_tech.font.italic = True; r_p4_tech.font.color.rgb = SLATE_GRAY

add_bullet(doc, '• Product Funnel Diagnostics:', 'Analyzed multi-stage product onboarding funnels across freemium user cohorts, pinpointing friction in onboarding step 3 responsible for a 34% drop-off in user velocity; modeled high-intent conversion lead scoring for top 15% trial accounts.')

# 4. Education & Certifications
add_section_title(doc, 'Education & Credentials')
ed1 = doc.add_paragraph()
ed1.paragraph_format.space_before = Pt(1.5); ed1.paragraph_format.space_after = Pt(0.5)
r_ed1 = ed1.add_run("Master's Program in Data Science")
r_ed1.font.name = 'Calibri'; r_ed1.font.size = Pt(8.8); r_ed1.font.bold = True; r_ed1.font.color.rgb = DARK_NAVY
r_ed1_sub = ed1.add_run('  |  Simplilearn in collaboration with IBM  (2025)')
r_ed1_sub.font.name = 'Calibri'; r_ed1_sub.font.size = Pt(8.8); r_ed1_sub.font.color.rgb = SLATE_GRAY

ed2 = doc.add_paragraph()
ed2.paragraph_format.space_before = Pt(0.5); ed2.paragraph_format.space_after = Pt(0.5)
r_ed2 = ed2.add_run('Bachelor of Commerce (B.Com)')
r_ed2.font.name = 'Calibri'; r_ed2.font.size = Pt(8.8); r_ed2.font.bold = True; r_ed2.font.color.rgb = DARK_NAVY
r_ed2_sub = ed2.add_run('  |  Sardar Patel Smarak Mahavidhyalaya, Larpur  (2022)')
r_ed2_sub.font.name = 'Calibri'; r_ed2_sub.font.size = Pt(8.8); r_ed2_sub.font.color.rgb = SLATE_GRAY

ed3 = doc.add_paragraph()
ed3.paragraph_format.space_before = Pt(0.5); ed3.paragraph_format.space_after = Pt(1)
r_ed3 = ed3.add_run('Simplilearn Certified Data Scientist')
r_ed3.font.name = 'Calibri'; r_ed3.font.size = Pt(8.8); r_ed3.font.bold = True; r_ed3.font.color.rgb = DARK_NAVY
r_ed3_sub = ed3.add_run("  |  Master's Program in collaboration with IBM  (2025)")
r_ed3_sub.font.name = 'Calibri'; r_ed3_sub.font.size = Pt(8.8); r_ed3_sub.font.color.rgb = SLATE_GRAY

# Save to both Desktop and Workspace
out_desktop = r'C:\Users\91945\OneDrive\Desktop\Auchitya_Singh_Insight_Analyst_Resume.docx'
out_workspace = r'c:\Users\91945\OneDrive\Desktop\XXX\VOID DOMAIN EXPENTION\Auchitya_Singh_Insight_Analyst_Resume.docx'
doc.save(out_desktop)
doc.save(out_workspace)
print('SUCCESS: Saved Insight Analyst Resume to Desktop and Workspace!')
