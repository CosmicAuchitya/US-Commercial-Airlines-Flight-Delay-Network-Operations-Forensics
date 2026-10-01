# US Airlines Delay Analytics: Master Question & Investigation Register

**Author:** Auchitya Singh  
**Role:** Commercial & Insight Data Analyst  
**Project:** US Airlines Delay & Operational Forensics Pipeline (518,556 Flight Records, 291 Airports)  
**Status:** Complete Forensic Analytics Register (Data Science, Statistical Testing, ML Pipeline, SQL & Storytelling)  

---

## 🎯 Project Core Objective
Uncover the commercial, operational, and physical infrastructure root causes of flight delays across 518K+ commercial US flights, 291 airports, and 44K runways to provide actionable strategic advisories for airline executives, airport operators, and passengers.

---

## 📋 Master Question Tracking Matrix

| Q# | Category | Research Question / Forensic Hypothesis | Status | Key Analytical & Statistical Finding |
| :---: | :--- | :--- | :---: | :--- |
| **Q01** | Commercial | What is the total dollar cost burden of delays across 518K flights at \$74.24/min? | **SOLVED** | 45.12% baseline delay rate (233,989 delayed flights). Assuming conservative 45-min average delay per flight, estimated economic impact exceeds \$780M across the dataset. |
| **Q02** | Carrier | **Southwest (WN) 70% Anomaly vs Competitors:** How does WN compare to all 16 carriers? | **SOLVED** | WN has the highest delay rate in the country (**69.78%**, 65,657 flights). Continental (56.62%), JetBlue (46.70%), Delta (45.05%), Mesa (24.29%). Saved to `01_airline_delay_comparison.png`. |
| **Q03** | Carrier | **WN vs Punctual Carriers (YV, OH, HA) Deep-Dive:** Why is WN at 70% while YV is 24% and HA is 32%? | **SOLVED** | **Aviation Model Divergence:** WN operates point-to-point with tight 20-min turns, creating a cascading domino delay from 47.5% (morning) to 81.7% (night). OH/YV operate hub-and-spoke with 45-60 min hub buffers that absorb upstream delays. HA operates 42-min median island hops in calm Pacific weather. |
| **Q04** | Temporal | **Day of Week Safety Index:** Which day of the week is safest (lowest delay probability)? | **SOLVED** | **Saturday is safest (40.56% delay)**. Wednesday is worst (47.58% delay). Saved to `02_weekday_delay_safety.png`. |
| **Q05** | Temporal | **Volume Pressure vs Delay:** Does higher flight frequency on Thursdays/Wednesdays drive delay spikes? | **SOLVED** | Saturday volume drops to 56,354 vs Thursday 87,988; delay rates directly track commercial airspace congestion. |
| **Q06** | Temporal | **Hourly Snowball Effect & Long Flights (Task 3d):** Departure patterns of long-haul flights (>4h)? | **SOLVED** | Bimodal schedule: Morning rush (7-9 AM, 31% of flights) and Night Red-Eye (10-11 PM, 10%). Delay starts low at 6 AM (33.1%), climbs to peak at 7 PM (60.5%), and cools down during late night red-eyes (40.4%). Saved to `03_long_flight_departure_patterns.png`. |
| **Q07** | Route | **Short-Haul vs Medium vs Long-Haul (Task 3c):** Which airlines should be recommended for each distance bracket? | **SOLVED** | **Short-haul (<=2h):** Mesa (YV - 23.7%), PSA (OH - 26.7%). **Medium-haul (2-4h):** Mesa (YV - 27.3%), United (UA - 30.5%). **Long-haul (>4h):** United (UA - 37.8%), Alaska (AS - 38.1%). Avoid Continental (59.8%) and Southwest (70.9%) on long routes. |
| **Q08** | Route | **Busiest Corridors & Asymmetry:** Are top routes (LAX-SFO) delay super-spreaders? | **SOLVED** | High-volume trunk routes experience heavy delay: LAX-SFO (55.4% delay) due to SFO marine layer fog and parallel runway spacing, whereas OGG-HNL is at 22.4%. Exported to `tableau_route_corridors.csv`. |
| **Q09** | Spatial | **Haversine Distance & Ground Speed:** What is actual flight distance vs scheduled duration (block speed)? | **SOLVED** | Vectorized great-circle distance computed across all 518K flights. Range: 31.0 miles (inter-island) to 4,954.5 miles (continental/Pacific). Median effective block speed: 306.0 mph. Distance categories created: Short-haul (<=500 mi: 219K flights), Medium-haul (500-1500 mi: 245K flights), Long-haul (>1500 mi: 54K flights). Exported to `tableau_route_corridors.csv` and `tableau_airline_performance.csv`. |
| **Q10** | Infrastructure | **Large Hubs vs Medium Hubs (Task 4):** How do delay rates compare at primary vs secondary hubs? | **SOLVED** | **The Medium Hub Bottleneck Paradox:** Medium Hubs suffer higher delay (**50.51%**) than Large Hubs (**45.99%**) because they have only 1-2 runways but face intense Southwest low-cost scheduling. Small/Regional hubs are at **36.01%**. Saved to `04_hub_category_delay_comparison.png`. |
| **Q11** | Infrastructure | **Altitude / Elevation Hypothesis (Task 5a):** Does airport altitude affect delay rate ($H_0$ testing)? | **SOLVED** | **Reject $H_0$.** Departure elevation ($t = 7.68, p = 1.60\times 10^{-14}$) and Arrival elevation ($t = 8.71, p = 3.07\times 10^{-18}$). Higher elevation significantly increases delay probability. |
| **Q12** | Infrastructure | **Runway Capacity Hypothesis (Task 5b):** Does runway count affect delays ($H_0$ testing)? | **SOLVED** | **Reject $H_0$.** Origin runway count ($t = 21.57, p = 3.67\times 10^{-103}$) and Destination runway count ($t = -44.88, p < 10^{-300}$). Fewer destination runways create acute arrival holding and runway congestion bottlenecks. |
| **Q13** | Operational | **Flight Length Hypothesis (Task 5c):** Does duration of flight affect delay ($H_0$ testing)? | **SOLVED** | **Reject $H_0$.** Flight length ($t = 29.17, p = 5.86\times 10^{-187}$). Longer flights accumulate greater airborne routing delays and weather deviations. |
| **Q14** | Operational | **Correlation Matrix & Predictor Interdependence (Task 6):** How do predictors correlate with delay? | **SOLVED** | Correlation matrix computed across 10 numeric predictors. `Time` has strongest positive correlation with `Delay` ($r = 0.150$). Destination runways negatively correlate with delay risk. Heatmap saved to `05_correlation_matrix_heatmap.png`. |
| **Q15** | Commercial | **Landing at 10+ Runway Mega-Airports (SQL Q3):** What is the delay rate at airports like ORD/DFW? | **SOLVED** | Only **37.37%** delay rate across 24,871 landing flights (7.75% lower than national average of 45.12%). Proves that massive runway redundancy shields airlines from ground holding delays. |
| **Q16** | Fleet | **Airline Age & Experience (Task 1b):** Does fleet operating maturity correlate with on-time reliability? | **SOLVED** | Web scraped 88 airlines from Wikipedia. Mature network legacies (Delta founded 1924, United 1926, American 1926) perform at 32-45% delay, whereas Southwest (1967) is at 69.8%. Network topology (point-to-point vs hub-and-spoke) is far more determinative than carrier founding date ($r = -0.08$). |
| **Q17** | Infrastructure | **Elevation Tiers Matrix (SQL Q4):** Delays above vs below average elevation? | **SOLVED** | Below Avg Origin + Above Avg Destination exhibits highest delay rate (**46.91%**, 42,448 flights). Above Avg Origin + Above Avg Destination has lowest delay (**44.44%**). |
| **Q18** | Modeling | **SGD Logistic Regression (Week 1 ML):** Scalable linear baseline for 518K records. | **SOLVED** | Train Accuracy: **63.24%**, Test Accuracy: **62.95%**, ROC-AUC: **0.6748**. Demonstrates linear separable baseline on massive dataset in <2 seconds. |
| **Q19** | Modeling | **Decision Tree Overfitting Control (Week 1 ML):** Unpruned vs Pruned Tree. | **SOLVED** | Unpruned tree overfitted heavily (Train Acc: 81.81%, Test Acc: 60.81%, 21% gap). Pruned tree (`max_depth=10, min_samples_leaf=50`) eliminated overfitting: Train Acc: **65.28%**, Test Acc: **64.81%**, Test ROC-AUC: **0.6874**. |
| **Q20** | Modeling | **Gradient Boosting & Top Delay Drivers (Week 1 ML):** Non-linear boosting performance. | **SOLVED** | `HistGradientBoostingClassifier` achieved the highest performance overall: Train Acc: **66.19%**, Test Acc: **65.76%**, ROC-AUC: **0.7081**. Feature Importance proved that **`Airline_WN` (42.5%)** and **`Time` (25.9%)** account for over **68.4% of total model decision weight**. |
| **Q21** | Modeling | **Stratified 5-Fold Cross Validation Voting (Week 1 ML):** Majority voting ensemble. | **SOLVED** | 5-Fold Voting Ensemble achieved **65.08%** test accuracy and **0.6938** ROC-AUC, demonstrating stable out-of-fold generalization across all airline and airport segments. |
| **Q22** | Storytelling | **Passenger Travel Playbook (Executive Takeaway):** Optimal travel recommendations. | **SOLVED** | 1) Fly Saturday morning (safest slot, <35% delay). 2) Avoid Wednesday/Thursday evening flights on Southwest and Continental (>75% delay). 3) Select United or Alaska for long-haul routes. |
| **Q23** | Storytelling | **Airline Operations & Airport COO Advisory (Executive Takeaway):** Operational remedies. | **SOLVED** | 1) Southwest must inject scheduled slack buffers at high-traffic secondary hubs (MDW, BNA, DAL). 2) Medium hubs require rapid-exit taxiway enhancements to break the 50.5% bottleneck. |

