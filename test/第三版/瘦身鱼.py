import csv
import random
from datetime import datetime, timedelta

output_file = "白云瘦身鱼_生产活动记录_严格版.csv"
batch_id = "BATCH-FS-003"
start_date = datetime(2026, 3, 10, 12, 0)
total_days = 46
scale = 2000  # 2000尾

factor_configs = [
    # 1. 育种阶段 (第1-20天)
    {"id": "EF-FSH-001", "name": "饲料消耗", "stage": "1.育种阶段", "days_offset": 0, "duration": 20, "mu_per": 0.008, "sigma_per": 0.002, "ef": 0.103, "act_unit": "kg", "calc_type": "per_fish"},
    {"id": "EF-FSH-002", "name": "种苗繁育耗能", "stage": "1.育种阶段", "days_offset": 0, "duration": 20, "mu_total": 35.0, "sigma_total": 6.0, "ef": 0.4403, "act_unit": "度", "calc_type": "total"},
    # 2. 养殖阶段 (第21-66天)
    {"id": "EF-FSH-003", "name": "鱼塘耗电", "stage": "2.养殖阶段", "days_offset": 20, "duration": 26, "mu_total": 45.0, "sigma_total": 8.0, "ef": 0.4419, "act_unit": "度", "calc_type": "total"},  # 养殖至4月5日
    # 3. 加工阶段 (第67-68天) 文档中加工阶段在养殖后，模拟2天
    {"id": "EF-FSH-004", "name": "屠宰分拣耗水", "stage": "3.加工阶段", "days_offset": 46, "duration": 2, "mu_total": 3800.0, "sigma_total": 450.0, "ef": 0.0002, "act_unit": "L", "calc_type": "total"},
    # 4. 运输阶段 (第69天) 批次结束于4月25日，运输安排在此后
    {"id": "EF-FSH-005", "name": "冷链运输", "stage": "4.运输阶段", "days_offset": 48, "duration": 1, "mu_total": 120.0, "sigma_total": 15.0, "ef": 2.68, "act_unit": "L", "calc_type": "total"},
]

def format_value(val, unit):
    return f"{round(val, 5)}({unit})"

def format_carbon(val):
    return f"{round(val, 6)}(kgCO₂e)"

with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["record_id", "batch_id", "factor_id", "record_time", "activity_data", "calculated_carbon"])

    for cfg in factor_configs:
        stage_start_date = start_date + timedelta(days=cfg["days_offset"])
        for day in range(cfg["duration"]):
            current_date = stage_start_date + timedelta(days=day)
            date_str = current_date.strftime('%Y%m%d')
            time_str = current_date.strftime('%Y/%m/%d %H:%M')

            if cfg["calc_type"] == "per_fish":
                activity_val = max(0.001, random.gauss(cfg["mu_per"], cfg["sigma_per"])) * scale
            else:
                activity_val = max(0.01, random.gauss(cfg["mu_total"], cfg["sigma_total"]))

            carbon_val = activity_val * cfg["ef"]

            type_map = {"EF-FSH-001": "F01", "EF-FSH-002": "E01", "EF-FSH-003": "E01",
                       "EF-FSH-004": "W01", "EF-FSH-005": "D01"}
            suffix = type_map.get(cfg["id"], "X01")
            record_id = f"REC-{date_str}-{suffix}"

            writer.writerow([
                record_id,
                batch_id,
                cfg["id"],
                time_str,
                format_value(activity_val, cfg["act_unit"]),
                format_carbon(carbon_val)
            ])

print(f"✅ 白云瘦身鱼仿真数据生成完毕！文件：{output_file}")