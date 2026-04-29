import csv
import random
from datetime import datetime, timedelta

output_file = "龙岗黄皮_生产活动记录_严格版.csv"
batch_id = "BATCH-HP-002"
start_date = datetime(2026, 3, 1, 12, 0)
total_days = 136
scale_mu = 10  # 10亩
scale_kg = 5000  # 预计产量5000kg

# 注意：EF-FRT-003 的单位是 kgCO2e/hm²，因此活动数据应是面积(hm²)
factor_configs = [
    # 1. 农资阶段 (第1-10天，模拟基肥和早期施药)
    {"id": "EF-FRT-001", "name": "化肥施用", "stage": "1.农资阶段", "days_offset": 0, "duration": 10, "mu_total": 15.0, "sigma_total": 4.0, "ef": 3.285, "act_unit": "kg", "calc_type": "total", "interval": 3},
    {"id": "EF-FRT-002", "name": "农药使用", "stage": "1.农资阶段", "days_offset": 0, "duration": 10, "mu_total": 8.5, "sigma_total": 1.5, "ef": 18.0917, "act_unit": "kg", "calc_type": "total", "interval": 7},
    # 2. 种植阶段 (第11-110天，模拟灌溉)
    {"id": "EF-FRT-003", "name": "灌溉耗电", "stage": "2.种植阶段", "days_offset": 10, "duration": 100, "mu_total": 0.67, "sigma_total": 0.1, "ef": 75.08, "act_unit": "hm²", "calc_type": "total"},  # 10亩≈0.67公顷
    # 3. 收获阶段 (第111-115天)
    {"id": "EF-FRT-004", "name": "机械采摘", "stage": "3.收获阶段", "days_offset": 110, "duration": 5, "mu_total": 28.0, "sigma_total": 5.0, "ef": 2.174, "act_unit": "kg", "calc_type": "total"},
    # 4. 加工阶段 (第116-120天)
    {"id": "EF-FRT-005", "name": "清洗烘干耗电", "stage": "4.加工阶段", "days_offset": 115, "duration": 5, "mu_total": 180.0, "sigma_total": 25.0, "ef": 0.44, "act_unit": "度", "calc_type": "total"},
    # 5. 包装阶段 (第121-125天)
    {"id": "EF-FRT-006", "name": "鲜果包装", "stage": "5.包装阶段", "days_offset": 120, "duration": 5, "mu_total": 85.0, "sigma_total": 12.0, "ef": 8.43, "act_unit": "kg", "calc_type": "total"},
    {"id": "EF-FRT-007", "name": "加工品包装", "stage": "5.包装阶段", "days_offset": 120, "duration": 5, "mu_total": 45.0, "sigma_total": 8.0, "ef": 1.137, "act_unit": "kg", "calc_type": "total"},
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
            # 处理间隔性活动（如施肥、打药）
            if "interval" in cfg and day % cfg["interval"] != 0:
                continue

            current_date = stage_start_date + timedelta(days=day)
            date_str = current_date.strftime('%Y%m%d')
            time_str = current_date.strftime('%Y/%m/%d %H:%M')

            activity_val = max(0.01, random.gauss(cfg["mu_total"], cfg["sigma_total"]))
            carbon_val = activity_val * cfg["ef"]

            type_map = {"EF-FRT-001": "F01", "EF-FRT-002": "P01", "EF-FRT-003": "I01",
                       "EF-FRT-004": "H01", "EF-FRT-005": "E01", "EF-FRT-006": "B01", "EF-FRT-007": "B02"}
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

print(f"✅ 龙岗黄皮仿真数据生成完毕！文件：{output_file}")