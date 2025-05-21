# 🌞 MoonLight Energy Solutions: Solar Challenge Week 1

Welcome to the official repository for **Solar Challenge Week 1** by **MoonLight Energy Solutions**! This project is part of our broader mission to harness data-driven strategies that accelerate sustainable energy adoption through targeted solar investments across the African continent.

🔗 **Repository URL**: [github.com/dagmaros27/solar-challenge-week1](https://github.com/dagmaros27/solar-challenge-week1)

---

## 📌 Project Purpose

As an Analytics Engineer at MoonLight Energy Solutions, your objective is to analyze environmental sensor data and solar radiation measurements to:

- Understand temporal and spatial solar trends.
- Evaluate the efficiency of sensor modules (ModA/ModB).
- Identify high-potential regions for solar infrastructure deployment.
- Deliver actionable insights for long-term sustainable energy planning.

---

## 🗂️ Folder Structure

```
solar-challenge-week1/
├── app/                  # Streamlit dashboard source
│   ├── main.py           # Main dashboard script
│   └── utils.py          # Reusable data/plotting functions
├── data/                 # (ignored) Cleaned input CSVs for each country
├── notebooks/            # Country-specific EDA notebooks
├── scripts/              # Analysis or automation scripts (if any)
├── tests/                # (optional) Unit tests
├── dashboard_screenshots/ # Screenshots of Streamlit UI for reference
├── .github/workflows/    # GitHub Actions CI
├── .gitignore
├── requirements.txt
└── README.md
```

> 🔒 Note: All raw/clean data is stored locally under `data/` and excluded via `.gitignore`.

---

## 📈 Dataset Description

The dataset contains solar radiation and environmental observations, including sensor performance and weather conditions. Below is a quick overview of the key fields:

| Column        | Description                                                                  |
| ------------- | ---------------------------------------------------------------------------- |
| Timestamp     | Date and time of observation (yyyy-mm-dd hh\:mm)                             |
| GHI (W/m²)    | Global Horizontal Irradiance – total solar energy received on a flat surface |
| DNI (W/m²)    | Direct Normal Irradiance – solar radiation perpendicular to the sun's rays   |
| DHI (W/m²)    | Diffuse Horizontal Irradiance – scattered sunlight on a horizontal surface   |
| ModA / ModB   | Sensor module irradiance measurements                                        |
| Tamb (°C)     | Ambient temperature                                                          |
| RH (%)        | Relative humidity                                                            |
| WS / WSgust   | Wind speed and gust measurements                                             |
| WD / WDstdev  | Wind direction and variability                                               |
| BP (hPa)      | Barometric pressure                                                          |
| Cleaning      | Binary flag indicating sensor cleaning                                       |
| Precipitation | Precipitation rate (mm/min)                                                  |
| TModA / TModB | Module-specific temperatures                                                 |
| Comments      | Free-text observations                                                       |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/dagmaros27/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Set Up the Environment

Install dependencies using:

```bash
pip install -r requirements.txt
```

### 3. Add Cleaned Data

Place cleaned CSV files inside the `data/` folder (e.g., `benin_clean.csv`, `togo_clean.csv`, etc.). These should not be committed to Git.

### 4. Explore EDA Notebooks

Each country has its own branch and EDA notebook:

```bash
git checkout eda-benin       # or eda-togo, eda-sierra-leone
```

Open the notebook in JupyterLab or VS Code to explore visual trends, correlations, and statistical outliers.

### 5. Launch the Dashboard Locally

```bash
streamlit run app/main.py
```

You’ll get an interactive UI to:

- Select countries
- View GHI boxplots and top regions table
- Understand which areas are most promising for solar deployment

📷 Screenshots of the dashboard are saved under the `dashboard_screenshots/` folder.

---

## 📊 Deliverables Overview

### ✅ Task 1: Git & CI/CD Setup

- `.gitignore`, GitHub Actions, clean repo structure

### ✅ Task 2: Data Profiling & Cleaning

- Outlier detection using Z-scores
- Null handling via median imputation
- Visual analysis (GHI/DNI/DHI) and sensor comparisons

### ✅ Task 3: Cross-Country Comparison

- Boxplots, ANOVA/Kruskal-Wallis tests
- Summary tables and statistical insight
- Prioritization recommendations: Togo > Benin > Sierra Leone

### 🎁 Bonus: Streamlit Dashboard

- Dynamic data selection
- GHI distribution and ranking tables
- Modularized via `utils.py`
- Screenshots provided

---

## 🤝 Contributors

- **Dagmaros27** – Analytics Engineer