---

## 🔬 Statistical Hypothesis Testing Scorecard (Task 5)

| Test # | Hypothesis Statement | Test Type | t-Statistic | p-Value | Null Hypothesis ($H_0$) Decision | Substantive Analytical Takeaway |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **5a** | Origin Airport Altitude vs Flight Delay | Welch's Two-Sample t-test | $+7.680$ | $1.60\times 10^{-14}$ | **REJECT $H_0$** | Delayed flights depart from significantly higher elevations (mean 932.4 ft vs 894.6 ft). |
| **5a** | Destination Airport Altitude vs Flight Delay | Welch's Two-Sample t-test | $+8.709$ | $3.07\times 10^{-18}$ | **REJECT $H_0$** | High-altitude destinations incur higher arrival vectoring and thin-air spacing delays. |
| **5b** | Origin Runway Count vs Flight Delay | Welch's Two-Sample t-test | $+21.572$ | $3.67\times 10^{-103}$ | **REJECT $H_0$** | High origin runway count correlates with complex mega-hub taxi queues. |
| **5b** | Destination Runway Count vs Flight Delay | Welch's Two-Sample t-test | $-44.885$ | $<10^{-300}$ | **REJECT $H_0$** | Destination runway scarcity is an acute delay catalyst; fewer runways lead to arrival holding patterns. |
| **5c** | Flight Duration (Length) vs Flight Delay | Welch's Two-Sample t-test | $+29.175$ | $5.86\times 10^{-187}$ | **REJECT $H_0$** | Longer flights (mean 136.2 mins delayed vs 128.5 mins on-time) face cumulative en-route airspace delays. |

