import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# =========================
# CONFIGURATION
# =========================

START_DATE = "2024-01-01"
DAYS = 90
INTERVALS_PER_DAY = 26  # 30-min intervals from 8am–9pm
AGENTS = 120
QUEUES = ["Support", "Retention"]

np.random.seed(42)

# =========================
# FOLDER SETUP
# =========================

BASE_PATH = "02_Data"
RAW_PATH = os.path.join(BASE_PATH, "raw_data")

os.makedirs(RAW_PATH, exist_ok=True)

# =========================
# DATE / TIME HELPERS
# =========================

dates = pd.date_range(start=START_DATE, periods=DAYS, freq="D")
intervals = [f"{8 + i//2}:{'00' if i%2==0 else '30'}" for i in range(INTERVALS_PER_DAY)]

# =========================
# 1. CALL VOLUME DATA
# =========================

call_volume_rows = []

for date in dates:
    for interval in intervals:
        for queue in QUEUES:
            base_calls = np.random.poisson(35 if queue == "Support" else 18)
            abandonment_rate = np.random.uniform(0.03, 0.10)

            offered = max(base_calls, 5)
            abandoned = int(offered * abandonment_rate)
            answered = offered - abandoned

            call_volume_rows.append([
                date, interval, queue,
                offered, answered, abandoned
            ])

call_volume = pd.DataFrame(call_volume_rows, columns=[
    "date", "interval", "queue",
    "offered_calls", "answered_calls", "abandoned_calls"
])

# =========================
# 2. AHT DATA
# =========================

aht_rows = []

for _ in range(len(call_volume) * 4):
    agent_id = f"A{np.random.randint(1, AGENTS+1):03d}"
    queue = np.random.choice(QUEUES)
    date = np.random.choice(dates)

    talk = np.random.normal(420 if queue == "Support" else 520, 60)
    hold = np.random.normal(60, 20)
    acw = np.random.normal(90, 30)

    aht = max(talk + hold + acw, 180)

    aht_rows.append([
        date, agent_id, queue,
        int(talk), int(hold), int(acw), int(aht)
    ])

aht_data = pd.DataFrame(aht_rows, columns=[
    "date", "agent_id", "queue",
    "talk_time_sec", "hold_time_sec", "acw_time_sec", "aht_sec"
])

# =========================
# 3. CSAT DATA
# =========================

csat_rows = []

for i in range(int(len(aht_data) * 0.6)):
    row = aht_data.sample(1).iloc[0]

    base_score = np.random.normal(4, 0.6)
    aht_penalty = -0.4 if row["aht_sec"] > 700 else 0

    csat = min(max(round(base_score + aht_penalty), 1), 5)

    csat_rows.append([
        row["date"],
        f"C{i:06d}",
        row["queue"],
        csat,
        csat >= 4
    ])

csat_data = pd.DataFrame(csat_rows, columns=[
    "date", "call_id", "queue",
    "csat_score", "resolution_flag"
])

# =========================
# 4. QA SCORES
# =========================

qa_rows = []

for i in range(int(len(csat_data) * 0.5)):
    row = csat_data.sample(1).iloc[0]

    compliance = np.random.randint(70, 100)
    soft_skills = np.random.randint(65, 100)
    script = np.random.randint(60, 100)

    overall = int((compliance + soft_skills + script) / 3)

    qa_rows.append([
        row["call_id"],
        f"A{np.random.randint(1, AGENTS+1):03d}",
        compliance,
        soft_skills,
        script,
        overall
    ])

qa_scores = pd.DataFrame(qa_rows, columns=[
    "call_id", "agent_id",
    "compliance_score", "soft_skills_score",
    "script_adherence", "overall_score"
])

# =========================
# 5. STAFFING LEVELS
# =========================

staffing_rows = []

for date in dates:
    for interval in intervals:
        scheduled = np.random.randint(80, 110)
        shrinkage = np.random.uniform(0.25, 0.38)
        available = int(scheduled * (1 - shrinkage))
        occupancy = np.random.uniform(0.70, 0.92)

        staffing_rows.append([
            date, interval,
            scheduled, available,
            round(shrinkage, 2),
            round(occupancy, 2)
        ])

staffing_levels = pd.DataFrame(staffing_rows, columns=[
    "date", "interval",
    "scheduled_fte", "available_fte",
    "shrinkage_pct", "occupancy_pct"
])

# =========================
# SAVE FILES
# =========================

call_volume.to_csv(f"{RAW_PATH}/call_volume.csv", index=False)
aht_data.to_csv(f"{RAW_PATH}/aht_data.csv", index=False)
csat_data.to_csv(f"{RAW_PATH}/csat_data.csv", index=False)
qa_scores.to_csv(f"{RAW_PATH}/qa_scores.csv", index=False)
staffing_levels.to_csv(f"{RAW_PATH}/staffing_levels.csv", index=False)

print("✅ Fake contact center data generated successfully.")
