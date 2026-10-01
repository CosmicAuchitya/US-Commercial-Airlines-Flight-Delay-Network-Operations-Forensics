# 📄 Resume Project Entry: US Commercial Aviation Delay & Network Forensics

**Author:** Auchitya Singh  
**Target Roles:** Data Analyst | Power BI Developer | Analytics Engineer | Business Intelligence Specialist  

---

## 📌 Section: Projects / Relevant Experience

### Option A: Standard 4-Bullet Format (Recommended for Tech & Analytics Roles)
Use this format for standard 1-page or 2-page resumes applying to Data Analyst, BI Developer, or Analytics Engineer roles.

```markdown
**US Commercial Airlines: Flight Delay & Network Operations Forensics** | *Power BI, Python, DuckDB, Scikit-Learn*
• Engineered an end-to-end data pipeline processing 518,556 commercial flight events across 291 US airports and 44,729 runways; resolved entity key anomalies (CYS fallback) and aggregated runways 1:1, preventing Cartesian joins and achieving 85% storage reduction via columnar Parquet.
• Integrated an in-memory DuckDB ANSI SQL engine executing multi-tier CTE cross-joins in <80ms; scraped live FAA Wikipedia enplanements to uncover the "Medium Hub Paradox" (Medium Hubs suffering 47.2% delay rates vs 44.6% in Mega Hubs).
• Benchmarked 4 machine learning architectures via Scikit-Learn ColumnTransformer; deployed a Champion HistGradientBoosting model achieving 0.742 ROC-AUC (68.6% Accuracy), identifying departure minute (39.2% Gini) and Southwest turnarounds (21.4%) as top delay drivers.
• Architected a 2-page Power BI executive suite with star schema modeling, quantifying a $938.1M FAA economic loss ($74.24/min); developed a custom 3D WebGL spherical airspace radar (.pbiviz) with animated flight paths and real-time corridor hover telemetry.
```

---

### Option B: Condensed 3-Bullet Format (For Space-Constrained Resumes)
Use this format if your resume is tight on space and you need maximum impact per line.

```markdown
**US Commercial Aviation Delay Forensics & 3D Airspace Radar** | *Python, Power BI, DuckDB, Scikit-Learn*
• Built a 518K-record pipeline with entity resolution, Haversine geospatial metrics, and in-memory DuckDB SQL (<80ms execution), identifying $938.1M in FAA delay drain and isolating carrier-specific cascading turnaround failures (Southwest 69.8% delay rate).
• Conducted inferential hypothesis testing (Welch's t-tests, p < 10⁻¹⁵) and trained ML models using Scikit-Learn, attaining 0.742 ROC-AUC with HistGradientBoosting to predict flight delays based on temporal congestion and airport elevation.
• Designed an executive Power BI dashboard with dimensional star schema modeling and an interactive 3D WebGL flight radar (.pbiviz), visualizing 1,830 domestic routes with real-time flight arcs and corridor financial bleed metrics.
```

---

### Option C: Business Intelligence & Power BI Heavy Focus
Use this format when applying specifically for Power BI / BI Specialist / Data Visualization roles.

```markdown
**Aviation Operations Executive BI Suite & 3D Airspace Telemetry** | *Power BI, DAX, Three.js WebGL, Python, DuckDB*
• Designed a production 2-page Power BI executive suite tracking 518,556 flights and $938.1M in FAA economic losses; implemented complex DAX measures, dynamic slicers, and a dimensional star schema (Fact Route Matrix + Dim Airports/Airlines).
• Developed and packaged a custom 3D WebGL Power BI visual (US_Aviation_Network_Map.pbiviz) using Three.js, rendering a rotating Earth globe with elevation topography, animated aircraft, and corridor financial telemetry.
• Conducted automated ETL, entity resolution, and spatial analytics in Python/DuckDB, converting 44K runway segments and BTS flight logs into high-performance analytical data marts for instant Power BI reporting.
```

---

## 🛠️ Technical Skills Section Updates for Your Resume

Make sure the following skills are added to your **Technical Skills** section:

* **Business Intelligence & Reporting:** Microsoft Power BI Desktop, DAX (Data Analysis Expressions), Star Schema Dimensional Modeling, Custom WebGL Visuals (Three.js), Tableau Data Marts.
* **Programming & Data Engineering:** Python (Pandas, NumPy), In-Memory DuckDB (ANSI SQL, CTEs, Window Functions), Columnar Parquet, Web Scraping (BeautifulSoup, urllib), Geospatial Analytics (Haversine Formula).
* **Machine Learning & Statistical Analysis:** Scikit-Learn (HistGradientBoosting, Decision Trees, SGD Classifier, ColumnTransformer), Hypothesis Testing (Welch's Two-Sample t-Test), Feature Importance (Gini), Correlation Analysis.

---

## 🎤 Interview Cheat Sheet: The 4 "Golden Stories" to Tell

When an interviewer asks: *"Tell me about a challenging data project you built"*, use this framework:

### 1. The Southwest Airlines (WN) Anomaly
> *"While Southwest was the volume leader with 94K flights, our analysis revealed an industry-worst 69.8% delay rate. By tracking delay rates across departure windows, I discovered a compounding 'snowball effect' — Southwest begins the morning at 48% delay, but because of their aggressive 25-minute aircraft turnarounds without schedule buffers, delays escalate to 81.3% by nightfall. This accounted for $150M+ in concentrated losses across just 5 key routes like Dallas to Houston."*

### 2. The Medium Hub Bottleneck Paradox
> *"Most people assume larger airports have worse delays. By scraping live FAA enplanement data from Wikipedia and merging it with flight records, I discovered that Medium Hubs (e.g., Burbank, Oakland) actually suffer higher delays (47.2%) than Mega Hubs (44.6%). Medium hubs absorb high traffic spillover but lack the parallel runways and advanced surface radar of mega hubs."*

### 3. In-Memory DuckDB SQL Architecture
> *"Instead of spinning up a costly cloud database, I used DuckDB directly inside the Python pipeline to execute ANSI SQL queries with complex CTEs against 518K rows in memory in under 80 milliseconds. This made the entire repository completely reproducible for any stakeholder without database setup."*

### 4. Custom 3D WebGL Flight Telemetry
> *"To bridge the gap between technical metrics and executive storytelling, I built a custom 3D WebGL visual inside Power BI using Three.js. It renders a spherical globe with flight arcs colored by financial bleed severity and real-time animated aircraft, letting executives interactively inspect route telemetry on hover."*