---

## 🤖 Machine Learning Model Benchmark (Week 1 ML)

| Model Name | Preprocessing Pipeline | Train Accuracy | Test Accuracy | Precision (Delay=1) | Recall (Delay=1) | F1-Score | ROC-AUC | Overfitting Evaluation |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **SGD Logistic Regression** | StandardScaler + OneHot + Ordinal | 63.24% | 62.95% | 61.26% | 48.68% | 0.5425 | 0.6748 | Zero overfitting. Fast linear baseline. |
| **Decision Tree (Unpruned)** | OneHot + Ordinal | 81.81% | 60.81% | 56.40% | 57.10% | 0.5674 | 0.6045 | **Severe Overfitting** (21.0% train-test accuracy gap). |
| **Decision Tree (Pruned)** | Max Depth=10, Min Leaf=50 | 65.28% | 64.81% | 66.44% | 44.49% | 0.5329 | 0.6874 | **Overfitting Solved** (0.47% train-test gap). |
| **5-Fold Ensemble DT (Voting)** | Stratified 5-Fold Majority Vote | N/A (CV) | 65.08% | 68.49% | 41.89% | 0.5198 | 0.6938 | Reduced variance, high precision (68.5%). |
| **HistGradientBoosting** | LightGBM-style Histogram Booster | **66.19%** | **65.76%** | **66.86%** | **47.81%** | **0.5575** | **0.7081** | **Champion Model:** Highest overall accuracy and ROC-AUC. |

