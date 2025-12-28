# 🧭 Project Roadmap & Data Schema


## 1. High-Level Project Roadmap (Nested Checklist)

### PHASE 0 — Repository & Structure Setup

* [x] Create repository structure
* [x] Initialize all folders with placeholder files
* [x] Define naming conventions for files and datasets

---

### PHASE 1 — System Definition & Business Context

📁 `00_Overview_and_Assumptions/`

* [ ] Define contact center type (support + retention)
* [ ] Define operational scope (channels, size, geography)
* [ ] Define business objectives (CX, cost, retention, efficiency)
* [ ] Document assumptions (volumes, staffing, behavior)
* [ ] Document constraints (budget, SLA targets, policy limits)

**Outputs:**

* `Contact_Center_Overview.md`
* `Business_Goals_and_Objectives.md`
* `Assumptions_and_Constraints.md`

---

### PHASE 2 — Business Analysis & KPI Framework

📁 `01_KPIs_and_Business_Analysis/`

* [ ] Identify strategic goals and decision needs
* [ ] Define KPI categories:

  * Operational
  * CX
  * Quality
  * Workforce
  * Cost
  
* [ ] Define each KPI’s purpose, formula, and interpretation
* [ ] Map goals → KPIs
* [ ] Document KPI tradeoffs and conflicts

**Outputs:**

* `KPI_Framework.md`
* `KPI_Dictionary.xlsx`
* `Goal_to_Metric_Mapping.md`
* `Tradeoffs_and_Conflicts.md`

---

### PHASE 3 — Data Design & Generation

📁 `02_Data/`

* [ ] Design data model (tables, keys, relationships)
* [ ] Define required datasets
* [ ] Generate realistic simulated data
* [ ] Clean and aggregate raw data
* [ ] Validate data consistency across tables

**Outputs:**

* `Raw_Data/*.csv`
* `Processed_Data/*.xlsx`

(See **Section 4 — Data Schema**)

---

### PHASE 4 — BI & Reporting

📁 `03_BI_and_Reporting/`

* [ ] Build Excel-based KPI calculations
* [ ] Perform trend and variance analysis
* [ ] Design operational dashboards
* [ ] Design CX-focused dashboards
* [ ] Write weekly performance insights

**Outputs:**

* `Excel_Analysis/*.xlsx`
* `Dashboards/*.xlsx / *.pbix`
* `Weekly_Insights_Report.md`

---

### PHASE 5 — Operations & Process Improvement

📁 `04_Operations_and_Process_Improvement/`

* [ ] Map As-Is process flow
* [ ] Identify bottlenecks and constraints
* [ ] Perform root cause analysis
* [ ] Estimate cost per contact
* [ ] Propose process improvements
* [ ] Discuss operational tradeoffs

**Outputs:**

* `Process_Mapping/*.md`
* `Bottleneck_Analysis.md`
* `Cost_Per_Contact_Analysis.xlsx`
* `Improvement_Proposals.md`

---

### PHASE 6 — Quality & CX Analytics

📁 `05_Quality_and_CX_Analytics/`

* [ ] Define quality dimensions and behaviors
* [ ] Design QA scorecard
* [ ] Analyze scripts for effectiveness
* [ ] Perform manual sentiment analysis
* [ ] Compare QA scores vs CX outcomes

**Outputs:**

* `QA_Framework.md`
* `QA_Scorecard.xlsx`
* `Script_Analysis.md`
* `Sentiment_Analysis/*`
* `Quality_vs_CX_Insights.md`

---

### PHASE 7 — Workforce & Capacity Thinking

📁 `06_Workforce_and_Capacity/`

* [ ] Analyze historical volume patterns
* [ ] Perform basic volume forecasting
* [ ] Analyze staffing, shrinkage, occupancy
* [ ] Simulate SLA risk scenarios
* [ ] Document real-time decision examples

**Outputs:**

* `Volume_Forecasting.xlsx`
* `Staffing_and_Shrinkage_Analysis.md`
* `SLA_Risk_Scenarios.md`
* `Real_Time_Decision_Examples.md`

---

### PHASE 8 — Executive Synthesis

📁 `07_Executive_Synthesis/`

* [ ] Integrate insights across all functions
* [ ] Define decision scenario (budget cut, volume spike, policy change)
* [ ] Evaluate tradeoffs and risks
* [ ] Produce executive recommendation

**Outputs:**

* `Executive_Decision_Memo.md`
* `Key_Findings_Summary.md`
* `Risks_and_Assumptions.md`

---

## 2. Data Schema (Complete Overview)

This project uses **simulated but realistic operational data**, designed to mirror common contact center systems.

---

### Table Overview

| Table             | Purpose                      | Approx. Records |
| ----------------- | ---------------------------- | --------------- |
| `call_volume`     | Demand over time             | 3,000–5,000     |
| `aht_data`        | Handling time metrics        | 3,000–5,000     |
| `csat_data`       | Customer experience outcomes | 2,000–4,000     |
| `qa_scores`       | Quality evaluation results   | 1,000–2,000     |
| `staffing_levels` | Workforce capacity           | 3,000–5,000     |

---

### Table Schemas

#### `call_volume.csv`

| Column          | Type    | Description                  |
| --------------- | ------- | ---------------------------- |
| date            | DATE    | Calendar date                |
| interval        | STRING  | Time interval (e.g., 30 min) |
| queue           | STRING  | Support / Retention          |
| offered_calls   | INTEGER | Total incoming calls         |
| answered_calls  | INTEGER | Calls answered               |
| abandoned_calls | INTEGER | Calls abandoned              |

---

#### `aht_data.csv`

| Column        | Type    | Description         |
| ------------- | ------- | ------------------- |
| date          | DATE    | Calendar date       |
| agent_id      | STRING  | Agent identifier    |
| queue         | STRING  | Support / Retention |
| talk_time_sec | INTEGER | Talk time           |
| hold_time_sec | INTEGER | Hold time           |
| acw_time_sec  | INTEGER | After-call work     |
| aht_sec       | INTEGER | Total handling time |

---

#### `csat_data.csv`

| Column          | Type    | Description    |
| --------------- | ------- | -------------- |
| date            | DATE    | Survey date    |
| call_id         | STRING  | Interaction ID |
| queue           | STRING  | Queue          |
| csat_score      | INTEGER | 1–5 rating     |
| resolution_flag | BOOLEAN | Issue resolved |

---

#### `qa_scores.csv`

| Column            | Type    | Description           |
| ----------------- | ------- | --------------------- |
| call_id           | STRING  | Interaction ID        |
| agent_id          | STRING  | Agent identifier      |
| compliance_score  | INTEGER | Policy adherence      |
| soft_skills_score | INTEGER | Communication quality |
| script_adherence  | INTEGER | Script usage          |
| overall_score     | INTEGER | Total QA score        |

---

#### `staffing_levels.csv`

| Column        | Type    | Description         |
| ------------- | ------- | ------------------- |
| date          | DATE    | Calendar date       |
| interval      | STRING  | Time interval       |
| scheduled_fte | INTEGER | Scheduled agents    |
| available_fte | INTEGER | Logged-in agents    |
| shrinkage_pct | FLOAT   | Non-productive time |
| occupancy_pct | FLOAT   | Utilization         |