### Top Delay Feature Importances:
1. `Airline_WN` (Southwest Airlines): **42.50%**
2. `Time` (Departure Time from Midnight): **25.93%**
3. `Length` (Flight Scheduled Duration): **5.63%**
4. `from_elevation_ft` (Origin Altitude): **5.05%**
5. `Airline_CO` (Continental Airlines): **4.08%**
6. `from_runway_count` (Origin Runway Redundancy): **3.61%**
7. `DayOfWeek` (Day of Travel): **2.67%**
8. `to_elevation_ft` (Destination Altitude): **2.51%**

---

## 🗄️ SQL Analytics Executive Output Tables (Week 2 SQL)

### Query 1: Delays by Day of Week
| DayOfWeek | DayName | Total Flights | Delayed Flights | On-Time Flights | Delay % |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 1 | Monday | 70,008 | 33,059 | 36,949 | 47.22% |
| 2 | Tuesday | 68,721 | 31,072 | 37,649 | 45.21% |
| 3 | Wednesday | 86,478 | 41,144 | 45,334 | **47.58% (Worst)** |
| 4 | Thursday | 87,988 | 40,280 | 47,708 | 45.78% |
| 5 | Friday | 81,797 | 34,813 | 46,984 | 42.56% |
| 6 | Saturday | 56,354 | 22,860 | 33,494 | **40.56% (Safest)** |
| 7 | Sunday | 67,210 | 30,761 | 36,449 | 45.77% |

### Query 2: Delays by Airline (Top 5 vs Bottom 5)
| Airline | Carrier Name / Network Model | Total Flights | Delayed Flights | Delay % | Avg Duration (min) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **WN** | Southwest Airlines (Point-to-Point LCC) | 94,097 | 65,657 | **69.78%** | 95.0 |
| **CO** | Continental Airlines (Legacy Network) | 21,118 | 11,957 | **56.62%** | 165.7 |
| **B6** | JetBlue Airways (Point-to-Point / Focus Cities) | 18,112 | 8,459 | **46.70%** | 173.2 |
| **OO** | SkyWest Airlines (Regional Mainline Feeder) | 50,254 | 22,760 | **45.29%** | 88.3 |
| **DL** | Delta Air Lines (Mega Hub-and-Spoke) | 60,940 | 27,452 | **45.05%** | 148.6 |
| ... | ... | ... | ... | ... | ... |
| **US** | US Airways (Hub-and-Spoke) | 34,500 | 11,591 | **33.60%** | 134.1 |
| **UA** | United Airlines (Global Hub-and-Spoke) | 27,619 | 8,946 | **32.39%** | 179.9 |
| **HA** | Hawaiian Airlines (Island Shuttle Network) | 5,578 | 1,786 | **32.02%** | 42.0 |
| **OH** | PSA Airlines (Regional Hub Feeder) | 12,630 | 3,502 | **27.73%** | 105.0 |
| **YV** | Mesa Airlines (Regional Hub Feeder) | 13,725 | 3,334 | **24.29%** | 87.2 |

### Query 3: Mega-Hub Landings (Airports with $\ge 10$ Runways - e.g. ORD, DFW)
| Landing Metric | Flights Landing at $\ge 10$ Runways | National Average Benchmark | Variance |
| :--- | :---: | :---: | :---: |
| **Total Flights Landing** | 24,871 | 518,556 | - |
| **Delayed Flights** | 9,295 | 233,989 | - |
| **Delay Percentage** | **37.37%** | **45.12%** | **-7.75% (Substantial Improvement)** |
| **On-Time Reliability** | **62.63%** | **54.88%** | **+7.75% Higher Reliability** |

### Query 4: Elevation Tiers Interaction Matrix
| Source Airport Elevation | Destination Airport Elevation | Total Flight Volume | Delayed Flights | Delay Rate (%) |
| :--- | :--- | :---: | :---: | :---: |
| Below Average Elevation | Above Average Elevation | 90,488 | 42,448 | **46.91% (Highest Risk)** |
| Above Average Elevation | Below Average Elevation | 90,490 | 40,857 | **45.15%** |
| Below Average Elevation | Below Average Elevation | 289,738 | 129,419 | **44.67%** |
| Above Average Elevation | Above Average Elevation | 47,840 | 21,265 | **44.44% (Lowest Risk)** |

---

## 📊 Tableau / Power BI Data Assets Exported

| File Name | Location | Grain / Dimensions | Business Use Case |
| :--- | :--- | :--- | :--- |
| `tableau_airline_performance.csv` | `output/tables/` | Airline (16 carriers) | Executive carrier scorecard, delay rate vs flight duration, fleet dynamics. |
| `tableau_temporal_patterns.csv` | `output/tables/` | DayOfWeek $\times$ Hour (168 cells) | Operational heatmaps, passenger departure advisory calendar, peak congestion windows. |
| `tableau_hub_infrastructure.csv` | `output/tables/` | Airport IATA (291 airports) | Geo-spatial bubble map of delays, runway capacity vs delay rate, elevation profiles. |
| `tableau_route_corridors.csv` | `output/tables/` | Origin-Destination Pairs (Top Corridors) | Trunk corridor flow analysis (e.g. LAX-SFO, ORD-LGA), route delay benchmarks. |
| `model_comparison_metrics.csv` | `output/tables/` | 4 Trained ML Architectures | Model evaluation benchmark comparing Train/Test Accuracy, Precision, Recall, F1, ROC-AUC. |

---

## 📌 Deliverable Artifacts Log
* **Figure 01:** `output/figures/01_airline_delay_comparison.png` (Southwest 69.8% anomaly).
* **Figure 02:** `output/figures/02_weekday_delay_safety.png` (Saturday safest, Wednesday riskiest).
* **Figure 03:** `output/figures/03_long_flight_departure_patterns.png` (Long-haul bimodal rush & evening delay peak).
* **Figure 04:** `output/figures/04_hub_category_delay_comparison.png` (Medium Hub Bottleneck Paradox: 50.5% vs 46.0%).
* **Figure 05:** `output/figures/05_correlation_matrix_heatmap.png` (10-feature correlation heatmap).
* **Figure 06:** `output/figures/06_model_comparison_metrics.png` (Machine learning model performance metrics comparison).
* **Figure 07:** `output/figures/07_feature_importance.png` (Decision Tree feature importance identifying Southwest & Time as dominant drivers).
* **SQL Script:** `src/02_sql_analytics_queries.sql` (Complete Week 2 ANSI SQL suite).
* **ML Script:** `src/03_machine_learning_pipeline.py` (Complete Week 1 scikit-learn ML pipeline).
* **Interactive Notebook:** `data/raw/my_flight_analytics.py` (Full `# %%` pair-programming workbook with all tasks).
